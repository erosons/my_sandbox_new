
--Bulk COpY
COPY INTO EMP FROM @mystage
files = ('emp.csv')
file_format = (format_name ='CSVfileformat')
match_by_column_name = case_sensitive
force = true  --forces the load if snowflake has previous loaded the data



--Azure Bulk CopY
COPY INTO EMP FROM @my_azure_stage
files = ('emp.csv')
file_format = (format_name ='CSVfileformat')
match_by_column_name = case_sensitive
force = true  --forces the load if snowflake has previous loaded the data



--AWS Bulk CopY
COPY INTO EMP FROM @my_azure_stage
files = ('emp.csv')
file_format = (format_name ='CSVfileformat')
match_by_column_name = case_sensitive
force = true  --forces the load if snowflake has previous loaded the data

--Remove  external stage:
DROP stage my_azure_stage;


-- Generating Schema SELECTING a TABLE
SELECT get_ddl('table','emp')

return -> create or replace TABLE EMP (
	EMPNO NUMBER(4,0),
	ENAME VARCHAR(16777216),
	JOB VARCHAR(16777216),
	MGR NUMBER(4,0),
	HIREDATE DATE,
	SAL NUMBER(5,1),
	COMM NUMBER(5,1),
	DEPTNO NUMBER(2,0)
);


