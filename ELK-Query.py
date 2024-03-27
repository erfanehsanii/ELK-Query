import requests
import json
from enum import Enum
import redis
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
from datetime import datetime


registry = CollectorRegistry()
gauge_metric = Gauge('healthcheck_metric', 'general application healthcheck',labelnames=["error_type"], registry=registry)



error_log = []
error_log.append(f"{datetime.now()}")
r = redis.Redis()
try:
    r.ping()
    print("Connection to Redis : Successful")
except:
    gauge_metric.labels("redis_connection").set(0)
    print("Connection to Redis : Failed")
    error_log.append("Connection to redis failed")


#----------------- Functions ------------------#

#declare enum for returning the result of checking log file
class Result(Enum):
    Error = 1
    Ok = 2
    Empty = 3


def check_previous_data_existance():

      cursor, keys = r.scan()
      if not keys:
          return Result.Empty

      else:
          return Result.Ok

def get_value_from_redis(key):
    try:
          value = r.get(key)
          return value

    except:
         print("Issue on getting key from redis .. ")
         error_log.append("Issue on getting key from redis")


def set_value_in_redis(key,value):
    try:
          r.set(key,value)

    except:
         print("Issue on setting key in redis .. ")
         error_log.append("Issue on setting key in redis")



def send_message(key,percent):
    webhook_url = ‘<>slack-webhook’

    requests_count = get_value_from_redis(key)
    string_requests_count = requests_count.decode('ascii')

    payload = {
         'text': f'*Drop over RPS* :alert: \n>*Provider:* {key} \n>*Drop Rate:* {int(percent)}% \n>*Requests: {int(string_requests_count)}*'
    }

    try:
        # Send the message to Slack
        response = requests.post(
            webhook_url,
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json'}
            )

        if response.status_code == 200:
            print("Message sent successfully")


        else:
            print("Failed to send message:", response.text)
            gauge_metric.labels("sending_message").set(0)
            error_log.append("Failed to send message to slack")
    except:
            gauge_metric.labels("sending_message").set(0)
            error_log.append("Failed to send message to slack")


def is_main_provider(key):
    if(key == "Mobile Communication Company of Iran PLC" or \
       key == "Iran Cell Service and Communication Company" or \
       key == "Iran Telecommunication Company PJS" or \
       key == "Rightel Communication Service Company PJS"):
        return True

    else:
        return False



#--------------- End Functions -----------------#




headers = {
    'Content-Type': 'application/json',
}

json_data = {
    'size': 0,
    'query': {
        'bool': {
            'must': [
                {
                    'match': {
                        'status.keyword': '200',
                    },
                },
                {
                    'range': {
                        '@timestamp': {
                            'gte': 'now-5m',
                            'lte': 'now',
                        },
                    },
                },
            ],
        },
    },
    'aggs': {
        'top_organizations': {
            'terms': {
                'field': 'organization.keyword',
                'size': 5,
            },
        },
    },
}




try:
    bytes_data = requests.get('http://172.16.29.75:9200/cdn-accesslog-new*/_search', headers=headers, json=json_data)

    content = bytes_data.content
    json_string = content.decode('utf-8')
    response_data = json.loads(json_string)

    previous_data = check_previous_data_existance()

    results = {}
    percentage_result = {}

    buckets = response_data['aggregations']['top_organizations']['buckets']

    if(previous_data == Result.Ok):
        for bucket in buckets:
            try:

                key = bucket['key']
                if(not key) :
                    continue
                print(key)

                 #check if it's main provider
                is_main = is_main_provider(key)
                if(not is_main):
                    continue

                doc_count = bucket['doc_count']
                #results[key] = doc_count

                print(doc_count)

                if (not doc_count):
                    exists = get_value_from_redis(key)
                    if exists:
                        r.delete(key)
                    else:
                        continue

                previous = get_value_from_redis(key)

                if not previous :
                    not_exists_in_redis = is_main_provider(key)
                    if(not_exists_in_redis):
                        set_value_in_redis(key,doc_count)
                        previous = doc_count


                print(previous)
                percent = (int(doc_count) / int(previous)) * 100
                print(percent)
                results[key] = percent
                print("------------------------------")
                #update value in redis
                set_value_in_redis(key , doc_count)
            except Exception as e:
                gauge_metric.labels("calculating_percentage").set(0)
                error_log.append(f"Failed to calculate the percentage - {key}\n {e}")

    elif(previous_data == Result.Empty):
        for bucket in buckets:
            key = bucket['key']
            if(not key) :
                continue

            is_main = is_main_provider(key)
            if(not is_main):
                continue


            doc_count = bucket['doc_count']

            #update value in redis
            set_value_in_redis(key , doc_count)


    elif(previous_data == Result.Error):
        print("Error occured while trying to check redis..")
        gauge_metric.labels("check_redis_value").set(0)
        error_log.append("Error occured while trying to check redis")





    #threshold
    if(previous_data == Result.Ok):
        try:

            for key, value in results.items():
                if(key == "Mobile Communication Company of Iran PLC"):
                    if(value < 100):
                        send_message(key,value)

                if(key == "Iran Cell Service and Communication Company"):
                    if(value < 100):
                        send_message(key,value)

                if(key == "Iran Telecommunication Company PJS"):
                    if(value < 100):
                        send_message(key,value)

                if(key == "Rightel Communication Service Company PJS"):
                    if(value < 100):
                        send_message(key,value)

        except:
            gauge_metric.labels("calculating_threshold").set(0)
            error_log.append("Calculating threshold failed")


except:
    gauge_metric.labels("main_function").set(0)
    error_log.append("error on main function")



# prometheus - pushgateway
try:
    if(len(error_log) == 1):
        gauge_metric.labels("healthy").set(1)

    pushgateway_address = 'http://172.30.33.194:9091'
    push_to_gateway(pushgateway_address, job='metrics', registry=registry)

except:
    gauge_metric.labels("sending_metrics_to_pushgateway").set(0)
    error_log.append("Sending metrics to pushgateway failed")


print("error count :",len(error_log))

if(len(error_log) > 1):
    json_error_log = json.dumps(error_log)
    set_value_in_redis("errors",json_error_log)