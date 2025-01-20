INSERT
    overwrite TABLE my_database.my_partitioned_table PARTITION (partition_column <calendar/load date>)
SELECT
    column1,
    column2,...,
    partition_column
FROM
    my_database.my_external_table;


ANALYZE TABLE my_database.my_partitioned_table COMPUTE STATISTICS FOR COLUMNS;

