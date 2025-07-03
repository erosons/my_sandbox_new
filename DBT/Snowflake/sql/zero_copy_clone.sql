# Clone Table:
# You can create a clone of a table or database as it existed in the past. 
# This does not duplicate data but instead references the original data, which helps save storage

CREATE OR REPLACE TABLE my_table_clone 
CLONE my_table 
AT (TIMESTAMP => '2024-10-01 10:00:00');