-- JavaScript stored procedure
create or replace procedure find_manager(name string)
  returns string
  language javascript
as $$
  var query = "select manager from employee_manager where employee = ?";
  var stmt = snowflake.createStatement({sqlText: query, binds: [NAME]});
  var res = stmt.execute();
  return res.next() ? res.getColumnValue(1) : null;
$$;

call find_manager('BLAKE');
call find_manager('nobody');
-- select * from table(result_scan(last_query_id()));