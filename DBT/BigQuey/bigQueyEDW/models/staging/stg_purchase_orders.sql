with stg_purchase_orders as (
    select * from {{source('northwind', 'purchase_orders')}}
)

select *, current_timestamp() as  ingestion_timestamp  from stg_purchase_orders