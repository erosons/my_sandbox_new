with source as (
      select * from {{ source('northwind', 'strings') }}
),
renamed as (
    select
        {{ adapter.quote("string_id") }},
        {{ adapter.quote("string_data") }}

    from source
)
select * from renamed
  