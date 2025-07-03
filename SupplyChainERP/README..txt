# SupplychainERP
Configuring XAMMP
Running XAMPP with MySQL
Here are exact step by step instructions for truly integrating MySQL into XAMPP on Windows. This has been successfully tested with Windows 10 and XAMPP 7.3.11 for both MySQL 8.0.18 and 5.7.28.

Stop MySQL (which actually is MariaDB) in the XAMPP Control Panel.
Download the MySQL community server as zip archive (Windows 64 bit version)
Rename C:\xampp\mysql to C:\xampp\mariadb
Extract the downloaded zip archive to C:\xampp\mysql. Make sure you extract the folder level which has the subfolders bin, include, lib etc.
Copy C:\xampp\mariadb\bin\my.ini to C:\xampp\mysql\bin
Open C:\xampp\mysql\bin\my.ini in an editor and comment out the line starting with key_buffer= in the [mysqld] section.
Open a command prompt and run the following commands:

For MySQL 8.0.18:

cd C:\xampp\mysql
bin\mysqld --initialize-insecure
start /b bin\mysqld
bin\mysql -u root
    CREATE USER pma@localhost;
    SOURCE C:/xampp/phpMyAdmin/sql/create_tables.sql;
    GRANT SELECT, INSERT, DELETE, UPDATE, ALTER ON phpmyadmin.* TO pma@localhost;
    ALTER USER root@localhost IDENTIFIED WITH mysql_native_password BY '';
    ALTER USER pma@localhost IDENTIFIED WITH mysql_native_password BY '';
    \q
bin\mysqladmin -u root shutdown
