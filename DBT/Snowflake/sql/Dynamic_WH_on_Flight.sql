
-- Step 1: Resume and resize the warehouse
ALTER WAREHOUSE COMPUTE_WH
RESUME IF SUSPENDED;

ALTER WAREHOUSE COMPUTE_WH
SET WAREHOUSE_SIZE = 'SMALL';

-- Step 2: Switch to the relevant schema and set session options
Use Airbnb;
USE SCHEMA DL_NORTHWIND;
ALTER SESSION SET USE_CACHED_RESULT = FALSE;

-- Step 3: Track the start time for monitoring
SET start_time = CURRENT_TIMESTAMP();

-- Step 4: Execute your query

SELECT * FROM DL_NORTHWIND.CUSTOMERS;

-- Step 5: (Optional) Track the end time if needed
SET end_time = CURRENT_TIMESTAMP();

-- Step 6: Return the warehouse to its original size (e.g., SMALL)
ALTER WAREHOUSE COMPUTE_WH
SET WAREHOUSE_SIZE = 'XSMALL';

-- Step 7: Suspend the warehouse (optional, if no longer needed)
ALTER WAREHOUSE COMPUTE_WH
SUSPEND;