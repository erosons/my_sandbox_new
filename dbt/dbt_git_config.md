## Git tracking

ignore
- dbt-env folder
- log folder

## Config

### materialization (tables or views)
{{ config(materialized='table') }}
OR
{{ config(materialized='views') }}

### data partitioning (tables or views)
{{ config(
    partition_by={
      "field": "creation_date",
      "data_type": "date"
    }
)}}
