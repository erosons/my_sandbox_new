
{{ config(materialized='table') }}

SELECT  *
FROM {{ref("Customer_2")}}  
---  The source function here references the sources schema pulled from  
--- Cockroack' -> CockroackEDW.dbo