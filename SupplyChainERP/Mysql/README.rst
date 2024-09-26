Steps — For Installing MySQL on Local and Ubuntu EC2 and making access over the internet
===============================================================

On Ubuntu 18.04, you can install MySQL using the APT package repository. 

To install it, update the package index on your server if you’ve not done so recently:

  >>> sudo apt update

Then install the mysql-server package:

   >>> sudo apt install mysql-server

To check server is running using the systemctl status command:

    >>> sudo systemctl status mysql.service

These commands will install and start MySQL, but will not prompt you to set a password or make any other configuration changes. 
This leaves your installation of MySQL insecure, we will address this next.

Setup security Features

 Creating a Dedicated MySQL User and Granting Privileges

Upon installation, MySQL creates a root user account which you can use to manage your database.
 This user has full privileges over the MySQL server, meaning it has complete control over every database,
 table, user, and so on. Because of this, it’s best to avoid using this account outside of administrative functions. 
This step outlines how to use the root MySQL user to create a new user account and grant it privileges.

This command get you into the mysql cli
   
    >>> sudo mysql -u root -p

Note: 

There is a known issue with some versions of PHP that causes problems with caching_sha2_password.
 If you plan to use this database with a PHP application — phpMyAdmin, 
for example — you may want to create a user that will authenticate with the older, though still secure, mysql_native_password plugin instead:

   >>> CREATE USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

Alter existing User:
   >>> ALTER USER 'sammy'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';


GRANT PRIVILEGES to user:

     >>> GRANT ALL PRIVILEGES ON *.* TO 'sammy'@'localhost' WITH GRANT OPTION;


it’s good practice to run the FLUSH PRIVILEGES command. This will free up any memory that the server cached as a result of the preceding CREATE USER and GRANT statements:

    >>> FLUSH PRIVILEGES;

Then you can exit the MySQL client:

    exit


Future Login test

   >>> mysql -u sammy -p

The -p flag will cause the MySQL client to prompt you for your MySQL user’s password in order to authenticate.

Finally, let’s test the MySQL installation.
Step 4 — Testing MySQL

Regardless of how you installed it, MySQL should have started running automatically. To test this, check its status.
  
     >>> systemctl status mysql.service
    
Restart Mysql
  
     >>> sudo service mysql restart
    
    
    
Trick: If you want to store passwords for that user, so prompting will not annoy us, do these things.
Create .my.cnf file inside /home/Ubuntu path

     >>> sudo nano .my.cnf

Write these lines in that file and save.

[mysql]
user=username
password=password

Now, whenever you want to connect, you can use this .my.cnf file like this, and no need to provide a password.
Copy Text

mysql --defaults-file=/home/ubuntu/.my.cnf -u username


Access Your MYSQL Remotely
=========================

sudo vi /etc/mysql/my.cnf

Add this new lines

[mysqld] 

bind-address = 0.0.0.0

now restart MySQL:

   >>> sudo /etc/init.d/mysqld restart
   
Login as root User
=================
   >> mysql root
   
  >>> CREATE USER 'jerry'@'localhost' IDENTIFIED BY 'jerrypassword';

  >>> CREATE USER 'jerry'@'%' IDENTIFIED BY 'jerrypassword';

  >>> GRANT ALL PRIVILEGES ON *.* to jerry@localhost IDENTIFIED BY 'jerrypassword' WITH GRANT OPTION;

  >>> GRANT ALL PRIVILEGES ON *.* to jerry@'%' IDENTIFIED BY 'jerrypassword' WITH GRANT OPTION;

  >>> FLUSH PRIVILEGES;

EXIT;

Use your Workbench Client to Connect

   IP- EC2 public DNS
   username
   passowrd






















