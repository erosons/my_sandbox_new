## KEY NOTE:
Because the sclabaility and cheap storage, it is alot Better to do al Transformation within Snowflake using -> ELT Model
- Fivetran
- Stitch
- Data Factory

## Warehouses sizes
Warehouse size corresponds to the number of Nodes in virtual warehouse, Each nodes is a compute unit.
X-LARGE -16
LARGE  - 8
MEDIUM - 4
SMALL  - 2
X_SMALL -1

Virtual warehouse can be suspend whe not in use and set to auto resume as soon as when new query are recieved.

## Sniwflake UI
 - SnowSQL CMD Line utility -> https://sfc-repo.snowflakecomputing.com/snowsql/bootstrap/1.3/linux_x86_64/index.html; https://sfc-repo.snowflakecomputing.com/snowsql/bootstrap/1.3/linux_x86_64/snowsql-1.3.2-linux_x86_64.bash
 - webbased Snowflake WebUI

Setup CLI config -> ~/.snowsql/config
[connections.clr5]
accountname = ''
username = ''''
password = ''
dbname = ''
schmaname = ''
warehousename = ''''

## External Tables :
- The decoupling storage from Compute Engine, where you access the data from external storage like s3

## Lake House Architecture:

Datalake layer (Structured and Unstructured Layer) => MetaData layer and Governance => Buisness Intelligence Layer

## SELECT SYSTEM$ALLOWLIST()
Allowing Hostnames

All Snowflake clients (SnowSQL, JDBC driver, ODBC driver, etc.) require permanent access to cloud storage (Amazon S3, Google Cloud Storage, or Microsoft Azure), as well as other web-based hosts, to perform various runtime operations. To ensure access, particularly in a secure/private network (e.g. AWS PrivateLink-enabled network), you must allow the hostnames for the required hosts.

## Configuration:
https://docs.snowflake.com/en/guides-overview-connecting