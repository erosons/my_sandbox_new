{{ config(severity= 'error') }}

SELECT inventory_id, sum(quantity) as total_sum
FROM `inner-arch-277522.dbt_northwind_dwh_northwind.fact_inventory`
GROUP BY inventory_id
having total_sum=0