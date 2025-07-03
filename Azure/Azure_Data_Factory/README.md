## Data Factory
 # Coping data (80 connector this core job) 
 # Transform data file format and attributes mapping
 # Dataflow just like in SSIS
This is the cloud version of SSIS -> SQL Server integration system
- Desiging
- Building
- testing
- Deploying
- Managing Application and Services
Batch processing with Databrick andADF
- Creating pipelines
- Creating Schedule
- Creating Event Based Triggers
- Linking Services and task
- Select Windws function, configure input and output for streaming data solutiond
- Configure ELT used in Polybase

## Build Options:
- PowerShell, Python, REST

## Integration
- DevOPs, key Vault , Monitor , Automation, databricks

## HTTP/TLS in transit


## ADF pipeline Activities can be categorized
    - Data Movement -> Copy Data activities
    - Transform -> Databricks Notebook (SQL,python)/HDinsight
    - Control Activties -> Filter,ForEach,ifConditions,Switch,Until

## Validation and Publishing
    - Basically involve checking all pipeline Status a working and then saving it


    Dataset <----------> Activities <------ Pipelines
    |
    |
    Linked services

## INTEGRATION RUNTIME:
    Provide the compute ,serverless azure managed infrastructure (PAY as you use)
    - IAAS (Software installation, Patching,Capacity/Scaling)
    - A Bridge or platform between Linked Services and Activity
    -  Activity/task defined within the action
    -  Linked Services define the integration location


## OPERATIONS PERFORMED  Integration Runtime
    - Data Flow (data transformation)
    - Data Movement
    - Format conversion, column mapping,serialization and deserialization
    - Provides the native compute to  move data between cloud data store in a secure, reliable and high performance manner.
    - Activity dispatch: Dispatch activities to (Databricks Notebook,spark,hive, HDinsight) for their respective execution
    - SSIS package Execution


## TYPES
   # Default
        - AutoResolveIntegrationRuntime: This help runs IR in the closest Location to our sources and resolve by ADF itself
    - Azure IR: When all sources & sink are cloud hosted (Public network),Data flow, data movement, activity dispatch
 # Configuration settings:
            You might have restrictions specifics based GDPR, for data not to leave a region, in such scenario you 
            You will need to provision the IR in those specific region rather allowing auto resolve, and metadata will be saved in region of provisoning

    - Self-hosted IR-> if the source and destination data are in private/premise,then we have to use IR installed in Private network.
# Configurations settings:  
    - Azure-SSIS IR -> when dealing with SSIS package execution (public or Private)
    - Airflow -> 

# TRIGGERS (1:M or M:1 relationships between trigger and pipelines)
   - Schedule : When you want to schedule a pipeline to run at particular hour/day/Month or time or reoccurence I choose schedule
   - Tumbling Windows: Advance option of scheduling
         the context of tumbling (minutes or hourly offset for a pipeline example a hourly schedule will 24 windows)
       - Allows you to do backfilling,
       - Target only one pipeline and maintains state e.g if a pipeline is suppose to start at 10am UTC and got delayed by upstream
         task, the starttime state will remain the same as 10am UTC, even if starts late
       - Allows for trigger depedencies on offset of windows sizes.
       # Depedency scenario
        - Dependence A->B Offset:1hr  of say and 1hour -> this means the pipeline B schedule say 10-11 will only run if schedule A 9-10 was sucessful
        - Dependence A->B offset:1hr, Window size:2hr -> this his means the pipeline B schedule say 10-11 will only run if schedule A  
          9-11 was sucessful
        - Self-dependency: A-A : these are DAGs, downstream task will not run until upstream is successful.
      # Additional Features:
       - Delay ->
       - Max concurrency -> Here in this scenario you want to trigger multiple task at the same time, say a backfill window of last 24hrs, where a the first 1-10 windows are triggered at the same time, then another 10 windows will start, until all the task are completed.
       Retry: wait time before retrying a failed task
       Activate (Y/N)
   - Storage events:
      This will trigger based on actions(put or delete file from a storage) a trigger will file to process the file

   - Custom events

   use salesDB;
Create Table Sales (
RowID int,
OrderID int,
OrderDate date,
Shipdate date,
Discount float,
Profit float
);