{
  "__inputs": [
    {
      "name": "DS_PROMETHEUS.INTERNAL-ODMONT.COM",
      "label": "prometheus.internal-odmont.com",
      "description": "",
      "type": "datasource",
      "pluginId": "prometheus",
      "pluginName": "Prometheus"
    }
  ],
  "__elements": [],
  "__requires": [
    {
      "type": "grafana",
      "id": "grafana",
      "name": "Grafana",
      "version": "8.5.3"
    },
    {
      "type": "datasource",
      "id": "prometheus",
      "name": "Prometheus",
      "version": "1.0.0"
    },
    {
      "type": "panel",
      "id": "stat",
      "name": "Stat",
      "version": ""
    },
    {
      "type": "panel",
      "id": "state-timeline",
      "name": "State timeline",
      "version": ""
    },
    {
      "type": "panel",
      "id": "text",
      "name": "Text",
      "version": ""
    },
    {
      "type": "panel",
      "id": "timeseries",
      "name": "Time series",
      "version": ""
    }
  ],
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": {
          "type": "grafana",
          "uid": "-- Grafana --"
        },
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "target": {
          "limit": 100,
          "matchAny": false,
          "tags": [],
          "type": "dashboard"
        },
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": null,
  "iteration": 1655913813644,
  "links": [],
  "liveNow": false,
  "panels": [
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 0
      },
      "id": 49,
      "panels": [],
      "title": "Cluster Metrics",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "dark-red",
                "value": 0
              },
              {
                "color": "green",
                "value": 1
              }
            ]
          },
          "unit": "bool_yes_no"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 3,
        "x": 0,
        "y": 1
      },
      "id": 16,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "textMode": "auto"
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_up{env=~\"$env\"}",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "MongoService UP",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "Mongodb Service Uptime in hours",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "#65882d",
                "value": null
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 5,
        "x": 3,
        "y": 1
      },
      "id": 18,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {
          "titleSize": 15,
          "valueSize": 15
        },
        "textMode": "auto"
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_members_uptime{env=~\"$env\", member_state=\"PRIMARY\"}",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Mongodb Uptime",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "The number of incoming connections from clients to the database server. This number includes the current shell session. Consider the value of connections.available to add more context to this datum.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "semi-dark-green",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 4,
        "x": 8,
        "y": 1
      },
      "id": 20,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {
          "titleSize": 15,
          "valueSize": 15
        },
        "textMode": "auto"
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_ss_connections{env=\"$env\", conn_type=\"current\"}",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Current Connections",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "Count of all incoming connections created to the server. This number includes connections that have since closed.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "semi-dark-green",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 4,
        "x": 12,
        "y": 1
      },
      "id": 22,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {
          "titleSize": 15,
          "valueSize": 15
        },
        "textMode": "auto"
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_ss_connections{env=\"$env\", conn_type=\"totalCreated\"}",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Total Created Connections",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "The number of unused incoming connections available. Consider this value in combination with the value of connections.current to understand the connection load on the database, and the UNIX ulimit Settings document for more information about system thresholds on available connections.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "semi-dark-green",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 4,
        "x": 16,
        "y": 1
      },
      "id": 21,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {
          "titleSize": 15,
          "valueSize": 15
        },
        "textMode": "auto"
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_ss_connections{env=\"$env\", conn_type=\"available\"}",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Available Connections",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "The number of active client connections to the server. Active client connections refers to client connections that currently have operations in progress.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "semi-dark-green",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 4,
        "x": 20,
        "y": 1
      },
      "id": 23,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {
          "titleSize": 15,
          "valueSize": 15
        },
        "textMode": "auto"
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_ss_connections{env=\"$env\", conn_type=\"available\"}",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Active Connections",
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "",
      "gridPos": {
        "h": 2,
        "w": 24,
        "x": 0,
        "y": 9
      },
      "id": 25,
      "options": {
        "content": "A document that reports on database operations by type since the mongod instance last started. These numbers will grow over time until next restart. Analyze these values over time to track database utilization.",
        "mode": "markdown"
      },
      "pluginVersion": "8.5.3",
      "title": "opcounters",
      "type": "text"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "The total number of insert operations received since the mongod instance last started.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-yellow",
                "value": null
              }
            ]
          },
          "unit": "ops"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 0,
        "y": 11
      },
      "id": 26,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "rate(mongodb_ss_opcounters{env=\"$env\", legacy_op_type=\"insert\"}[$__interval])",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Received Insert Operations",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "The total number of update operations received since the mongod instance last started.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-yellow",
                "value": null
              }
            ]
          },
          "unit": "ops"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 8,
        "y": 11
      },
      "id": 28,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "rate(mongodb_ss_opcounters{env=\"$env\", legacy_op_type=\"update\"}[$__interval])",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Received Update Operations",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "The total number of commands issued to the database since the mongod instance last started.\n\nopcounters.command counts all commands except the write commands: insert, update, and delete.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-yellow",
                "value": null
              }
            ]
          },
          "unit": "ops"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 16,
        "y": 11
      },
      "id": 30,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "rate(mongodb_ss_opcounters{env=\"$env\", legacy_op_type=\"command\"}[$__interval])",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Received Command Operations",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "The total number of queries received since the mongod instance last started.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 6,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-yellow",
                "value": null
              }
            ]
          },
          "unit": "ops"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 0,
        "y": 19
      },
      "id": 27,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "rate(mongodb_ss_opcounters{env=\"$env\", legacy_op_type=\"query\"}[$__interval])",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Received Queries",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "The total number of delete operations since the mongod instance last started.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-yellow",
                "value": null
              }
            ]
          },
          "unit": "ops"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 8,
        "y": 19
      },
      "id": 29,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "rate(mongodb_ss_opcounters{env=\"$env\", legacy_op_type=\"delete\"}[$__interval])",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Received Delete Operations",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "The total number of getMore operations since the mongod instance last started. This counter can be high even if the query count is low. Secondary nodes send getMore operations as part of the replication process.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-yellow",
                "value": null
              }
            ]
          },
          "unit": "ops"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 16,
        "y": 19
      },
      "id": 31,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "rate(mongodb_ss_opcounters{env=\"$env\", legacy_op_type=\"getmore\"}[$__interval])",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Received getMore Operations",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "Number of collections in the database.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "continuous-GrYlRd"
          },
          "custom": {
            "fillOpacity": 60,
            "lineWidth": 0,
            "spanNulls": false
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 0,
        "y": 27
      },
      "id": 33,
      "options": {
        "alignValue": "center",
        "legend": {
          "displayMode": "list",
          "placement": "bottom"
        },
        "mergeValues": true,
        "rowHeight": 0.93,
        "showValue": "always",
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_dbstats_collections{env=\"$env\", instance=\"$instance\"}",
          "legendFormat": "{{database}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Total Collections/DB",
      "type": "state-timeline"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "Total number of indexes across all collections in the database.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "continuous-GrYlRd"
          },
          "custom": {
            "fillOpacity": 60,
            "lineWidth": 0,
            "spanNulls": false
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 8,
        "y": 27
      },
      "id": 34,
      "options": {
        "alignValue": "center",
        "legend": {
          "displayMode": "list",
          "placement": "bottom"
        },
        "mergeValues": true,
        "rowHeight": 0.93,
        "showValue": "always",
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_dbstats_indexes{env=\"$env\", instance=\"$instance\"}",
          "legendFormat": "{{database}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Total Indexs/DB",
      "type": "state-timeline"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "Number of views in the database.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "continuous-GrYlRd"
          },
          "custom": {
            "fillOpacity": 60,
            "lineWidth": 0,
            "spanNulls": false
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 8,
        "x": 16,
        "y": 27
      },
      "id": 35,
      "options": {
        "alignValue": "center",
        "legend": {
          "displayMode": "list",
          "placement": "bottom"
        },
        "mergeValues": true,
        "rowHeight": 0.93,
        "showValue": "always",
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_dbstats_views{env=\"$env\", instance=\"$instance\"}",
          "legendFormat": "{{database}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Total Views/DB",
      "type": "state-timeline"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "Sum of the space allocated to all collections in the database for document storage, including free space.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 35
      },
      "id": 37,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_dbstats_storageSize{env=\"$env\", instance=\"$instance\"}",
          "legendFormat": "{{database}} ",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Allocated Storage to Collections in DB",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "Sum of the space allocated to all indexes in the database, including free index space.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 35
      },
      "id": 38,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_dbstats_indexSize{env=\"$env\", instance=\"$instance\"}",
          "legendFormat": "{{database}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Allocated Storage to Indexs in DB",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 43
      },
      "id": 14,
      "panels": [],
      "title": "Replication Set Metrics",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "semi-dark-blue",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 7,
        "x": 0,
        "y": 44
      },
      "id": 42,
      "options": {
        "colorMode": "background",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {
          "valueSize": 30
        },
        "textMode": "name"
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_rs_members_id{env=\"$env\", member_state=\"PRIMARY\", instance=\"$instance\"}",
          "legendFormat": "{{member_state}} - {{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "This metric can show a correlation with the replication lag value.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "ms"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 9,
        "w": 8,
        "x": 7,
        "y": 44
      },
      "id": 47,
      "options": {
        "legend": {
          "calcs": [
            "last"
          ],
          "displayMode": "table",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_rs_members_pingMs{env=\"$env\", instance=\"$instance\"}",
          "legendFormat": "{{member_state}} - {{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Max Member Ping Time - $instance",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "The oplog (operations log) is a special capped collection that keeps a rolling record of all operations that modify the data stored in your databases.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 14,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-yellow",
                "value": null
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": [
          {
            "matcher": {
              "id": "byName",
              "options": "172.31.11.244:9216"
            },
            "properties": [
              {
                "id": "color",
                "value": {
                  "fixedColor": "semi-dark-orange",
                  "mode": "fixed"
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 9,
        "w": 9,
        "x": 15,
        "y": 44
      },
      "id": 40,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_oplog_stats_size{env=\"$env\", instance=\"$instance\", rs_nm=\"$rs\"}",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "OPLog Size",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "semi-dark-blue",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 5,
        "w": 7,
        "x": 0,
        "y": 48
      },
      "id": 43,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "textMode": "name"
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_rs_members_id{env=\"$env\", member_state=\"SECONDARY\", instance=\"$instance\"}",
          "legendFormat": "{{member_state}} - {{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "type": "stat"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "MongoDB replication lag occurs when the secondary node cannot replicate data fast enough to keep up with the rate that data is being written to the primary node. It could be caused by something as simple as network latency, packet loss within your network, or a routing issue.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 22,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "ms"
        },
        "overrides": [
          {
            "__systemRef": "hideSeriesFrom",
            "matcher": {
              "id": "byNames",
              "options": {
                "mode": "exclude",
                "names": [
                  "{cl_id=\"62961a7e162f952813b8d646\", env=\"DEV\", instance=\"172.31.11.244:9216\", job=\"mongodb_exporter\", member_idx=\"172.31.11.244:27017\", member_state=\"SECONDARY\", rs_nm=\"repl\", rs_state=\"2\"}"
                ],
                "prefix": "All except:",
                "readOnly": true
              }
            },
            "properties": [
              {
                "id": "custom.hideFrom",
                "value": {
                  "legend": false,
                  "tooltip": false,
                  "viz": true
                }
              }
            ]
          }
        ]
      },
      "gridPos": {
        "h": 9,
        "w": 20,
        "x": 0,
        "y": 53
      },
      "id": 53,
      "options": {
        "legend": {
          "calcs": [
            "last",
            "mean",
            "max",
            "min"
          ],
          "displayMode": "table",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_rs_members_optimeDate{env=\"$env\", instance=\"$instance\", rs_nm=\"$rs\"} - mongodb_rs_members_optimeDate{env=\"$env\", instance=\"$instance\", rs_nm=\"$rs\"}",
          "legendFormat": "{{member_state}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Replication Lag",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "This shows the time since the last election.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "dark-green",
                "value": null
              }
            ]
          },
          "unit": "dateTimeAsLocal"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 9,
        "w": 4,
        "x": 20,
        "y": 53
      },
      "id": 45,
      "options": {
        "colorMode": "background",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "textMode": "auto"
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "expr": "mongodb_electionCandidateMetrics_lastElectionDate{env=\"$env\"}",
          "refId": "A"
        }
      ],
      "title": "ReplSet Last Election",
      "type": "stat"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 62
      },
      "id": 2,
      "panels": [],
      "title": "Cursor Metrics",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "Cursor is a pointer, and using this pointer we can access the document. cursor.timeOut property was updated incrementally, and connections that died without closing the cursor. The consequence is that it will remain open on the server and consume memory unless it is reaped by the default MongoDB setting.",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 9,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "semi-dark-orange",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 63
      },
      "id": 55,
      "options": {
        "legend": {
          "calcs": [
            "last",
            "mean",
            "max"
          ],
          "displayMode": "table",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_ss_metrics_cursor_timedOut{env=\"$env\", rs_nm=\"$rs\"}",
          "legendFormat": "{{instance}} - {{rs_nm}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Cursor Timeout",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "description": "Number of cursors currently opened by MongoDB for clients",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "semi-dark-orange",
                "value": null
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 63
      },
      "id": 56,
      "options": {
        "legend": {
          "calcs": [
            "last",
            "mean",
            "max"
          ],
          "displayMode": "table",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "mongodb_ss_metrics_cursor_totalOpened{env=\"$env\", rs_nm=\"$rs\"}",
          "legendFormat": "{{instance}} - {{rs_nm}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Cursor totalOpened",
      "type": "timeseries"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 71
      },
      "id": 51,
      "panels": [],
      "title": "Server Metrics",
      "type": "row"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "never",
            "spanNulls": true,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "percent"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 72
      },
      "id": 4,
      "options": {
        "legend": {
          "calcs": [
            "lastNotNull",
            "min",
            "max",
            "mean"
          ],
          "displayMode": "table",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "multi",
          "sort": "desc"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "avg(rate(node_cpu_seconds_total{env=\"$env\", mode=\"system\"}[$interval])) by (instance) *100",
          "hide": false,
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "CPU% Basic",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineStyle": {
              "fill": "solid"
            },
            "lineWidth": 2,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "bytes"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 72
      },
      "id": 6,
      "options": {
        "legend": {
          "calcs": [
            "lastNotNull",
            "max",
            "mean",
            "sum"
          ],
          "displayMode": "table",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "node_memory_MemTotal_bytes{env=\"$env\", job=\"$nodeJob\"} - node_memory_MemFree_bytes{env=\"$env\", job=\"$nodeJob\"} - (node_memory_Cached_bytes{env=\"$env\", job=\"$nodeJob\"} + node_memory_Buffers_bytes{env=\"$env\", job=\"$nodeJob\"})",
          "hide": false,
          "legendFormat": "{{instance}} - RAM Used",
          "range": true,
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "node_memory_Cached_bytes{env=\"$env\", job=\"$nodeJob\"} + node_memory_Buffers_bytes{env=\"$env\", job=\"$nodeJob\"} + node_memory_SReclaimable_bytes{env=\"$env\", job=\"$nodeJob\"}",
          "hide": false,
          "legendFormat": "{{instance}} - Buffer Mem",
          "range": true,
          "refId": "B"
        }
      ],
      "title": "Memory Utilization",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "binBps"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 0,
        "y": 80
      },
      "id": 12,
      "options": {
        "legend": {
          "calcs": [
            "mean",
            "min",
            "max"
          ],
          "displayMode": "table",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "irate(node_network_receive_bytes_total{env=\"$env\", job=\"$nodeJob\"}[5m])",
          "legendFormat": "{{instance}}-{{device}} - Receives",
          "range": true,
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "irate(node_network_transmit_bytes_total{env=\"$env\", job=\"$nodeJob\"}[5m])",
          "hide": false,
          "legendFormat": "{{instance}}-{{device}} - Transmit",
          "range": true,
          "refId": "B"
        }
      ],
      "title": "Network I/O",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 21,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineStyle": {
              "fill": "solid"
            },
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "binBps"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 12,
        "x": 12,
        "y": 80
      },
      "id": 10,
      "options": {
        "legend": {
          "calcs": [
            "min",
            "max",
            "mean"
          ],
          "displayMode": "table",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "rate(node_disk_read_bytes_total{env=\"$env\", job=\"$nodeJob\",device=~\"$device\"}[$interval])",
          "legendFormat": "{{instance}}-{{device}} - Reads",
          "range": true,
          "refId": "A"
        },
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "rate(node_disk_written_bytes_total{env=\"$env\", job=\"$nodeJob\",device=~\"$device\"}[$interval])",
          "hide": false,
          "legendFormat": "{{instance}}-{{device}} - Write",
          "range": true,
          "refId": "B"
        }
      ],
      "title": "Disk I/O",
      "type": "timeseries"
    },
    {
      "datasource": {
        "type": "prometheus",
        "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
      },
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "palette-classic"
          },
          "custom": {
            "axisLabel": "",
            "axisPlacement": "auto",
            "barAlignment": 0,
            "drawStyle": "line",
            "fillOpacity": 0,
            "gradientMode": "none",
            "hideFrom": {
              "legend": false,
              "tooltip": false,
              "viz": false
            },
            "lineInterpolation": "linear",
            "lineWidth": 1,
            "pointSize": 5,
            "scaleDistribution": {
              "type": "linear"
            },
            "showPoints": "auto",
            "spanNulls": false,
            "stacking": {
              "group": "A",
              "mode": "none"
            },
            "thresholdsStyle": {
              "mode": "off"
            }
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 6,
        "w": 24,
        "x": 0,
        "y": 88
      },
      "id": 8,
      "options": {
        "legend": {
          "calcs": [],
          "displayMode": "list",
          "placement": "bottom"
        },
        "tooltip": {
          "mode": "single",
          "sort": "none"
        }
      },
      "pluginVersion": "8.5.3",
      "targets": [
        {
          "datasource": {
            "type": "prometheus",
            "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
          },
          "editorMode": "code",
          "expr": "100 - ((node_filesystem_avail_bytes{env=\"$env\", job=\"$nodeJob\",device!~'rootfs'} * 100) / node_filesystem_size_bytes{env=\"$env\", job=\"$nodeJob\",device!~'rootfs'})",
          "legendFormat": "{{instance}}",
          "range": true,
          "refId": "A"
        }
      ],
      "title": "Disk Space Utilization",
      "type": "timeseries"
    }
  ],
  "refresh": "",
  "schemaVersion": 36,
  "style": "dark",
  "tags": [],
  "templating": {
    "list": [
      {
        "current": {
          "selected": false,
          "text": "prometheus.internal-odmont.com",
          "value": "prometheus.internal-odmont.com"
        },
        "hide": 0,
        "includeAll": false,
        "label": "Datasource",
        "multi": false,
        "name": "datasource",
        "options": [],
        "query": "prometheus",
        "queryValue": "",
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "type": "datasource"
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
        },
        "definition": "label_values(mongodb_up, env)",
        "hide": 0,
        "includeAll": false,
        "label": "env",
        "multi": false,
        "name": "env",
        "options": [],
        "query": {
          "query": "label_values(mongodb_up, env)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "type": "query"
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
        },
        "definition": "label_values(mongodb_up{env=\"$env\"}, job)",
        "hide": 2,
        "includeAll": false,
        "label": "",
        "multi": false,
        "name": "mongoJob",
        "options": [],
        "query": {
          "query": "label_values(mongodb_up{env=\"$env\"}, job)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "type": "query"
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
        },
        "definition": "label_values(node_uname_info, nodename)",
        "hide": 2,
        "includeAll": false,
        "label": "Hostname",
        "multi": false,
        "name": "hostname",
        "options": [],
        "query": {
          "query": "label_values(node_uname_info, nodename)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "type": "query"
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
        },
        "definition": "label_values(mongodb_up{env=\"$env\"}, instance)",
        "hide": 0,
        "includeAll": false,
        "label": "Instance",
        "multi": false,
        "name": "instance",
        "options": [],
        "query": {
          "query": "label_values(mongodb_up{env=\"$env\"}, instance)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "type": "query"
      },
      {
        "auto": false,
        "auto_count": 30,
        "auto_min": "10s",
        "current": {
          "selected": false,
          "text": "30s",
          "value": "30s"
        },
        "hide": 2,
        "name": "interval",
        "options": [
          {
            "selected": true,
            "text": "30s",
            "value": "30s"
          },
          {
            "selected": false,
            "text": "1m",
            "value": "1m"
          },
          {
            "selected": false,
            "text": "2m",
            "value": "2m"
          },
          {
            "selected": false,
            "text": "3m",
            "value": "3m"
          },
          {
            "selected": false,
            "text": "5m",
            "value": "5m"
          },
          {
            "selected": false,
            "text": "10m",
            "value": "10m"
          },
          {
            "selected": false,
            "text": "30m",
            "value": "30m"
          }
        ],
        "query": "30s,1m,2m,3m,5m,10m,30m",
        "refresh": 2,
        "skipUrlSync": false,
        "type": "interval"
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
        },
        "definition": "label_values(node_uname_info, job)",
        "hide": 2,
        "includeAll": false,
        "multi": false,
        "name": "nodeJob",
        "options": [],
        "query": {
          "query": "label_values(node_uname_info, job)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "type": "query"
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
        },
        "definition": "label_values(node_filesystem_size_bytes, mountpoint)",
        "hide": 0,
        "includeAll": false,
        "label": "Mountpoints",
        "multi": false,
        "name": "mountpoint",
        "options": [],
        "query": {
          "query": "label_values(node_filesystem_size_bytes, mountpoint)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "type": "query"
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
        },
        "definition": "label_values(node_disk_reads_completed_total, device)",
        "hide": 2,
        "includeAll": false,
        "label": "",
        "multi": false,
        "name": "device",
        "options": [],
        "query": {
          "query": "label_values(node_disk_reads_completed_total, device)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "type": "query"
      },
      {
        "current": {},
        "datasource": {
          "type": "prometheus",
          "uid": "${DS_PROMETHEUS.INTERNAL-ODMONT.COM}"
        },
        "definition": "label_values(mongodb_rs_ok{env=\"$env\"}, rs_nm)",
        "hide": 0,
        "includeAll": false,
        "label": "ReplicaSet",
        "multi": false,
        "name": "rs",
        "options": [],
        "query": {
          "query": "label_values(mongodb_rs_ok{env=\"$env\"}, rs_nm)",
          "refId": "StandardVariableQuery"
        },
        "refresh": 1,
        "regex": "",
        "skipUrlSync": false,
        "sort": 0,
        "type": "query"
      }
    ]
  },
  "time": {
    "from": "now-6h",
    "to": "now"
  },
  "timepicker": {},
  "timezone": "",
  "title": "Opstree/Mongodb Dashboard",
  "uid": "SsEeTs97k",
  "version": 37,
  "weekStart": "",
  "gnetId": 16490,
  "description": "MongoDB Dashboard with Cluster, Replication, cursor, and server metrics using Mongodb Exporter by percona"
}