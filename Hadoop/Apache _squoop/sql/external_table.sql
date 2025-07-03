CREATE EXTERNAL TABLE if not exists my_database.my_external_table (
    column1 datatype1,
    column2 datatype2,
    ...
    partition_column datatypeN
)
STORED AS PARQUET
LOCATION '/user/hadoop/[target_dir]';


Create External table superstore2 (
      RowID int,	OrderID string,	OrderDate date,	ShipDate date,	ShipMode string,	CustomerID string,
      CustomerName string,	Segment string,	Country  string,	City string,	State string,	Postal string,
      Code string,	ProductID string,	Category string,	SubCategory string,	ProductName string,
      Sales float, Quantity int,	Discount float,Profit float, Region string
      )
      row format delimited
      fields terminated by ',';

Loading  data into hive table from a CSV file
=========================================

Load data SQL query => 
Load data local inpath '/home/samson/Downloads/Superstore.csv' into table superstore2
Load data local inpath '/home/samson/Downloads/Superstore.csv'
                       into table superstore_managed