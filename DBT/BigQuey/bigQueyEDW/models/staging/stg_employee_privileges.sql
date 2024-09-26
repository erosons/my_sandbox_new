with stg_employee_privileges as (
    select * from {{source('northwind', 'employee_privileges')}}
)

select *, current_timestamp() as  ingestion_timestamp  from stg_employee_privileges