
CREATE TABLE Orders(
OrderID varchar(255),
PaymentID int,
user_id varchar(255),
created_at datetime,
modified_at datetime,
ProductName varchar(20),
PRIMARY KEY (OrderID),
FOREIGN KEY (PaymentID)
REFERENCES Payment(PaymentID),
FOREIGN KEY (user_id)
REFERENCES users(user_id)
);
