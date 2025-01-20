

{{ config(materialized='table') }}

SELECT s."TerritoryID",s."SalesQuota",s."Bonus",s."CommissionPct",s."SalesYTD",t."CostYTD",t."CostLastYear"
 FROM "dbo"."SalesPerson" as s
 JOIN "dbo"."SalesTerritory" as t  on t."TerritoryID" =s."TerritoryID"
