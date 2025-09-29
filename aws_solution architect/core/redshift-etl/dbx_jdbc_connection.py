spark.read.format("redshift") \
  .option("url", "jdbc:redshift://<host>:5439/<db>?ssl=true") \
  .option("user", dbutils.secrets.get("redshift","user")) \
  .option("password", dbutils.secrets.get("redshift","password")) \
  .option("query", "select 1 as ok") \
  .option("tempdir", "s3a://<BUCKET>/tmp") \
  .option("aws_iam_role", "arn:aws:iam::<acct>:role/<RedshiftCopyRole>") \
  .load().show()
