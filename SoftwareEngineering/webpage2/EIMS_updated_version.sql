DROP DATABASE IF EXISTS EIMS;
CREATE DATABASE IF NOT EXISTS EIMS ;
/* DATETIME of SQL Server will be used as DATE data type of the standard SQL */
USE EIMS ;


CREATE TABLE address (
address_id  VARCHAR(50) NOT NULL,
street      VARCHAR(50) NOT NULL,
city        VARCHAR(30)NOT NULL,
state       VARCHAR(30) NOT NULL,
zip_code    VARCHAR(20) NOT NULL,
country     VARCHAR(10) NOT NULL,
CONSTRAINT address_idpk PRIMARY KEY (address_id)
);

CREATE TABLE customer (
customer_id     VARCHAR(8) NOT NULL,
first_name      VARCHAR(20) NOT NULL,
last_name       VARCHAR(20) NOT NULL,
email           VARCHAR (50)NOT NULL,
marital_status  VARCHAR( 3)NOT NULL,
gender          CHAR(1) NOT NULL,
DOB             DATE NOT NULL,
address_id      VARCHAR(20) NOT NULL,
Staff           CHAR(1),
CONSTRAINT customer_idPK PRIMARY KEY (customer_id),
FOREIGN KEY (address_id)  REFERENCES address(address_id)
);


CREATE TABLE shipment (
shipment_id     VARCHAR(20)NOT NULL,
order_id        VARCHAR(20)NOT NULL,
shipment_date   DATE NOT NULL,
CONSTRAINT shipment_id PRIMARY KEY (shipment_id)
-- CONSTRAINT order_id FOREIGN KEY (order_id) REFERENCES  Transactions (order_id)
);

CREATE TABLE  Transactions (
transaction_ID  VARCHAR(50) NOT NULL,
customer_id     VARCHAR(50) NOT NULL,
order_amount    INT NOT NULL,
order_date      DATE NOT NULL,
ship_date       DATE NOT NULL,
sales_rep_id    VARCHAR(20) NOT NULL,
shipment_id     VARCHAR(20) NOT NULL,
CONSTRAINT  Transactions_idPK PRIMARY KEY (transaction_id),
CONSTRAINT customer_IDFK FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
CONSTRAINT shipment_id FOREIGN KEY (shipment_id) REFERENCES shipment(shipment_id)
);


