USE SqlShackMergeDemo
GO 

MERGE TargetProducts AS Target 
USING SourceProducts AS Source
ON Source.ProductID = Target.ProductID 
WHEN NOT MATCHED BY Target THEN
INSERT (ProductID, ProductName, Price) 
VALUES (Source.ProductID, Source.ProductName, Source.Price) ;