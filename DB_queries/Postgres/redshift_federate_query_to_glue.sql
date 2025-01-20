---================
--REDSHIFT SPECTRUM
--=================

CREATE EXTERNAL SCHEMA IF NOT EXISTS S3input
FROM DATA CATALOG DATABASE 'redshiftbucket'
IAM_ROLE 'arn:aws:iam' --With read acess to s3 and glue acess to datacatalog


Select count(*) FROM s3input.people_csv;


CREATE VIEW AS TRANSACTION_REVIEWS

AS 

SELECT * FROM s3input.people_csv
WITH NO SCHEMA BINDING;