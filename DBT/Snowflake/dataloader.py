import snowflake.connector
# pip install snowflake-connector-python


# Create a cursor object
with open(snowflake.connector.connect(
    user='<username>',
    password='<password>',
    account='<account_name>.snowflakecomputing.com',
    warehouse='<warehouse_name>',
    database='<database_name>',
    schema='<schema_name>'
      )
    ) as conn:
    cur = conn.cursor()

    # Execute a query
    cur.execute("SELECT * FROM <table_name>")

    # Fetch the results
    data = cur.fetchall()

    # Print the data
    for row in data:
        print(row)

# # Close the cursor and connection
# cur.close()
# conn.close()
