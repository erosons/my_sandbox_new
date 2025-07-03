## INTRODUCTION
Monte Carlo uses machine learning to infer and learn what the datasets looks like, proactively identify
downtime, assess its impact, nd noitfy those who need to know.

For Monitoring and Alerting on 
- ETL 
- Data Warehouse
- Data lakes 
- BI-tools

# What the Pillars and what are we monitoring and then Alerting to specific Owners
   - Freshness: How up-to-date data tables are and update frequency or cadence of how the table update 
   - Volume based on growth trend : Based on completeness of the data
   - Quality : Monioring the table values on certain threshold amd alerting if they fall out of acceptable standards
   - Schema we here doing schema validation and monitoring all schema changes in the environment
   - Lineage: Monitors the upstream sources and downstream ingestors of data by higlight the imapct it raduis by a break in your data

# Monitoring
 - Field Health -> dips and spike  in stats like null uniqueness with threshold
 - Custom SQL rule
 - Json Schema-> Monitor schema changes (addition or removal)
 - Dimension tracking -> (fields cardinality and fields cardinality) app, geo,
 - Freshness and Volume SLI (dectectors with custom thresolds for table freshness and volume changes data size)

# Data Layers
Bronze - Data Lake (s3,hDFS,ADLS)  (Spark, Airflow)
Silver - DataWarehouse (snowflake,Redshift,BigQuery, Trino) (DBT, Spark, Airflow)
Gold - Data Science Analytics (Tableau,PowerBi, QuickInsght, Looker)
    
Monte Carlo Agent (Data Montiors systems)    [Metadata => [Logs, Queries,runtime, usage, depedencies)
 - Pipeline Observability
 - Assets
 - Domain

# Actions and Configurations
- OOTB ML monitors
   - Freshness
   - Volume
   - Schema
- Custom ML Monitors
   - Field Health
   - JSon Schema
   - Dimension Tracking
- Rules Based Monitor
  - SQL Rules
  - Freshness SLI
  - Volume SLI 

# Obervability Management Output
   - incident Management (Slacks,Pager,duty)
       - RCA
       - Alerting
       - Incident Status
       - Blast
       - Affected Reports
       - Query Logd
       - Incident comms

   - Insights Visibity (Snowflake,BigQuery, Redishift)
     - Key Assest base of table be written to
     - Event History
     - Misconfigured
     - Monitors
     - Heavy Queries impact
     - Cleanup for redundant data asessts
     - Monitors coverage 
     - Incidents history

# Domain Design Stragies
   Domains are set of tables in MonteCarlo , used as a way to organize data within the platform,
   This can be projects or Schemas directly from the warehouse or pick a chort of relevants tables
   - Benefits
      - ACL (Editor, Admin, Viewer)
      - Restrict Incidence Mangement (Only users in that domain can have to see the incidents that happenon those tables)
      - Build Domain specific notifications channel (Reduce Noise , Alert Fatigue)
      - Reporting: Provides a great over of the landscape to understand team that are struggling
      - use API -> this can be done via CLI

# Key Assests & Key Assest Report
   Is a Feature that help find the most used 
   - Tables and View in a datawarehouse -> Allow us to design a strategy for faster respond time to incident or addional monitoting 
   - This are activity driven table or view and score are assigned to them based on the last 30days
   Table important Scores are based
      - Numbers of reads
      - Number of score
      - Number of users 
      - The degree of connectivity base on how many users are connected (Upstream and Downstream)
      - The update Cadence pf an Assets and age and freshness
      NOTE: Assests usually have importance score greater > 0.8

# Assets
 - Gives you the full details of the tables in data warehouse
   Further anlysis at the level of each table Assets
   Summary
      - alerts
      - freshness
      - volume
      - Schema are automatically tracked.
   Monitors:
    - Table Monitors
    - Metric Monitors
    - Other Monitors

   Data Explorer:
    - This can be used for profiling the table Assets
   General Information:
    - Usahe information of the key Assets

# Lineage, 
  This helps us identify (upstream and Downstream) fields and table to estimate what broken before setting severity
  - Table Level Lineage
  - Field level Lineage

# Dashboard:



# Data Collector -> Agent to collect data from snowflow flake.
Connect to Software datawarehouse
This uses Private-public-key to connect from snowflake from Monte Carlo to Snowflake.
 See snowflake key pair instruction

# SEE instructions to setUP the Integration

# Setup CLI for integration Create and ENV to aviod conflicts -> MonteCarlo
 >> pip install pip install -U montecarlodata
 
 - SetUp your API key on the UI in the API secetion to integrate
   >>  pip install -U montecarlodata
   >>> pip install -U montecarlodata
   >>> montecarlo --version
   >>> montecarlo configure (KEY ID and secret)
   >>> montecarlo validate

# Monitor Capabilities :https://docs.getmontecarlo.com/docs/monitors-as-code
   # Overview

   Monte Carlo developed a YAML-based monitors configuration to help teams deploy monitors as part of their CI/CD process. The following guide explains how to get started with monitors as code.

   Create Montecarlo Project -> Folder

   First, you will need to create a Monte Carlo project. 
   A Monte Carlo project is simply a directory which contains a montecarlo.yml file, which contains project-level configuration options. If you are using DBT, we recommend placing montecarlo.yml in the same directory as dbt_project.yml

## Congiguration files required
- montecarlo.yml to identify your targetDB
- custom_sql.yml

## Runing your .yml cases
 >> montecarlo monitors apply --dry-run
 >> montecarlo monitors apply