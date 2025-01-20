CREATE DATABASE SqlShackMergeDemo
GO
   
--===================
 --Partition by a specific column  and aggregating by another colums
--===================

SELECT Customercity, 
       AVG(Orderamount) OVER(PARTITION BY Customercity) AS AvgOrderAmount, 
       MIN(OrderAmount) OVER(PARTITION BY Customercity) AS MinOrderAmount, 
       SUM(Orderamount) OVER(PARTITION BY Customercity) TotalOrderAmount
FROM [dbo].[Orders];



--===================
 --We can add required columns in a select statement with the SQL PARTITION 
 --===================

SELECT Customercity, 
       CustomerName, 
       OrderAmount, 
       AVG(Orderamount) OVER(PARTITION BY Customercity) AS AvgOrderAmount, 
       MIN(OrderAmount) OVER(PARTITION BY Customercity) AS MinOrderAmount, 
       SUM(Orderamount) OVER(PARTITION BY Customercity) TotalOrderAmount,
       COUNT(Orderamount) OVER(PARTITION BY Customercity) TotalOrderAmount
FROM [dbo].[Orders];


--===================
 --We can add required columns in a select statement with the SQL PARTITION  WITH ROW_NUMBER()
 --===================

SELECT Customercity, 
       CustomerName, 
       ROW_NUMBER() OVER(PARTITION BY Customercity
       ORDER BY OrderAmount DESC) AS "Row Number", 
       OrderAmount, 
       COUNT(OrderID) OVER(PARTITION BY Customercity) AS CountOfOrders, 
       AVG(Orderamount) OVER(PARTITION BY Customercity) AS AvgOrderAmount, 
       MIN(OrderAmount) OVER(PARTITION BY Customercity) AS MinOrderAmount, 
       SUM(Orderamount) OVER(PARTITION BY Customercity) TotalOrderAmount
FROM [dbo].[Orders];


--===================
 --PARTITION BY clause with Cumulative total value
 --===================

SELECT Customercity, 
       CustomerName, 
       OrderAmount, 
       ROW_NUMBER() OVER(PARTITION BY Customercity ORDER BY OrderAmount DESC) AS "Row Number", 
       CONVERT(VARCHAR(20), SUM(orderamount) OVER(PARTITION BY Customercity ORDER BY OrderAmount DESC ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING), 1) AS CumulativeTotal,

--===================
 --PARTITION Running Total  BY clause with Cumulative total value
 --===================    

SELECT 

      UnitPrice 
      ,SalesOrderDetailID
      ,sum(UnitPrice) over(order by SalesOrderDetailID  asc) as runing_total
      ,SUM(LineTotal) OVER(PARTITION BY SalesOrderID
       ORDER BY LineTotal ASC ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING) AS CumulativeTotal
 FROM [Sales].[SalesOrderDetail]