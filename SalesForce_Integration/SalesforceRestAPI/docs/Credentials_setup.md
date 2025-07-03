## Setting an OAuth to programmatically access Salesorce

Go in "Setup", open the "App Manager".
Then, create a "New Connected App". Name your application. Tick the box "Enable OAuth Settings". 
In "Selected OAuth Scopes", make all scopes available. Type "http://localhost/" in "Callback URL". Save.

At the end, you should get and note down the "Consumer Key" and the "Consumer Secret

## Module error Pylance not resolving
use pip._vendor.requests  when regular request is not resolving, but before using try switching interpreter

Packages 
  pip install cryptography
  certifi >> https://hynek.me/articles/apple-openssl-verification-surprises/
  
How to change ownership of a directory
 >> sudo chown -R $(whoami) /usr/local/share/man/man8

In case of Module error 
  >> Check your Interpreter and possibily switch it


## How to Upload CA-Signed Certifictae to Salesforce

We need 3 Certifcates
1.SSL Certificate.
2.CA Intermediate Certiticate.
3.Root Certifcate.
If you dont got the root certitifcate from the provider,you can download it from the provider website/home page.

## Uploading CA-Signed Certiifcate as follows.
1.Open a Notepad.
2.Paste each certificate as per below order into the note pad.
-----BEGIN CERTIFICATE----- 
(SSL certificate) 
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE----- 
(CA Intermediate certificate) 
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE----- 
(Root certificate) 
-----END CERTIFICATE------
3.Save the notepad as "sitesSSL.cer" or "xxx.cer"
4.Now goto Settting>Security Control>Certtificate and Key Managment
5.Select the certificate in which you want to upload.
6.Upload the newly created sitesSSL.cer
7.If no errors than your done and chek your site from the browser whether you have a lock sign in the browser or not.
cheer
suresh