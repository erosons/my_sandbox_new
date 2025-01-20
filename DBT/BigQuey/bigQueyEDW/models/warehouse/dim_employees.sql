with  
source as (
    select distinct
    id as employee_id
    ,company
    ,last_name
    ,first_name
    ,email_address
    ,job_title
    ,business_phone
    ,home_phone
    ,mobile_phone
    ,fax_number
    ,address
    ,city
    ,state_province
    ,zip_postal_code
    ,country_region
    ,web_page
    ,notes
    ,attachments
    ,current_timestamp() as insertion_timestamp
from {{ ref('stg_employees') }}
),
unique_source as (
   select *, row_number() over(PARTITION BY employee_id) as rnk 
   from source
)

select * 
except (rnk),
from unique_source
where rnk =1 