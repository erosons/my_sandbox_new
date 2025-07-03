{# Types of Stages in Snowflake:

    User Stages: Each user has a personal stage associated with their account.
    Table Stages: Every table has its own dedicated stage.
    Named Internal Stages: Explicitly created and named by users, which can be shared across multiple operations.

Key Use Cases for Internal Stages:

    Staging data before loading it into a Snowflake table (e.g., for ETL processes).
    Exporting data from Snowflake to files for external use or further processing.
    Data backup and restoration. #}

-- Named Internal Stages
Create stage if not exists mystage;

--REMOTE PUT a file in name stage with CLI command
PUT '/home/samson/Downloads/SampleSuperstore(in).csv' @mystage;

--List file in a named Stage
list @mystage

--Load the data from the internal stage into a table:
COPY INTO my_table
FROM @my_stage
FILE_FORMAT = (TYPE = 'CSV');

--Remove a file from the stage:
REMOVE @my_stage/my_data.csv;

--Remove  internal stage:
DROP stage mystage;

-- Query Internal table After Upload

SELECT metadata$file_row_number, $1,$2
from @mystage/SampleSuperstore.csv;

-- file_format definition in stage which can is resuable
CREATE file format CSVfileformat
    type ='csv',
    header = true;

SELECT * 
FROM TABLE(
    infer_schema(
        location => '@mystage',
        files => 'SampleSuperstore.csv',
        file_format => CSVfileformat
    )
);

--Construct a table from Schema file 

Create table emp using template(
    Select array_agg(
        object_construct(*)
    )
    FROM TABLE(
    infer_schema(
        location => '@mystage',
        files => 'emp.csv',
        file_format => 'CSVfileformat'
     ) )
) 
 {# => the inner function returns an array of array_agg #}

[
  {
    "COLUMN_NAME": "EMPNO",
    "EXPRESSION": "$1::NUMBER(4, 0)",
    "FILENAMES": "emp.csv",
    "NULLABLE": true,
    "ORDER_ID": 0,
    "TYPE": "NUMBER(4, 0)"
  },
  {
    "COLUMN_NAME": "ENAME",
    "EXPRESSION": "$2::TEXT",
    "FILENAMES": "emp.csv",
    "NULLABLE": true,
    "ORDER_ID": 1,
    "TYPE": "TEXT"
  },
  {
    "COLUMN_NAME": "JOB",
    "EXPRESSION": "$3::TEXT",
    "FILENAMES": "emp.csv",
    "NULLABLE": true,
    "ORDER_ID": 2,
    "TYPE": "TEXT"
  },
  {
    "COLUMN_NAME": "MGR",
    "EXPRESSION": "$4::NUMBER(4, 0)",
    "FILENAMES": "emp.csv",
    "NULLABLE": true,
    "ORDER_ID": 3,
    "TYPE": "NUMBER(4, 0)"
  },
  {
    "COLUMN_NAME": "HIREDATE",
    "EXPRESSION": "$5::DATE",
    "FILENAMES": "emp.csv",
    "NULLABLE": true,
    "ORDER_ID": 4,
    "TYPE": "DATE"
  },
  {
    "COLUMN_NAME": "SAL",
    "EXPRESSION": "$6::NUMBER(5, 1)",
    "FILENAMES": "emp.csv",
    "NULLABLE": true,
    "ORDER_ID": 5,
    "TYPE": "NUMBER(5, 1)"
  },
  {
    "COLUMN_NAME": "COMM",
    "EXPRESSION": "$7::NUMBER(5, 1)",
    "FILENAMES": "emp.csv",
    "NULLABLE": true,
    "ORDER_ID": 6,
    "TYPE": "NUMBER(5, 1)"
  },
  {
    "COLUMN_NAME": "DEPTNO",
    "EXPRESSION": "$8::NUMBER(2, 0)",
    "FILENAMES": "emp.csv",
    "NULLABLE": true,
    "ORDER_ID": 7,
    "TYPE": "NUMBER(2, 0)"
  }
]