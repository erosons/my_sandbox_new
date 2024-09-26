with stg_sales_reports as (
    select * from {{source('northwind', 'sales_reports')}}
)

select *, current_timestamp() as  ingestion_timestamp  from stg_sales_reports