{# In Snowflake, Time Travel is a feature that allows you to access historical 
data (e.g., tables, schemas, or databases) at any point within a configurable 
retention period. This means you can query, restore, or even clone data as it 
existed at a specific point in the past. Time Travel is particularly useful for recovering data 
that has been accidentally modified or deleted, or for auditing purposes. #}

{# CREATE A TABLE OF DATABASE WITH TIME TRAVEL #}
CREATE DATABASE my_database
DATA_RETENTION_TIME_IN_DAYS = 15;

{# OR #}

CREATE TABLE my_table (
  id INT,
  name STRING,
  created_at TIMESTAMP
)
DATA_RETENTION_TIME_IN_DAYS = 15;


{# Restore a Table to a Previous State
If a table was accidentally modified or deleted, you can restore it to a previous state using  #}
ALTER TABLE my_table 
RESTORE AT (TIMESTAMP => '2024-10-01 10:00:00');

SELECT * 
FROM my_table 
AT (TIMESTAMP => '2024-10-01 10:00:00');

SELECT * 
FROM my_table 
AT (OFFSET => -INTERVAL '5 minutes');

SELECT * 
FROM my_table 
AT (STATEMENT => 'query_id');




