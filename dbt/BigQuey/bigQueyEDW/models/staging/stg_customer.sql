with stg_customer as (
    select * from {{source('northwind', 'customer')}}
)

select *, current_timestamp() as  ingestion_timestamp  from stg_customer