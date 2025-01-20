Create table abc (v, variant)

 {# Session Variables -> Global variables #}

set table_name = 'abc';
unset table_name
SELECT * from identifier($table_name);

{# 
Local variables -> in blocks, stored proc, function in snowflake scripting#}

BEGIN
  -- Declare a string variable
  DECLARE var_name STRING;
  
  -- Assign a value to the variable
  LET var_name := 'Hello Snowflake!';
  
  -- Use the variable (e.g., in a SELECT statement)
  RETURN var_name;
END;

{# Example #}
CREATE OR REPLACE PROCEDURE my_procedure()
RETURNS STRING
LANGUAGE SQL
AS
$$
DECLARE var_value STRING;

BEGIN
  -- Assign a value to the variable
  LET var_value := 'product_name';

  -- Use the variable in a SELECT statement to retrieve some data from a table
  LET var_value := (SELECT product_name FROM products WHERE product_name = :var_value LIMIT 1);

  -- Return the value of the variable after the SELECT query
  RETURN var_value;
END;
$$;


{# Bind variables  -> for parameterized queries w/runtime param values #}
SELECT (:1),(:2) to_timpestamp((?),2)

{# Environment Variables  #}
SET/ Expoert name=value -> $name 

