with stg_orders as (
    select * from {{source('northwind', 'orders')}}
)

select *, current_timestamp() as  ingestion_timestamp  from stg_orders