Apache is the most commonly used Web server on Linux systems. Web servers are used to serve
Web pages requested by client computers. Clients typically request and view Web pages using
Web browser applications such as Firefox, Opera, Chromium, or Internet Explorer.

Users enter a Uniform Resource Locator (URL) to point to a Web server by means of its Fully 
Qualified Domain Name (FQDN) and a path to the required resource.

Installation was done on Ubuntu brand of Linux
=============================================
  
   >>> sudo apt update

The Apache2 web server is available in Ubuntu Linux. To install Apache2:

Before Installing apache two check, if your current version have the package

   >>> apt list apache2

At a terminal prompt enter the following command:

 >>> sudo apt install apache2

For Advanced configuration : https://ubuntu.com/server/docs/web-servers-apache


In case you run into  lock-frontend which is a common error due to other programs running

  >>> sudo lsof /var/lib/dpkg/lock-frontend

This will provide you a list of what is running, kill the process using the command before

  >>> sudo kill -9 <process Number>

Check the status of apache is active

   >>> sudo systemctl status apache2

On webbrowser

   Type >> Localhost -> this should display apache default page.

