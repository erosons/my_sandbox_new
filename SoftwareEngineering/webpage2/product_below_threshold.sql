SET @workout_dumbell =5;
SET @Football = 2;
SET @Apple = 15;
SET @Trash = 2;
SET @INSTA = 10;
SET @Humidifier =5;
SET @Blockout = 7;
SET @Mens_Watch= 2;
SET @Womans=15;
SET @Pot=10;

 Select y.* 
  FROM
   (
    Select x.*,(p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
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
   ) y
where Inventory_Balance < @workout_dumbell 


    UNION ALL
 Select y.* 
  FROM
   (    
    Select x.*,(p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
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
    ) y
where Inventory_Balance < @Football
    
   UNION ALL
  Select y.* 
  FROM
   (   
    Select x.*,(p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
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
    ) y
where Inventory_Balance < @Apple
 
 UNION ALL
  Select y.* 
  FROM
   (   
    Select x.*,(p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
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
    ) y
where Inventory_Balance < @Trash

  UNION ALL
  Select y.* 
  FROM
   (   
    Select x.*,(p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
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
      ) y
where Inventory_Balance < @INSTA
    
    UNION ALL
  Select y.* 
  FROM
   (   
    Select x.*,(p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
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
      ) y
where Inventory_Balance < @Humidifier
    
    UNION ALL
  Select y.* 
  FROM
   (   
    Select x.*,(p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
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
     ) y
where Inventory_Balance < @Blockout
    
    UNION ALL
 Select y.* 
  FROM
   (    
    Select x.*,(p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
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
      ) y
where Inventory_Balance <  @Mens_Watch
    
    UNION ALL
 Select y.* 
  FROM
   (    
    Select x.*,(p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
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
      ) y
where Inventory_Balance < @Womans
    
    UNION ALL
  Select y.* 
  FROM
   (   
    Select x.*,(p.QtyOnHand-TotalQuantitySold) as Inventory_Balance
    from (
    Select 
    p.product_id, p.product_name,
    sum(QuantitySold) as TotalQuantitySold
    from transactionsdetails t
    join product p  on p.product_id =t.Product_ID
    where p.product_name='Pot Set'
    group by p.product_id, p.product_name
        ) x 
    Join product p on p.product_id =x.Product_ID
     ) y
where Inventory_Balance < @Pot
