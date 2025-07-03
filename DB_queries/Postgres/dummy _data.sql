Create table employee (
id  integer not null,
name varchar(150),
salary integer,
Constraint emp_pk primary key(id));

WITH
SALARY_LIST 
as (
	SELECT '{1000,2000,5000,150000,200000,250000}'::int[] as salary
	)
insert into employee (id, name , salary)
select n, 'Employee'||n as name, 
salary[1+mod(n,array_length(salary,1))]
from SALARY_LIST ,generate_series(1, 100000000) as n