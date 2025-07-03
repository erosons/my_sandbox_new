SELECT *
FROM (
    WITH CustomerOrders AS (
        SELECT 
            c.CUSTOMER_ID,
            c.FIRST_NAME,
            c.LAST_NAME,
            o.ORDER_ID,
            o.ORDER_DATE,
            o.STATUS,
            p.AMOUNT,
            p.PAYMENT_METHOD
        FROM analytics.public.customers AS c
        JOIN analytics.public.orders AS o
            ON c.CUSTOMER_ID = o.CUSTOMER_ID
        JOIN analytics_public.stg_payments AS p
            ON o.ORDER_ID = p.ORDER_ID
    )
    -- This is likely where the next part of the query continues
)
