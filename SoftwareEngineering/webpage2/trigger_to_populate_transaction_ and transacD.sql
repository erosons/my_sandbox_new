---Trigger1

TRIGGER   - UPDATE transactionsdetails
MYSQL SYNTAX
UPDATE product
  SET QtyOnHand  = QtyOnHand  - NEW.QuantitySold
  WHERE product.Product_ID = NEW.Product_ID


--- Trigger 2
CREATE TRIGGER TransactionManager
AFTER INSERT ON TransactionStaging
FOR EACH ROW
BEGIN

INSERT INTO transaction
AS 
SELECT 
NEW.transaction_ID, 
NEW.customer_id,
SUM(NEW.order_amount) as order_amount,    
NEW.order_date,
NEW.ship_date,
NEW.sales_rep_id,
NEW.shipment_id
GROUP BY
NEW.transaction_ID, 
NEW.customer_id,    
NEW.order_date,
NEW.ship_date,
NEW.sales_rep_id,
NEW.shipment_id ;

INSERT INTO TransactionsDetails  
AS SELECT  NEW.TransctionDetail_ID 
  NEW.Transaction_ID 
  NEW.Product_ID 
  NEW.UnitPrice 
  NEW.QuantitySold
  FROM TransactionStaging ;

DELETE FROM TransactionStaging;


