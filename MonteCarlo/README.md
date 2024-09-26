## INTRODUCTION
Monte Carlo uses machine learning to infer and learn what the datasets looks like, proactively identify
downtime, assess its impact, nd noitfy those who need to know.

For Monitoring and Alerting on 
- ETL 
- Data Warehouse
- Data lakes 
- BI-tools

What were we monitoring and  then Alerting to specific Owners
- Freshness load date
- Volume based on growth trend
- Thresold monitoring of data.
- Distribution
- Schema we here doing schema validation
- Lineage

# Monitoring
 - Field Health -> dips and spike  in stats like null uniqueness with threshold
 - Custom SQL rule
 - Json Schema-> Monitor schema changes (addition or removal)
 - Dimension tracking -> (fields cardinality and fields cardinality) app, geo,
 - Freshness and Volume SLI (dectectors with custom thresolds for table freshness and volume changes data size)

# Track Incident Management
   Incident monitoring for bridges and Managment

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