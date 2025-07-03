## Duplicate Records Check

First we’ll identify duplicate records in a table.

A duplicate records check in SQL can be performed by using the GROUP BY clause along with the HAVING clause. Here’s an example in SQL Server:

SELECT column_1, column_2, ..., column_n, COUNT(*)
FROM table_name
GROUP BY column_1, column_2, ..., column_n
HAVING COUNT(*) > 1;

In this code, the GROUP BY clause groups together records with identical values in the specified columns, and the HAVING clause filters out groups with a count of one, leaving only the duplicates.

## NULL Value Check

Next, let’s ensure that mandatory fields have values rather than NULLs.

A null value check in SQL can be performed by using the IS NULL operator in a WHERE clause. Here’s an example:

SELECT 
  [column1], [column2], ..., [columnN]
FROM 
WHERE [columnX] ISNULL;

This will give you a result set of all the records in the table where the value in column X is NULL. 

## Data Type Check

Now let’s verify that data in each field is of the correct data type.

A data type check in SQL can be performed by using the CASE statement and the IS OF operator. Here’s an example:

SELECT 
  [column1], [column2], ..., [columnN],
  CASE 
    WHEN [columnX] IS OF (DATATYPE1) THEN 'DataType1'
    WHEN [columnX] IS OF (DATATYPE2) THEN 'DataType2'
    ELSE 'Other'
  END AS DataType
FROM 
  [table_name];

This will return all the records in the table, along with a new column, DataType, indicating the data type of the value in columnX. The CASE statement checks the data type of columnX and returns a string value indicating the data type. In this example, DATATYPE1 and DATATYPE2 are placeholders for the actual data types you want to check for, such as INT, VARCHAR, DATE, etc. If the data type of columnX is neither DATATYPE1 nor DATATYPE2, it will be categorized as “Other.”

## Range Check

Here we validate that values in a field fall within a specified range.

A range check in SQL can be performed by using the BETWEEN operator in a WHERE clause. Here’s how:

SELECT 
  [column1], [column2], ..., [columnN]
FROM 
WHERE [columnX] BETWEEN [lower_bound] AND [upper_bound];

This will give you all the records in the table where the value in columnX is between lower_bound and upper_bound. The BETWEEN operator is inclusive, meaning that the result set will include records where the value in columnX is equal to lower_bound or upper_bound.

## Domain Check

A domain check in SQL can be performed by using a subquery in a WHERE clause to check if the value in a column is in a list of valid values, known as a domain. 

Here’s the example query:

SELECT 
  [column1], [column2], ..., [columnN]
FROM 
WHERE [columnX] IN (SELECT [valid_value1], [valid_value2], ..., [valid_valueN] FROM [domain_table]);

This gives you all the records in the table where the value in columnX is in the list of valid values stored in the domain_table.

## Uniqueness Check

This helps to prevent duplicates from being inserted into the database and ensures that each value in the column is unique.

The most common way to perform a uniqueness check in SQL is to use a unique constraint. This is a restriction placed on a column or set of columns that ensures that the values in those columns are unique across all records in the table.

Here’s an example of how to create one:

ALTER TABLE [table_name]
ADD CONSTRAINT [uc_column_name] 
UNIQUE ([column_name]);

This will create a unique constraint uc_column_name on the column_name in the table_name. If you try to insert a record into the table with a value that already exists in the column_name, the database engine will raise an error and reject the insertion.
Format Check

A format check is a way to enforce a particular pattern or format for the values in a particular column, helping to ensure that the data in the column is consistent.

Here’s an example:

ALTER TABLE [table_name]
ADD CONSTRAINT [ck_column_name] 
CHECK ([column_name] LIKE '[A-Z][0-9][0-9]');

This will create a check constraint ck_column_name on the column_name in the table_name. The constraint ensures that the value in column_name starts with an uppercase letter and is followed by two digits. Knowing regex will help you form the constraint.

## Length Check

A length check is a way to enforce a specific length or range of lengths for the values in a particular column.

Here’s an example using a check constraint:

ALTER TABLE [table_name]
ADD CONSTRAINT [ck_column_name] 
CHECK (LEN([column_name]) >= 5 AND LEN([column_name]) <= 10);

This will create a check constraint ck_column_name on the column_name in the table_name. The constraint ensures that the length of the value in column_name is between 5 and 10 characters.

## Completeness Check

Last but not least, a completeness check helps to identify missing or incomplete data and prevent it from affecting your analysis or reports.

There are a few ways to perform a completeness check in SQL:
Use the NULL value

You can check for missing data by looking for NULL values in a particular column.

SELECT [column_name]
FROM [table_name]
WHERE [column_name] IS NULL;

This query returns all the rows where the column_name is NULL.
Use the COUNT function

You can also use the COUNT function to check the completeness of your data.

SELECT COUNT([column_name])
FROM [table_name];

This query returns the number of rows in the table_name. You can compare this count to the expected number of rows to determine if there is any missing data.
Use the GROUP BY clause

You can also use the GROUP BY clause to check for missing data.

SELECT [group_by_column], COUNT([column_name])
FROM [table_name]
GROUP BY [group_by_column];

This query returns the number of rows for each unique value in the group_by_column. You can use this information to determine if there is any missing data for a particular group.


## DBT test CASES