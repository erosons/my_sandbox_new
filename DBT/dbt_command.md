# Project Setup & Initialization

  >> dbt init <project_name>
        Initializes a new DBT project in the specified directory.
        Example: dbt init my_project

  >> dbt debug
        Checks your project and environment to ensure everything is set up correctly.
        Useful for troubleshooting configuration issues.

# Building & Running Models

  >> dbt run
        Executes the SQL in your models and materializes them as tables or views in the database.
        Example: dbt run

  >> dbt run --select <model_name>
        Runs a specific model or models. Useful for testing a subset of your project.
        Example: dbt run --select customers

  >> dbt run --models <model_pattern>
        Runs a set of models that match the provided pattern. Can use model names, tags, or folder paths.
        dbt_project/
        │
        ├── models/
        │   ├── marts/
        │   │   ├── orders/
        │   │   │   └── orders.sql
        │   │   ├── customers/
        │   │   │   └── customers.sql
        │   │   ├── products/
        │   │   │   └── products.sql
        │   └── staging/
        │       ├── staging_orders.sql
        │       ├── staging_customers.sql
        │       ├── staging_products.sql
        │
        └── seeds/
            └── lookup_data.csv
        Example: dbt run --models my_folder.*/ dbt run -m my_folder.*
        >> dbt run --models marts.orders.* / dbt run -m marts.orders.*
        >> dbt run --models marts.orders.orders
        >> dbt run --models marts.* --exclude staging.*
        >> dbt run --models marts.orders.orders marts.customers.customers


  >> dbt run --full-refresh ( allows you to switch from materializing a Table Model to just creating a View)
        Forces a full rebuild of incremental models by dropping and recreating the tables.
        Example: dbt run --full-refresh

# Testing & Validating Data

  >> dbt test
        Runs all tests defined in your project to validate data quality.
        Example: dbt test

  >> dbt test --select <model_name>
        Runs tests only on the specified model(s).
        Example: dbt test --select orders

# Documentation

  >> dbt docs generate
        Generates the documentation for your DBT project.
        Example: dbt docs generate

  >> dbt docs serve

    Starts a local web server to browse the documentation generated from your DBT project.
    Example: dbt docs serve

# Debugging & Logs

  >> dbt debug

    Verifies DBT’s connection to your database and validates the configuration.
    Example: dbt debug

  >> dbt logs --latest

    Retrieves the logs from the latest DBT run.
    Example: dbt logs --latest

# Compilation

  >> dbt compile

    Compiles the DBT project into raw SQL files without executing them. Useful for inspecting the generated SQL.
    Example: dbt compile

  >> dbt compile --models <model_name>

    Compiles a specific model.
    Example: dbt compile --models my_model

# Snapshotting

  >> dbt snapshot

  Capturing changes in data over time with respect to SCD
      -> Timestamp strategies (use 1NF and updated_at columns to track changes)
      -> Check Any
  For any changes dbt populates the sbaphot table with changes

# Cleaning

  >> dbt clean

    Removes all DBT-generated files, such as compiled models and run artifacts.
    Example: dbt clean

# Seeds (Loading CSV Files)

  >> dbt seed

    Loads CSV files in the data folder into your database as tables.
    Example: dbt seed

  >> dbt seed --select <seed_file>

    Loads a specific seed file.
    Example: dbt seed --select customers.csv

Versioning & Upgrading

  >> dbt deps

    Downloads and installs the dependencies listed in your packages.yml file.
    Example: dbt deps

  >> dbt run-operation <macro_name>

    Executes a custom macro defined in your project.
    Example: dbt run-operation my_macro

DAG & Lineage

  >> dbt ls

    Lists all models, tests, seeds, and snapshots in your project.
    Example: dbt ls

  >> dbt ls --select <model_name>

    Lists specific models that match a pattern.
    Example: dbt ls --select staging.*

  >> dbt graph

    Generates a directed acyclic graph (DAG) representing the data lineage in your DBT project.
    Example: dbt graph

## Advanced Commands

  >> dbt build

    A combination of dbt run, dbt test, dbt snapshot, and dbt seed in one command.
    Example: dbt build

  >> dbt run --state <path_to_previous_run>

    Allows you to run models based on the state of a previous run (useful for partial runs or state comparison).
    Example: dbt run --state path_to_previous_run
  
  Freshness Check on your source data  
   >> dbt source freshness

Command Summary
Command	Description
dbt init <project_name>	Initialize a new DBT project.
dbt run	Run models and materialize transformations.
dbt test	Run tests to validate data quality.
dbt docs generate	Generate project documentation.
dbt snapshot	Run snapshots to track changes over time.
dbt seed	Load seed files (CSV) into the database.
dbt deps	Install dependencies from packages.yml.
dbt clean	Remove DBT-generated files.
dbt compile	Compile SQL models into raw SQL files without executing.
dbt graph	Generate a DAG for your project’s data lineage.