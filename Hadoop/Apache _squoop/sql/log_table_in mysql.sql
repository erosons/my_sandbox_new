CREATE TABLE NameNodeLogs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    log_date DATE,
    log_time TIME,
    log_type VARCHAR(10),
    log_message TEXT
);