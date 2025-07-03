use EIMS;

DELIMITER #
CREATE TRIGGER TransactionManager
AFTER INSERT 
ON TransactionStaging
FOR EACH ROW
BEGIN

INSERT INTO transactions
SELECT 
    new.transaction_ID, 
    new.customer_id,
    SUM(new.order_amount) as order_amount,    
    new.order_date,
    new.ship_date,
    new.sales_rep_id,
    new.shipment_id
FROM TransactionStaging
GROUP BY
    new.transaction_ID, 
    new.customer_id,   
    new.order_date,
    new.ship_date,
    new.sales_rep_id,
    new.shipment_id;

INSERT INTO TransactionsDetails VALUES (new.TransctionDetail_ID ,new.Transaction_ID, new.Product_ID ,new.UnitPrice,new.QuantitySold);
DELETE FROM transactionstaging;
    
 END#;