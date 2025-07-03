Insert into ProductInventory (SKUID,Quantity,user_id)
SELECT distinct SKUID,count(ProductID) as Quantity ,user_id
From Product
group by user_id,SKUID
