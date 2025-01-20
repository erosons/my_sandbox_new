CREATE OR REPLACE FUNCTION get_manager(name string)
 returns string
 AS
 $$
 SELECT MANAGER
 FROM employee_manager
 Where employee = name
 $$;

SELECT get_manager('BLAKE')