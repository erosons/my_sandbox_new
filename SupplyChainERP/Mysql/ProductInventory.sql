CREATE TABLE ProductInventory(
SKUID varchar(200),
Quantity int ,
created_at timestamp,
PRIMARY KEY (SKUID),
FOREIGN KEY (ProductID)
REFERENCES users(ProductID)
);