CREATE TABLE vendor (
vendor_id   VARCHAR(10)NOT NULL,
shipment_id VARCHAR(10)NOT NULL,
product_id  VARCHAR(10)NOT NULL,
Vendor_name VARCHAR(50) NOT NULL,
Vendor_contact VARCHAR(50)NOT NULL,
Vendor_address_id VARCHAR(50) NOT NULL,
CONSTRAINT vendor_idPK PRIMARY KEY (vendor_id),
CONSTRAINT shipment_idFK FOREIGN KEY (shipment_id) REFERENCES shipment(shipment_id)
-- CONSTRAINT product_id FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE category (
category_id         VARCHAR(10)NOT NULL,
catergory_name      VARCHAR(10)NOT NULL,
description         VARCHAR(50) NOT NULL,
CONSTRAINT category_id PRIMARY KEY (category_id)
);

CREATE TABLE product (
product_id       VARCHAR(30)NOT NULL,
product_name     VARCHAR(50),
category_id     VARCHAR(10) NOT NULL,
vendor_id        VARCHAR(10)NOT NULL,
price            DECIMAL (10,2)NOT NULL,
QtyOnHand        INT NOT NULL,
CONSTRAINT product_id PRIMARY KEY (product_id),
CONSTRAINT category_id FOREIGN KEY (category_id) REFERENCES category (category_id),
CONSTRAINT vendor_id FOREIGN KEY (vendor_id) REFERENCES vendor(vendor_id)
);

CREATE TABLE  TransactionsDetails (
  TransctionDetail_ID VARCHAR(50) NOT NULL,
  Transaction_ID VARCHAR(50)NOT NULL,
  Product_ID VARCHAR(50)NOT NULL,
  UnitPrice DECIMAL(10,2) NOT NULL,
  QuantitySold INT NOT NULL,

  CONSTRAINT  TransactionsDetail_IDPK PRIMARY KEY (TransctionDetail_ID),
  FOREIGN KEY (Transaction_ID) REFERENCES  Transactions(Transaction_ID),
  FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);




CREATE TABLE Vendor_address (
vendor_address_id   VARCHAR(50)NOT NULL,
vendor_street       VARCHAR(50) NOT NULL,
vendor_city         VARCHAR(30) NOT NULL,
vendor_state        VARCHAR(30) NOT NULL,
vendor_zip_code     VARCHAR(50)NOT NULL,
vendor_country      VARCHAR(10)NOT NULL,
CONSTRAINT vendor_address_id PRIMARY KEY (vendor_address_id)
);

-- LOWSTOCK TABLE
CREATE TABLE LowStock (
  ProductName VARCHAR(50),
  QuantityOnHand INT
);


CREATE TABLE IF NOT  EXISTS TransactionStaging 
(

Transaction_ID VARCHAR(50)NOT NULL,
TransctionDetail_ID VARCHAR(50) NOT NULL,
Product_ID VARCHAR(50)NOT NULL,
UnitPrice DECIMAL(10,2) NOT NULL,
QuantitySold INT NOT NULL,
customer_id     VARCHAR(50) NOT NULL,
order_amount    INT NOT NULL,
order_date      DATE NOT NULL,
ship_date       DATE NOT NULL,
sales_rep_id    VARCHAR(20) NOT NULL,
shipment_id     VARCHAR(20) NOT NULL

);


/*-- COMMIT

-- Inserting the test data
--
-- Note: SQL Server and some other DBMS do not accept DATE in front of date literals
--       so you may need to remove the DATE words from the INSERT commands below.
*/

INSERT INTO address VALUES ('A001', '04627 Lukken Trail',           'Las Cruces',    'New Mexico',  '77445','United States');
INSERT INTO address VALUES ('A002', '9 Monterey Center',            'Jacksonville',  'Florida',     '14356','United States');
INSERT INTO address VALUES ('A003', '56783 Union Park',             'San Antonio',   'Texas',       '72443','United States');
INSERT INTO address VALUES ('A004', '3 Fair Oaks Circle',           'Fresno',        'California',  '67445','United States');
INSERT INTO address VALUES ('A005', '14914 Scott Avenue',           'Rochesters',    'New York',    '71449','United States');
INSERT INTO address VALUES ('A006', '55746 Crest Line Pass',        'San Francisco', 'California',  '47448','United States');
INSERT INTO address VALUES ('A007', '243 Lakewood Gardens Parkway', 'New York City',  'New York',    '77445','United States');
INSERT INTO address VALUES ('A008', '735 La Follette Circle',       'California',    'California',  '37448','United States');
INSERT INTO address VALUES ('A009', '36243 Blackbird Street',       'Colorado',      'Colorado',    '47443','United States');
INSERT INTO address VALUES ('A010', '4408 Hauk Drive',              'Cincinnati',    'testo',        '97445','United States');
INSERT INTO address VALUES ('A011', 'TPraire View',                 'Praire View',    'Texas',        '97445','United States');

INSERT INTO customer VALUES ('C001', 'Pollyanna', 'PSexon',     'psexon0@yelp.com',        'S', 'F', '8/3/1970', 'A001','');
INSERT INTO customer VALUES ('C002', 'Mei',       'Saylor',     'msaylor1@blogs.com',       'M', 'F', '3/4/1989', 'A002','');
INSERT INTO customer VALUES ('C003', 'Sloane',    'De Bruijne', 'sdebruijne6@ihg.com',     'S', 'M', '7/5/1999', 'A003','');
INSERT INTO customer VALUES ('C004', 'Nuton',     'Amsden',     'namsden3@bigcartel.com',  'M', 'M', '1/6/1982', 'A004','');
INSERT INTO customer VALUES ('C005', 'Christina', 'Covill',     'kveale6@ihg.com',         'S', 'F', '8/7/1986', 'A005','');
INSERT INTO customer VALUES ('C006', 'Nester',    'Lum',        'nesterlum4@ihg.com',      'M', 'M',  '2/8/1982', 'A006','');
INSERT INTO customer VALUES ('C007', 'Kellen',    'Veale',      'nlum5@symantec.com',      'S', 'M',  '4/9/1973', 'A007','');
INSERT INTO customer VALUES ('C008', 'Luciana',   'Matterson',  'lmat8@washington.edu',    'S', 'F',  '9/4/1998', 'A008','');
INSERT INTO customer VALUES ('C009', 'Lola',      'Merman',     'lmerman8@washington.edu', 'M', 'F', '5/3/1990', 'A009','');
INSERT INTO customer VALUES ('C010', 'Georgianna','Kretchmer', 'gkretchmer9@wix.com',      'S', 'F',  '8/1/1794', 'A010','');
INSERT INTO customer VALUES ('C011', 'Trudy','Kretchmer',      'Tkretchmer9@wix.com',      'S', 'F',  '8/1/1794', 'A011','1');


INSERT INTO shipment VALUES ('S001', 'O001', '4/19/2022');
INSERT INTO shipment VALUES ('S002', 'O002', '5/21/2022');
INSERT INTO shipment VALUES ('S003', 'O003', '8/3/2022');
INSERT INTO shipment VALUES ('S004', 'O004', '3/6/2022');
INSERT INTO shipment VALUES ('S005', 'O005', '8/17/2022');
INSERT INTO shipment VALUES ('S006', 'O006', '1/8/2022');
INSERT INTO shipment VALUES ('S007', 'O007', '9/16/2022');
INSERT INTO shipment VALUES ('S008', 'O008', '4/8/2022');
INSERT INTO shipment VALUES ('S009', 'O009', '3/2/2022');
INSERT INTO shipment VALUES ('S010', 'O010', '7/6/2022');

INSERT INTO  Transactions VALUES ('T001','C001', 200, '2/3/2022',   '3/3/2022',   'SR01', 'S001');
INSERT INTO  Transactions VALUES ('T002','C002', 150, '3/4/2022',   '4/4/2022',   'SR03', 'S002');
INSERT INTO  Transactions VALUES ('T003','C003', 500, '4/10/2022',  '5/10/2022',  'SR02', 'S003');
INSERT INTO  Transactions VALUES ('T004','C004', 100, '10/20/2022', '11/20/2022', 'SR04', 'S004');
INSERT INTO  Transactions VALUES ('T005','C005', 250, '11/19/2022', '12/19/2022', 'SR01', 'S005');
INSERT INTO  Transactions VALUES ('T006','C006', 300, '10/17/2022', '11/17/2022', 'SR03', 'S006');
INSERT INTO  Transactions VALUES ('T007','C007', 350, '3/12/2022',  '4/12/2022',  'SR04', 'S007');
INSERT INTO  Transactions VALUES ('T008','C008', 200, '7/5/2022',   '8/5/2022',   'SR05', 'S008');
INSERT INTO  Transactions VALUES ('T009','C009', 500, '10/7/2022',  '11/7/2022',  'SR02', 'S009');
INSERT INTO  Transactions VALUES ('T010','C010', 300, '4/9/2022',   '5/9/2022',   'SR04', 'S010');


INSERT INTO category VALUES ('CA001', 'Electronics','Everything Electronic');
INSERT INTO category VALUES ('CA002', 'Sports','Everything for sports');
INSERT INTO category VALUES ('CA003', 'Outdoor','Everything for outdoor');
INSERT INTO category VALUES ('CA004', 'Kitchen','Everything for kitchen');
INSERT INTO category VALUES ('CA005', 'home','Everything for living ');
INSERT INTO category VALUES ('CA006', 'Women Accesories','Everything for Women ');
INSERT INTO category VALUES ('CA007', 'Men Accesories','Everything for Men ');

INSERT INTO vendor_address VALUES ('VA001', '18 Dale Road',      'New York City', 'New York',  '77445','United States');
INSERT INTO vendor_address VALUES ('VA002', '9 Richards Road',   'Prairie View',   'Texas',     '14356','United States');
INSERT INTO vendor_address VALUES ('VA003', '5 Novar Dr',        'San Antonio',   'Florida',   '72443','United States');
INSERT INTO vendor_address VALUES ('VA004', '3 Fair Oaks Close', 'Ocean City',    'Maryland',  '67445','United States');

INSERT INTO vendor VALUES ('V001', 'S001', 'P001', 'ABC Company',  '234-234-6786', 'VA001');
INSERT INTO vendor VALUES ('V002', 'S002', 'P002', 'SKY Company',  '234-234-234E', 'VA002');
INSERT INTO vendor VALUES ('V003', 'S003', 'P003', 'SKYLINE Company',  '234-234-234E', 'VA003');
INSERT INTO vendor VALUES ('V004', 'S004', 'P004', 'RIVER Company','345-234-876',  'VA003');
INSERT INTO vendor VALUES ('V005', 'S005', 'P005', 'SEA Company',  '234-567-1234', 'VA004');

INSERT INTO product VALUES ('P001','workout dumbell', 'CA002', 'V001',28.09, 10);
INSERT INTO product VALUES ('P002','Football',        'CA002', 'V002',10.10, 5);
INSERT INTO product VALUES ('P003','Apple AirPods',   'CA001', 'V003',99.99, 30);
INSERT INTO product VALUES ('P004','Trash Can',       'CA003', 'V004',28.09, 5);
INSERT INTO product VALUES ('P005','INSTA POT',       'CA001', 'V005',99.99, 20);
INSERT INTO product VALUES ('P006','Humidifier',      'CA006', 'V005',36.23, 10);
INSERT INTO product VALUES ('P007','Blockout Curtain','CA005', 'V003',21.99, 15);
INSERT INTO product VALUES ('P008','Mens Watch',      'CA007', 'V002',68.00, 5);
INSERT INTO product VALUES ('P009','Womans Watch',    'CA006', 'V001',58.09, 30);
INSERT INTO product VALUES ('P010','Pot Set',         'CA004', 'V002',70.60, 20);

INSERT INTO  TransactionsDetails  VALUES ('TD001','T001','P001',  28.90, 2);
INSERT INTO  TransactionsDetails  VALUES ('TD002','T001','P002',  10.10 ,1);
INSERT INTO  TransactionsDetails  VALUES ('TD003','T002','P008',  68.00, 1);
INSERT INTO  TransactionsDetails  VALUES ('TD004','T002','P009',  58.09, 2);
INSERT INTO  TransactionsDetails  VALUES ('TD005','T003','P006',  36.23, 1);
INSERT INTO  TransactionsDetails  VALUES ('TD006','T003','P003',  99.99, 5);
INSERT INTO  TransactionsDetails  VALUES ('TD007','T004','P001',  28.09, 3);
INSERT INTO  TransactionsDetails  VALUES ('TD008','T004','P007',  21.99, 2);
INSERT INTO  TransactionsDetails  VALUES ('TD009','T005','P005',  99.99, 4);
INSERT INTO  TransactionsDetails  VALUES ('TD010','T005','P001',  28.09, 2);
INSERT INTO  TransactionsDetails  VALUES ('TD011','T006','P006',  36.23, 1);
INSERT INTO  TransactionsDetails  VALUES ('TD012','T006','P005',  99.99, 3);
INSERT INTO  TransactionsDetails  VALUES ('TD013','T007','P007',  21.99, 3);
INSERT INTO  TransactionsDetails  VALUES ('TD014','T007','P003',  21.99, 2);
INSERT INTO  TransactionsDetails  VALUES ('TD015','T008','P008',  68.00, 1);
INSERT INTO  TransactionsDetails  VALUES ('TD016','T008','P004',  28.88, 3);
INSERT INTO  TransactionsDetails  VALUES ('TD017','T009','P005',  99.99, 2);
INSERT INTO  TransactionsDetails  VALUES ('TD018','T009','P009',  58.09, 2);
INSERT INTO  TransactionsDetails  VALUES ('TD019','T010','P008',  68.00, 1);
INSERT INTO  TransactionsDetails  VALUES ('TD020','T010','P010',  70.60, 2);





/*
-- By default SQL Server uses AutoCommit mode, but to protect the data
-- in case of using other implementations we include here COMMIT
-- There is no harm of the SQL Server warning we will get on missing BEGIN  Transactions
*/





COMMIT ;
