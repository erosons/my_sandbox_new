with stg_inventory_transactions as (
    select * from {{source('northwind', 'inventory_transactions')}}
)

select *, current_timestamp() as  ingestion_timestamp  from stg_inventory_transactions