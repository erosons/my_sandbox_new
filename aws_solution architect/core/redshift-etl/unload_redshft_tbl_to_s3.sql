UNLOAD ('SELECT * FROM sales')
TO 's3://redshift-stagingarea/users'
CREDENTIALS 'aws_iam_role=<ARN ROlE>'