CREATE OR REPLACE PROCEDURE find_manager(name STRING)
  RETURNS STRING
  LANGUAGE PYTHON
  RUNTIME_VERSION = '3.8'
  HANDLER = 'find_manager'
  PACKAGES = ('snowflake-snowpark-python')
AS
$$
import snowflake.snowpark as snowpark

def find_manager(session, name):
    # Embed the parameter directly in the SQL query using formatted strings
    query = f"SELECT manager FROM employee_manager WHERE employee = '{name}'"
    
    # Execute the query
    result = session.sql(query).collect()
    
    # If result is found, return the manager name, else return None
    return result[0]['MANAGER'] if result else None
$$;


call find_manager('BLAKE')


{# Find enployee given a manager #}

CREATE OR REPLACE PROCEDURE find_manager(name STRING)
  RETURNS TABLE(employee string)
  LANGUAGE PYTHON
  RUNTIME_VERSION = '3.8'
  HANDLER = 'find_manager'
  PACKAGES = ('snowflake-snowpark-python')
AS
$$
import snowflake.snowpark as snowpark

def find_manager(session, name):
    # Embed the parameter directly in the SQL query using formatted strings
    query = f"SELECT employee FROM employee_manager WHERE manager = '{name}'"
    
    # Execute the query
    result = session.sql(query)
    
    # If result is found, return the manager name, else return None
    return result
$$;


{# -- STORED PROC RETURNING A TABLE #}

CREATE OR REPLACE PROCEDURE find_employee(name STRING)
  RETURNS TABLE(employee STRING)
  LANGUAGE PYTHON
  RUNTIME_VERSION = '3.8'
  HANDLER = 'find_manager'
  PACKAGES = ('snowflake-snowpark-python')
AS
$$
import snowflake.snowpark as snowpark

def find_manager(session, name):
    # Create the SQL query using formatted strings
    query = f"SELECT employee FROM employee_manager WHERE manager = '{name}'"
    
    # Execute the query and return the result as a DataFrame
    result = session.sql(query)
    
    # Return the result directly (as a DataFrame, which will be returned as a table)
    return result
$$;
