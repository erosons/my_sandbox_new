## project initiazation 
TypeError: MessageToJson() got an unexpected keyword argument 'including_default_value_fields' -> python -m pip install protobuf==4.25.3No 
sample profile found for sqlserver -> not an error

# Rutime Error  >>> dbt dparse
- Runtime Error
  Could not find profile named 'CockroackEDW'  -> make sure Project Name matches

  # During connection testing with  >>> dbt debug
- Authentication Error -> password , ssl certicate, encryption issues 

## Runtime Error     
  Credentials in profile "CockroackEDW", target "dev_sqlserver" invalid: Runtime Error
    Could not find adapter type sqlserver!  -> Missing Adapater

## 15:47:41  Unhandled error while executing target/run/CockroackEDW/models/example/customer_categorization.sql
('42S02', "[42S02] [Microsoft][ODBC Driver 18 for SQL Server][SQL Server]Invalid object name 'Sales.Customer'. (208) (SQLMoreResults)")
--> Schema error

##  Unable to do partial parsing because saved manifest not found. Starting full parse.