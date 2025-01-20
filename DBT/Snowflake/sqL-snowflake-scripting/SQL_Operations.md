DDL 
 - CREATE (like , CATS,clone)
 - ALTER
 - DROP
 - SHOW|DESC -> metadata review
 - COMMENT|USE

DML
 - INSERT|UPDATE
 # INSERT
  - Conditional Mutiple-table insert
    -- multi-table insert (no PK enforced!)
        insert first
            when deptno <= 20
            then into dept_like
            else into dept_cloned
        select * from dept;
 # INSERT overwrite
     -- Will truncate your table and insert new records
 - DELETE|TRUNCATE(does maiantain metadata)
 - MERGE|EXPLAIN

 DQL
  - SELECT|CALL

TRANSACTION
  BEGIN TRANSACTION
  COMMIT|ROLLBACK
  DESCRIBE TRANSACTION
  SHOW TRANSACTION |LOCKS

DCL -> DATA CONTROL LANGUAGE
 - USER|ROLE
 - GRANT|REVOKE
