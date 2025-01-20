{# the snapshot will track the and delete operation if the inavlidate is set to true and end the lifecyle of theat records
>> dbt snapshot
#}
{% snapshot scd_raw_listings %}
{{
config(
    target_schema='History',
    unique_key='id',
    strategy='timestamp',
    updated_at='updated_at',
    invalidate_hard_deletes=True  
    )
 }}
select * FROM {{ source('AIRBNB', 'listings') }}
{% endsnapshot %}