 SELECT get_manager('BLAKE')

 CREATE OR REPLACE FUNCTION get_surbordinates(name string)
 returns table(employee string)
 AS
 '
  SELECT employee FROM employee_manager
  where manager = name
 ';

# CALLING UDTF
 SELECT * from table(get_surbordinates('KING'));