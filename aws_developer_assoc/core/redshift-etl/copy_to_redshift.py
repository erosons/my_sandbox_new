

if redshift_connection is None:
    print('Error establishing connecting to the MySQL databasse')
else:
    print(f'connection {redshift_connection} established')

# run the  Copy commad to load the file into Redshift


S3_URI = ("s3://" + bucketname + "/order_extract.csv")
role_string = ("arn:aws:iam::" + account_id + ":role/" + iam_role)


"""
SQl query for copying from S3 into DW
"""

sql = "COPY my_schema.my_table"
sql = sql + " FROM %s "
sql = sql + " iam_role %s"
sql = sql + "delimiter ',';"


# create a cursor object and execute the COPY

r_s = redshift_connection.cursor()
r_s.execute(sql, (S3_URI, role_string))

# Close the cursor and commit the transaction
r_s.close()
redshift_connection.commit()

# Close connection
# redshift_connection.close()
