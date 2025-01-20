{{ config(materialized='view')}}

SELECT  *
FROM {{source('Cockroack',"Customers_DB_2")}}  
---  The source function here references the sources schema pulled from  
--- Cockroack' -> CockroackEDW.dbo