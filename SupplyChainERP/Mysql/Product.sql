CREATE TABLE Product(
ProductID varchar(200),
Name varchar(200),
SKUID varchar(200),
Price double,
user_id varchar(200),
created_at timestamp,
PRIMARY KEY (ProductID),
FOREIGN KEY (user_id)
REFERENCES users(user_id)
);

