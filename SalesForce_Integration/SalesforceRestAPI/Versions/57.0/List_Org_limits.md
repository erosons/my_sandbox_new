Use Post Man to GET API limit

Supply the Bearer token: this is session token genarated from your OAth => access_token)

curl https://MyDomainName.my.salesforce.com/services/data/v57.0/limits/ -H "Authorization: Bearer token" -H "X-PrettyPrint:1"


{
    "AnalyticsExternalDataSizeMB": {
        "Max": 40960,
        "Remaining": 40960
    },
    "ConcurrentAsyncGetReportInstances": {
        "Max": 200,
        "Remaining": 200
    },
    "ConcurrentEinsteinDataInsightsStoryCreation": {
        "Max": 5,
        "Remaining": 5
    },
    "ConcurrentEinsteinDiscoveryStoryCreation": {
        "Max": 2,
        "Remaining": 2
    },
    "ConcurrentSyncReportRuns": {
        "Max": 20,
        "Remaining": 20
    },
    "DailyAnalyticsDataflowJobExecutions": {
        "Max": 60,
        "Remaining": 60
    },
    "DailyAnalyticsUploadedFilesSizeMB": {
        "Max": 51200,
        "Remaining": 51200
    },
    "DailyApiRequests": {
        "Max": 15000,
        "Remaining": 14978,
        "Ant Migration Tool": {
            "Max": 0,
            "Remaining": 0
        },
        "Dataloader Bulk": {
            "Max": 0,
            "Remaining": 0
        },
        "Dataloader Partner": {
            "Max": 0,
            "Remaining": 0
        },
        "Force.com IDE": {
            "Max": 0,
            "Remaining": 0
        },
        "SFIntegration": {
            "Max": 0,
            "Remaining": 0
        },
        "Salesforce Mobile Dashboards": {
            "Max": 0,
            "Remaining": 0
        },
        "Salesforce Touch": {
            "Max": 0,
            "Remaining": 0
        },
        "Salesforce for Outlook": {
            "Max": 0,
            "Remaining": 0
        },
        "Workbench": {
            "Max": 0,
            "Remaining": 0
        }
    },
    "DailyAsyncApexExecutions": {
        "Max": 250000,
        "Remaining": 250000
    },
    "DailyBulkApiRequests": {
        "Max": 15000,
        "Remaining": 15000,
        "Ant Migration Tool": {
            "Max": 0,
            "Remaining": 0
        },
        "Dataloader Bulk": {
            "Max": 0,
            "Remaining": 0
        },
        "Dataloader Partner": {
            "Max": 0,
            "Remaining": 0
        },
        "Force.com IDE": {
            "Max": 0,
            "Remaining": 0
        },
        "SFIntegration": {
            "Max": 0,
            "Remaining": 0
        },
        "Salesforce Mobile Dashboards": {
            "Max": 0,
            "Remaining": 0
        },
        "Salesforce Touch": {
            "Max": 0,
            "Remaining": 0
        },
        "Salesforce for Outlook": {
            "Max": 0,
            "Remaining": 0
        },
        "Workbench": {
            "Max": 0,
            "Remaining": 0
        }
    },
    "DailyDeliveredPlatformEvents": {
        "Max": 10000,
        "Remaining": 10000
    },
    "DailyDurableGenericStreamingApiEvents": {
        "Max": 10000,
        "Remaining": 10000
    },
    "DailyDurableStreamingApiEvents": {
        "Max": 10000,
        "Remaining": 10000
    },
    "DailyEinsteinDataInsightsStoryCreation": {
        "Max": 1000,
        "Remaining": 1000
    },
    "DailyEinsteinDiscoveryPredictAPICalls": {
        "Max": 50000,
        "Remaining": 50000
    },
    "DailyEinsteinDiscoveryPredictionsByCDC": {
        "Max": 500000,
        "Remaining": 500000
    },
    "DailyEinsteinDiscoveryStoryCreation": {
        "Max": 100,
        "Remaining": 100
    },
    "DailyGenericStreamingApiEvents": {
        "Max": 10000,
        "Remaining": 10000,
        "Ant Migration Tool": {
            "Max": 0,
            "Remaining": 0
        },
        "Dataloader Bulk": {
            "Max": 0,
            "Remaining": 0
        },
        "Dataloader Partner": {
            "Max": 0,
            "Remaining": 0
        },
        "Force.com IDE": {
            "Max": 0,
            "Remaining": 0
        },
        "SFIntegration": {
            "Max": 0,
            "Remaining": 0
        },
        "Salesforce Mobile Dashboards": {
            "Max": 0,
            "Remaining": 0
        },
        "Salesforce Touch": {
            "Max": 0,
            "Remaining": 0
        },
        "Salesforce for Outlook": {
            "Max": 0,
            "Remaining": 0
        },
        "Workbench": {
            "Max": 0,
            "Remaining": 0
        }
    },
    "DailyStandardVolumePlatformEvents": {
        "Max": 10000,
        "Remaining": 10000
    },
    "DailyStreamingApiEvents": {
        "Max": 10000,
        "Remaining": 10000,
        "Ant Migration Tool": {
            "Max": 0,
            "Remaining": 0
        },
        "Dataloader Bulk": {
            "Max": 0,
            "Remaining": 0
        },
        "Dataloader Partner": {
            "Max": 0,
            "Remaining": 0
        },
        "Force.com IDE": {
            "Max": 0,
            "Remaining": 0
        },
        "SFIntegration": {
            "Max": 0,
            "Remaining": 0
        },
        "Salesforce Mobile Dashboards": {
            "Max": 0,
            "Remaining": 0
        },
        "Salesforce Touch": {
            "Max": 0,
            "Remaining": 0
        },
        "Salesforce for Outlook": {
            "Max": 0,
            "Remaining": 0
        },
        "Workbench": {
            "Max": 0,
            "Remaining": 0
        }
    },
    "DailyWorkflowEmails": {
        "Max": 1890,
        "Remaining": 1890
    },
    "DataStorageMB": {
        "Max": 5,
        "Remaining": 5
    },
    "DurableStreamingApiConcurrentClients": {
        "Max": 20,
        "Remaining": 20
    },
    "FileStorageMB": {
        "Max": 20,
        "Remaining": 20
    },
    "HourlyAsyncReportRuns": {
        "Max": 1200,
        "Remaining": 1200
    },
    "HourlyDashboardRefreshes": {
        "Max": 200,
        "Remaining": 200
    },
    "HourlyDashboardResults": {
        "Max": 5000,
        "Remaining": 5000
    },
    "HourlyDashboardStatuses": {
        "Max": 999999999,
        "Remaining": 999999999
    },
    "HourlyLongTermIdMapping": {
        "Max": 100000,
        "Remaining": 100000
    },
    "HourlyManagedContentPublicRequests": {
        "Max": 50000,
        "Remaining": 50000
    },
    "HourlyODataCallout": {
        "Max": 1000,
        "Remaining": 996
    },
    "HourlyPublishedPlatformEvents": {
        "Max": 50000,
        "Remaining": 50000
    },
    "HourlyPublishedStandardVolumePlatformEvents": {
        "Max": 1000,
        "Remaining": 1000
    },
    "HourlyShortTermIdMapping": {
        "Max": 100000,
        "Remaining": 100000
    },
    "HourlySyncReportRuns": {
        "Max": 500,
        "Remaining": 500
    },
    "HourlyTimeBasedWorkflow": {
        "Max": 1000,
        "Remaining": 1000
    },
    "MassEmail": {
        "Max": 10,
        "Remaining": 10
    },
    "MonthlyEinsteinDiscoveryStoryCreation": {
        "Max": 500,
        "Remaining": 500
    },
    "MonthlyPlatformEvents": {
        "Max": 300000,
        "Remaining": 300000
    },
    "Package2VersionCreates": {
        "Max": 6,
        "Remaining": 6
    },
    "Package2VersionCreatesWithoutValidation": {
        "Max": 500,
        "Remaining": 500
    },
    "PrivateConnectOutboundCalloutHourlyLimitMB": {
        "Max": 0,
        "Remaining": 0
    },
    "SingleEmail": {
        "Max": 15,
        "Remaining": 15
    },
    "StreamingApiConcurrentClients": {
        "Max": 20,
        "Remaining": 20
    }
}