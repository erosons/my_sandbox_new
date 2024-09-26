# Setting up DBT Cloud
https://docs.getdbt.com/guides/redshift?step=1

# Build your own Adapter
https://docs.getdbt.com/guides/adapter-creation?step=1

# Help 
--https://community.getdbt.com/

List of DBT Adapters (Trusted or Community)
- pip install dbt-core
- pip install dbt-sqlserver
- pip install dbt-bigquery
- pip install dbt-databricks
- pip install dbt-athena-community
- pip install dbt-synapse
- pip install dbt-databricks
- pip install dbt-postgres
- pip install dbt-dremio
- pip install dbt-snowflake
- pip install dbt-trino
- pip install dbt-teradata
- pip install dbt-glue
- pip install dbt-redshift
- pip install dbt-oracle
- python -m pip install dbt-core dbt-hive

Intialize youe virtualenv
Install dbt-core
Install required  Adapter

## Kick Starting DBT Project

create ~/.dbt/profiles.yml

## Note your profiles.yml are sources configuration filename should be lower case
- In this directory  in linux ~/.dbt
- In windows in this directory ~\.dt
Add your source cofiguration see dbt webpage

# Next Initialize A project
>>> dbt init Cocacola_DWH   Note : make sure you are the dbt-core environment , for bigquery profiles.yaml is automatically setup
      map  your target database _name to the profiles.yaml -> projetName
      map the database credentials
      cd to the EDW directory

## Validates the profiles.yaml  -> validate structure
>>  dbt parse    

## dbt debug   -> Validates the database -> connectivity
>>  dbt debug  
    - validates profiles.yml file
    - dbt_project.yml file
    - Required dependencies:
    Git Tracking Executing "git --help"

## dbt complie  -> validating end -end connection for errors
  This test all you model without executimg the code.

for test cases ->>> dbt compile  -m warehouse.fact_sales

## Command  dbt run 
 -- Scan the model repository
 -- create a compaitble sql dialect
 -- pass the dialect to the dataware house

 ## Command  dbt run --full-refresh

 ## to review Catalog and Lineage Graph
 >> dbt docs generate
 >> dbt docs serve  --port 9090

 ## General Configuration

 Alias: name conention
 Tag : tag LOB
 Docs: Costomizing Lineage
 Schema : material  selections

 Adapter Specific Configurations
 - Customing Adapter to match  datawarehouse specification 


 ## Creating List of reuseable source tables in the model Folder
 Cocroack_Soures.yaml
 sometime you might require to do this over agan to make sources reflect
 >>> dbt clean    
          the dbt clean command is used to remove all files and directories that are specified in the clean-targets    configuration  in your dbt_project.yml
 >>> dbt compile
          DBT takes your .sql files from the models/ directory, processes them with any Jinja templates, macros, and configurations, and generates raw SQL statements.
          These compiled SQL files are then stored in the target/compiled/ directory in a structure that mirrors your models/ directory.
 
 ## Documentation
 >>> dbt docs generate 
 >>> dbt docs serve  --port 9090

## Typical Development Workflow for Dim modelling
Create the .yaml file below into model directory for source / target as shown below.
   Source:
      - sources.yaml -> list target tables  
      - Create a all sql sripts
      ->  Materilaize them as View
    Targets:
      star -schema Model
        model_target.yml ->  This is used for the description of tables in the catalog
      
Analyses:
 This are also a model structure, and  but are  not materialize in the datawarehouse, their result lives  analysis folder
 Serve as your validation and code quality check of logic before materializing in the datawarehouse.
 >> dbt compile -s analyses/for_analysis_Customer_1.sql
    ->  get complied in target/analyses
 
Seeds : 
  Are basically a small csv that could be located in the seed folder



## Difference between .dbt/profile.yaml vs dbt_project.yaml
the first .yaml stores all your EDW connections details amd which environment you are operating in 
the second project.yaml stores everything about your various projects profiles, model structure(either as a view or table, and ingestion patttern)

# Model 
 can be  - Views or Table
 it would be a combination
 - SQL
 - Configuration
 where {{ config(materialized='table') }} -> instructing DBT to create a table output in EDW
 Note : Model with configuration with default to a view
 {{ ref('my_first_dbt_model') }} -> referencing the first Model

 # Snaphot 
 Provides a type SCD 2 : Basically if you are creating SCD 2 type of dimension, all configguration details will live in the snaphots folder

 # Test
 Used for asserting certain assumption about your data,
 - singular testing : done by writing a sql query that will return failure if codition is not
 - Generic testing : These are reusable form of test , NOT, UNIQUENESS TEST

