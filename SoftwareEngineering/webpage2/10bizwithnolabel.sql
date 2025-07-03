Use EIMS;


DROP VIEW IF EXISTS  productBycategories;
CREATE OR REPLACE VIEW  productBycategories

AS

Select 
c.catergory_name, count(*) as ProductCount
from category c
inner join product p
on c.category_id = p.category_id
group by c.catergory_name;



DROP VIEW IF EXISTS  productSoldBycategories;
CREATE OR REPLACE VIEW productSoldBycategories

AS

Select 
product_name, count(*) as ProductCount
from transactionsdetails t
join product p
on t.Product_ID = p.product_id
join category c
on c.category_id =p.category_id
group by c.catergory_name;


DROP VIEW IF EXISTS  Inventorybalance;
CREATE OR REPLACE VIEW Inventorybalance

AS
    Select x.product_name,
    x.TotalQuantitySold,
    (p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
    from (
    Select 
    p.product_id, p.product_name,
    sum(QuantitySold) as TotalQuantitySold
    from transactionsdetails t
    join product p  on p.product_id =t.Product_ID
    where p.product_name='workout du'
    group by p.product_id, p.product_name
        ) x 
    Join product p on p.product_id =x.Product_ID
    
    UNION ALL
    
    Select 
    x.product_name,
    x.TotalQuantitySold,
    (p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
    from (
    Select 
    p.product_id, p.product_name,
    sum(QuantitySold) as TotalQuantitySold
    from transactionsdetails t
    join product p  on p.product_id =t.Product_ID
    where p.product_name='Football'
    group by p.product_id, p.product_name
        ) x 
    Join product p on p.product_id =x.Product_ID
    
   UNION ALL
    
    Select 
    x.product_name,
    x.TotalQuantitySold,
    (p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
    from (
    Select 
    p.product_id, p.product_name,
    sum(QuantitySold) as TotalQuantitySold
    from transactionsdetails t
    join product p  on p.product_id =t.Product_ID
    where p.product_name='Apple AirP'
    group by p.product_id, p.product_name
        ) x 
    Join product p on p.product_id =x.Product_ID
 
 UNION ALL
    
    Select 
    x.product_name,
    x.TotalQuantitySold,
    (p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
    from (
    Select 
    p.product_id, p.product_name,
    sum(QuantitySold) as TotalQuantitySold
    from transactionsdetails t
    join product p  on p.product_id =t.Product_ID
    where p.product_name='Trash Can'
    group by p.product_id, p.product_name
        ) x 
    Join product p on p.product_id =x.Product_ID
    
  UNION ALL
    
    Select x.product_name,
    x.TotalQuantitySold,
    (p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
    from (
    Select 
    p.product_id, p.product_name,
    sum(QuantitySold) as TotalQuantitySold
    from transactionsdetails t
    join product p  on p.product_id =t.Product_ID
    where p.product_name='INSTA POT'
    group by p.product_id, p.product_name
        ) x 
    Join product p on p.product_id =x.Product_ID
    
    UNION ALL
    
    Select
    x.product_name,
    x.TotalQuantitySold,
    (p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
    from (
    Select 
    p.product_id, p.product_name,
    sum(QuantitySold) as TotalQuantitySold
    from transactionsdetails t
    join product p  on p.product_id =t.Product_ID
    where p.product_name='Humidifier'
    group by p.product_id, p.product_name
        ) x 
    Join product p on p.product_id =x.Product_ID
    
    UNION ALL
    
    Select 
    x.product_name,
    x.TotalQuantitySold,
    (p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
    from (
    Select 
    p.product_id, p.product_name,
    sum(QuantitySold) as TotalQuantitySold
    from transactionsdetails t
    join product p  on p.product_id =t.Product_ID
    where p.product_name='Blockout C'
    group by p.product_id, p.product_name
        ) x 
    Join product p on p.product_id =x.Product_ID
    
    UNION ALL
    
    Select 
    x.product_name,
    x.TotalQuantitySold,
    (p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
    from (
    Select 
    p.product_id, p.product_name,
    sum(QuantitySold) as TotalQuantitySold
    from transactionsdetails t
    join product p  on p.product_id =t.Product_ID
    where p.product_name='Mens Watch'
    group by p.product_id, p.product_name
        ) x 
    Join product p on p.product_id =x.Product_ID
    
    UNION ALL
    
    Select
    x.product_name,
    x.TotalQuantitySold,
    (p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
    from (
    Select 
    p.product_id, p.product_name,
    sum(QuantitySold) as TotalQuantitySold
    from transactionsdetails t
    join product p  on p.product_id =t.Product_ID
    where p.product_name='Womans Wat'
    group by p.product_id, p.product_name
        ) x 
    Join product p on p.product_id =x.Product_ID
    
    UNION ALL
    
    Select 
    x.product_name,
    x.TotalQuantitySold,
    (p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
    from (
    Select 
    p.product_id, p.product_name,
    sum(QuantitySold) as TotalQuantitySold
    from transactionsdetails t
    join product p  on p.product_id =t.Product_ID
    where p.product_name='Pot Set'
    group by p.product_id, p.product_name
        ) x 
    Join product p on p.product_id =x.Product_ID;


use EIMS;

  Select * from LowStock;



use EIMS;

DROP VIEW IF EXISTS  CustomerMin_Max;
CREATE OR REPLACE VIEW CustomerMin_Max
AS

with minimumPurchased 
as (
    Select * from
    (
    Select c.customer_id,c.first_name, t.order_amount as minimumAmount_purchased,
    dense_rank() over(PARTITION by customer_id order by t.order_date asc) rnk
    from
    transactions t
    join customer c on t.customer_id =c.customer_id
        ) x
   where x.rnk =1
    
    ),

maximumPurchased 
as (
    Select * from
    (
    Select c.customer_id,c.first_name, t.order_amount as MaximumAmount_purchased,
    dense_rank() over(PARTITION by customer_id order by t.order_date desc) rnk
    from
    transactions t
    join customer c on t.customer_id =c.customer_id
        ) x
   where x.rnk =1
    
    )
    
   Select mi.first_name,
   mx.MaximumAmount_purchased,
   mi.minimumAmount_purchased
   from minimumPurchased mi
   join maximumPurchased mx on  mi.customer_id = mx.customer_id;



DROP VIEW IF EXISTS  Toptenproducts;
CREATE OR REPLACE VIEW Toptenproducts
AS
SELECT p.product_name,t.order_amount FROM 
transactions t
join transactionsdetails td on t.transaction_ID = td.Transaction_ID
join product p on p.product_id =td.Product_ID
order by t.order_amount desc
limit 5;


DROP VIEW IF EXISTS  bottom5products;
CREATE OR REPLACE VIEW bottom5products
AS
SELECT p.product_name,t.order_amount FROM 
transactions t
join transactionsdetails td on t.transaction_ID = td.Transaction_ID
join product p on p.product_id =td.Product_ID
order by t.order_amount asc
limit 5;



DROP VIEW IF EXISTS  customerSegmentationBygender;
CREATE OR REPLACE VIEW customerSegmentationBygender
AS
SELECT gender, count(*) as genderCount
FROM
customer
group by gender;


DROP VIEW IF EXISTS  customersRecency;
CREATE OR REPLACE VIEW customersRecency
AS

SELECT 
x.first_name ,
x.date_last_Visited
from
(
SELECT first_name, t.order_date as date_last_Visited,
dense_rank() over(partition by c.customer_id order by t.order_date desc) as rnk
FROM
customer c
join transactions t on t.customer_id =c.customer_id
 ) x
 where x.rnk =1;


DROP VIEW IF EXISTS  productBystate;
CREATE OR REPLACE VIEW productBystate
AS
Select a.state, 
t.order_amount
from customer c
join address a on a.address_id =c.address_id
join transactions t on c.customer_id =t.customer_id
order by t.order_amount desc;