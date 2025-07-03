with stg_string as (
    select * from {{source('northwind', 'strings')}}
)

select *, current_timestamp() as  ingestion_timestamp  from stg_string