{# TO FULLY TRANSFORM Array Object We Latten RETURNS => rows of flatten json that indexable #}

SELECT * 
FROM json_holder ,
Lateral flatten(input => json_holder.v,path =>'data') d


{# TRANSORM TO TABULAR FORMAT by Indexing the Json#}

SELECT d.value:DEPTNO,d.value:DNAME,d.value:LOC
FROM json_holder ,
Lateral flatten(input => json_holder.v,path =>'data') d

{# CAST to right Data Type #}

SELECT 
 d.value:DEPTNO::number(2,0) as DEPTNO,
 d.value:DNAME::VARCHAR(20) as DNAME,
 d.value:LOC::VARCHAR(20) as   LOC,
FROM json_holder ,
Lateral flatten(input => json_holder.v,path =>'data') d

-- another version 

SELECT 
 d.value:DEPTNO::number(2,0) as DEPTNO,
 d.value:DNAME::VARCHAR(20) as DNAME,
 d.value:LOC::VARCHAR(20) as   LOC,
FROM json_holder ,
Table(flatten(input => json_holder.v,path =>'data')) d



{# Performance Considerations of LATERAL vs TABLE()
1. LATERAL FLATTEN() (More Memory Efficient, Potentially Slower):

    Memory Efficiency:
        When you use LATERAL, Snowflake processes the FLATTEN() function on a per-row basis. This means the function works on each individual row’s JSON object and produces the output for that row before moving to the next row.
        This approach typically requires less memory because the function is working with smaller, row-level chunks of data at a time rather than operating on the entire dataset at once. Only a portion of the dataset is in memory at any given time, which leads to better memory management.
    Performance (Speed):
        While LATERAL is more memory-friendly, it can be slower because Snowflake must re-evaluate the FLATTEN() function for each row. This per-row evaluation incurs more overhead as the operation needs to be repeated multiple times (once for each row).
        In large datasets, the repeated processing of the function could lead to increased execution time, especially if the number of rows is large and each row contains complex JSON structures.

2. TABLE(FLATTEN()) (Potentially Faster, Higher Memory Usage):

    Memory Usage:
        In the case of TABLE(FLATTEN()), Snowflake applies the FLATTEN() function on the entire dataset or column (json_holder.v) without correlating it to individual rows. This means the function processes the entire set of JSON data at once, which could lead to higher memory consumption, as more data needs to be loaded into memory at a given time.
        Since the FLATTEN() operation is done in one pass across the entire dataset, the entire dataset (or a significant portion of it) could be stored in memory during the process, consuming more memory resources.

    Performance (Speed):
        The potential benefit of TABLE(FLATTEN()) is that it may be faster since the function doesn't need to be re-evaluated for each row. Instead, it processes the entire dataset in one go, leveraging optimizations like bulk processing.
        This approach can be faster in scenarios where you are dealing with simple data and don’t need per-row operations. However, it comes at the cost of higher memory usage. #}