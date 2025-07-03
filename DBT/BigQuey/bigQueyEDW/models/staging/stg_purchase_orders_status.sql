with stg_purchase_orders_status as (
    select * from {{source('northwind', 'purchase_order_status')}}
)

select *, current_timestamp() as  ingestion_timestamp  from stg_purchase_orders_status