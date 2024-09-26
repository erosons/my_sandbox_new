with stg_inventory_transaction_types as (
    select * from {{source('northwind', 'inventory_transaction_types')}}
)

select *, current_timestamp() as  ingestion_timestamp  from stg_inventory_transaction_types