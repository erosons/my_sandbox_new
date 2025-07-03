
with stg_purchase_order_details as (
    select * from {{source('northwind', 'purchase_order_details')}}
)

select *, current_timestamp() as  ingestion_timestamp  from stg_purchase_order_details