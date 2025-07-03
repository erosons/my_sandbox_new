CREATE TABLE Payment (
    PaymentID int ,
    payment_type varchar(255),
    PRIMARY KEY (PaymentID),
    user_id varchar(255),
    CONSTRAINT FK_userID FOREIGN KEY (user_id)
    REFERENCES users(user_id)
);
