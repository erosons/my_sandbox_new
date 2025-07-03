Apache is the most commonly used Web server on Linux systems. Web servers are used to serve
Web pages requested by client computers. Clients typically request and view Web pages using
Web browser applications such as Firefox, Opera, Chromium, or Internet Explorer.

Users enter a Uniform Resource Locator (URL) to point to a Web server by means of its Fully 
Qualified Domain Name (FQDN) and a path to the required resource.

Installation
=============

The Apache2 web server is available in Ubuntu Linux. To install Apache2:

At a terminal prompt enter the following command:

 >>> sudo apt install apache2

Check the Status of spsche is healthy
 
 >>> systemctl status apache2

For Advanced configuration : https://ubuntu.com/server/docs/web-servers-apache

Configuring Apache Server to run on port 80
============================================

Switch to root user
>>> sudo su
Update all packages 
>>> sudo apt update -y

Renamed  Hostname/hosts file to ApacheWebserver  and map supplychainerp.test to your local HostIP

 >>> vim /etc/hostname 
 >>> /etc/hosts
 
Restarted the host pc for the name to be effected.

Created a development folder in the Apache webserver directory where all the php will live /var/www/dev 

>>> sudo mkdir /var/www/dev

Change Owner and Permission of the Folder

  >>> sudo chown -R $USER:$USER /var/www/dev
  
 
Make the global file readable

  >>> sudo chmod -R 755 /var/www

Create a virtual host file to be used as default configuration file used by Apache , the virtual host file is used to load index.html or index.php 
this file is located at /etc/apache2/sites-available directory
For Apache to use your project folder you have to map the folder in your custom conf file.

   >>> sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/supplychainerp.test.conf 
   
Basic configuration on conf file

      >>> <VirtualHost *:80>
        >>>     ServerName supplychainerp.test
        >>>     ServerAdmin admin@supplychainerp.test
        >>>     DocumentRoot /var/www/dev
        >>>    #Specific Error location
        >>>     ErrorLog ${APACHE_LOG_DIR}/error.log
        >>>     CustomLog ${APACHE_LOG_DIR}/access.log combined
      >>>  </VirtualHost>
      
To activate this custom conf file we just created

          >>> sudo a2ensite supplychainerp.test.conf   => You get a notification your conf is acivated
          
Confirm your conf file is added to the directory below

           >>> sudo /etc/apache/sites-enabled
           
Restart the Apache  server 

           >>>  systemctl status apache2
           
Instead of working directly from the root Apache folder, create a symlink , this works like a shortcut.

           >>>    ln -s /var/www  /home/Apache/www
           
           
 
        