# Macros  & JINJA: docs -> https://docs.getdbt.com/docs/build/jinja-macros
 You can call it a functions or piece of code that can be reused througout the entire projects, so you dont, DRY- don't repeat yourselves.
 ->  Fimilization Jinja : it is templating code that helps you ge rid of static code and makes your code more dynamic
# JINJA

    Expressions {{ ... }}: Expressions are used when you want to output a string. You can use expressions to reference variables and call macros.
    Statements {% ... %}:  Statements don't output a string. They are used for control flow, for example, to set up for loops and if statements, to set or modify variables, or to define macros.
    Comments {# ... #}:    Jinja comments are used to prevent the text within the comment from executing or outputing a string.

input
-----
{% set payment_methods = ["bank_transfer", "credit_card", "gift_card"] %}
select
    order_id,
    {% for payment_method in payment_methods %}
    sum(case when payment_method = '{{payment_method}}' then amount end) as {{payment_method}}_amount,
    {% endfor %}
    sum(amount) as total_amount
from app_data.payments
group by 1

Output
-------
select
    order_id,
    sum(case when payment_method = 'bank_transfer' then amount end) as bank_transfer_amount,
    sum(case when payment_method = 'credit_card' then amount end) as credit_card_amount,
    sum(case when payment_method = 'gift_card' then amount end) as gift_card_amount,
    sum(amount) as total_amount
from app_data.payments
group by 1

# MACROS


-Macro files can contain one or more macros — here's an example:

{% macro cents_to_dollars(column_name, scale=2) %}
    ({{ column_name }} / 100)::numeric(16, {{ scale }})
{% endmacro %}

A model which uses this macro might look like:

  select
    id as payment_id,
    {{ cents_to_dollars('amount') }} as amount_usd,
    ...
  from app_data.payments

This would be compiled to:
  select
    id as payment_id,
    (amount / 100)::numeric(16, 2) as amount_usd,
    ...
  from app_data.payments


Using a macro from a package
A number of useful macros have also been grouped together into packages — our most popular package is # dbt-utils.
  select
    field_1,
    field_2,
    field_3,
    field_4,
    field_5,
    count(*)
  from my_table
  {{ dbt_utils.dimensions(5) }}


## Command  dbt run 
 -- Scan the model repository
 -- create a compaitble sql dialect
 -- pass the dialect to the dataware house

 ## to review Catalog and Lineage Graph
 >> dbt docs generate
 >> dbt docs serve  --port 9090

 ## General Configuration

 Alias: name conention
 Tag : tag LOB
 Docs: Costomizing Lineage
 Schema : material  selections

 Adapter Specific Configurations
 - Customing Adapter to match  datawarehouse specification 


 ## Creating List of reuseable source tables in the model Folder
soures.yaml in any of your DW layer
 sometime you might require to do this over agan to make sources reflect
 >>> dbt clean    
          the dbt clean command is used to remove all files and directories that are specified in the clean-targets configuration  in your dbt_project.yml
 >>> dbt compile
          DBT takes your .sql files from the ~ models/ directory ~, processes them with any Jinja templates, macros, and configurations, and generates raw SQL statements.
          These compiled SQL files are then stored in the  ~ target/compiled/ ~ directory in a structure that mirrors your models/ directory.
 
 ## Documentation
 >> dbt docs genrate 
 >>> dbt docs serve  --port 9090

## Typical Development Workflow for Dim modelling
Create the .yaml file below into model directory for source / target as shown below.
   Source:
      - sources.yaml -> list target tables  
      - Create a all sql sripts
      ->  Materilaize them as View
    Targets:
      star -schema Model
        model_target.yml ->  This is used for the description of tables in the catalog
      
Analyses:
 This are also a model structure, and  but are  not materialize in the datawarehouse, their result lives  analysis folder
 Serve as your validation and code quality check of logic before materializing in the datawarehouse.
 >> dbt compile -s analyses/for_analysis_Customer_1.sql
    ->  get complied in target/analyses
 
Seeds : 
  Are basically a small csv that could be located in the seed folder


## DEBUGGING DBT

Assume there is an error is your sql, Using your code to test for error directly on the UI , can help resolves issues fasters.
Note whatever is complied in 
  - target/complied is what dbt run a gainst the analytics systems.

## DOING TEST and ASSERTION/ UNIT TESTING
In target transformation, where we want to do the testing
Create  columnar test/ generic test in schema.yml files 
- Or write your singular test in the test folder
- Writing a generic test , you can create a jinja macro in the test folder and apply in the schema.yml
NOTE:
  In the dbt_porject.yml if a test model is defined as show below the all test becomes materialzed in the DB
     tests;
       +store_failures: true
>> dbt test

## PRODUCTION DEPLOYMENT
 >>> dbt debug --target prod
 >>> dbt compile --target prod
 >>  dbt run --target prod


 