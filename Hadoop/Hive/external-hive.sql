Create External table superstore2 (
      RowID int,OrderID string,	OrderDate date,	ShipDate date,	ShipMode string,	CustomerID string,
      CustomerName string,	Segment string,	Country  string,	City string,	State string,	Postal string,
      Code string,	ProductID string,	Category string,	SubCategory string,	ProductName string,
      Sales float, Quantity int,	Discount float,Profit float, Region string
      )
      row format delimited
      fields terminated by ',';