{# Clone a table , will create a table of similiar sturture but data is not copied #}


Create table dept_like  like dept   
insert overwrite into dept_like select * from dept --truncate table before loading

SELECT * FROM dept_like

-- CTAS Operations
CREATE TABLE dept_ctas
 as 
SELECT * FROM dept

{# CLONE A TABLE #}
--... (zero-copy cloning)
CREATE TABLE dept_cloned clone dept_like --This references and creates a branch of table if does not create table and use storage space
SELECT * FROM dept_cloned

insert into dept_like values (50, 'MAILROOM', 'ATLANTA');
select * from dept_like;
select * from dept_cloned;

insert into dept_cloned values (60, 'DEVELOPMENT', 'CHICAGO');
select * from dept_cloned;
select * from dept_like;


-- multi-table insert (no PK enforced!)
insert first
  when deptno <= 20
  then into dept_like
  else into dept_cloned
select * from dept;


-- update all rows from dept_ctas (always use WHERE!)
update dept_like
  set dname = 'deleted'
  from dept
  where dept_like.deptno = dept.deptno;
  
select * from dept_like;