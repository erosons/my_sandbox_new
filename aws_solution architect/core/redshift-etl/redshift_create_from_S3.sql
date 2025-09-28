Create table Sales.Transaction_History (
  RowID          varchar,
  OrderID       varchar,
  OrderDate    varchar,	
  ShipDate     varchar,
  ShipMode	   varchar,
  CustomerID  varchar,
  CustomerName	 varchar,
  Segment     varchar,
  Country      varchar,
  City              varchar,
  State            varchar,
  PostalCode   varchar,
  Region	     varchar,
  ProductID   varchar,
  Category     varchar,
  SubCategory	varchar,
  ProductName varchar,
  Sales    varchar,	
  Quantity	 varchar,
  Discount varchar,
  Profit     varchar
) ;
Copy Sales.Transaction_History FROM  's3://etlbucket/SampleSuperstore.csv'
iam_role  'arn:aws:iam::033060477027:role/service-role/AmazonRedshift-CommandsAccessRole-20220623T191438'
compupdate off
delimiter ',' timeformat 'MM/DD/YYYYY HH:MI:SS' ;