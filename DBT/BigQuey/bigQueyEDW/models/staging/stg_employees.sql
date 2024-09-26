with stg_employees as (
    select * from {{source('northwind', 'employees')}}
)

select *, current_timestamp() as  ingestion_timestamp  from stg_employees