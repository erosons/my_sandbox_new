
# The reason for these string format %s passing is to help prevent sql injection.
sqlcommand = 'SELECT * FROM %s;'

sqlcommand_r_s = "select coalesce(max(lastupdated),'1900-01-01') from %s;"


sql_incremental_extract = "select * from test.Orders"
sql_incremental_extract = sql_incremental_extract + \
    " " + "where lastupdated >= %(value2)s;"
