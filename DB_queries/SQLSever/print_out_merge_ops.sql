USE SqlShackMergeDemo
GO
    
MERGE TargetProducts AS Target
USING SourceProducts	AS Source
ON Source.ProductID = Target.ProductID
    
-- For Inserts
WHEN NOT MATCHED BY Target THEN
    INSERT (ProductID,ProductName, Price) 
    VALUES (Source.ProductID,Source.ProductName, Source.Price)
    
-- For Updates
WHEN MATCHED THEN UPDATE SET
    Target.ProductName	= Source.ProductName,
    Target.Price		= Source.Price
    
-- For Deletes
WHEN NOT MATCHED BY Source THEN
    DELETE
        
-- Checking the actions by MERGE statement
OUTPUT $action, 
DELETED.ProductID AS TargetProductID, 
DELETED.ProductName AS TargetProductName, 
DELETED.Price AS TargetPrice, 
INSERTED.ProductID AS SourceProductID, 
INSERTED.ProductName AS SourceProductName, 
INSERTED.Price AS SourcePrice;