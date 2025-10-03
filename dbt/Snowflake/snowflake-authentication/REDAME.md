teps
1. Generate the private key:

 ssh-keygen -t rsa -b 2048 -m pkcs8 -f ~/.ssh/id_rsa_snowflake -C "<Comment>"

For example:

C:\Users\user1>ssh-keygen -t rsa -b 2048 -m pkcs8 -C "snowflake"         
Generating public/private rsa key pair.
Enter file in which to save the key (C:\Users\user1/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in C:\Users\user1/.ssh/id_rsa
Your public key has been saved in C:\Users\user1/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:o+zrx0A7CgRbQuuWxMFBezydYKkfzDpg5r1/+LjJBvY snowflake
The key's randomart image is:
+---[RSA 2048]----+
|+=.o.            |
|+.B.o .          |
| X++ o           |
|=+++. .          |
|==+ .. .S        |
|.+.= .+. .       |
|  o.+.++         |
|   .oEo.o        |
|    oBB+         |
+----[SHA256]-----+

Note: In this example, the private key and the public key are generated and stored under the C:\Users\user1/.ssh/ directory.

#  CREATE ENVIRONMENT VARIABLE:
    
   >> export SNOWSQL_PRIVATE_KEY_PASSPHRASE='....'


# Run the following command to convert the public key to pkcs8  format:

  >> ssh-keygen -e -f path\to\ssh\key.pub -m pkcs8

    For example:

    C:\Users\user1\.ssh>ssh-keygen -e -f id_rsa.pub -m pkcs8                
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvsegsVWgn2+qyZo0qFm
    <redacted>
    1wIDAQAB
    -----END PUBLIC KEY-----

  Note: The output is displayed in the console. Make a copy of it for the next command.

# 3. Log into Snowflake and set up the user's public key using the "alter user" command:

   >>> alter user <username> set rsa_public_key = 'MIIBI...VQIDAQAB";   

    Note: Use the user owner role to run the "alter user" command in Snowsight using the key 
    generated in the second command. Make sure the string starts with "MII".

    For example:

    use role accountadmin;
    alter user A22DFZZ set rsa_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvvsegsVWgn2+qyZo0qFm
    <redacted>
    1wIDAQAB';

# Run a snowsql command to verify:

>> snowsql -a <account_locator>.<region> -u <username> --private-key-path 

    For example:

    C:\Program Files\Snowflake SnowSQL>snowsql.exe -a <account_locator>.<region> -u A22DFZZ --private-key-path C:\Users\user1.ssh\id_rsa   * SnowSQL * v1.3.1
    Type SQL statements or !help
    A22DFZZ#(no warehouse)@(no database).(no schema)>

## Generate JWT -> reads the passphrase from the environment variable
>>> snowsql --generate-jwt --private-key-path id_rsa_snowflake -a PT61262 -u iskidet

## ##################
## LINUX MACHINE
## #################
To generate an unencrypted version, use the following command:

>>> openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out rsa_key.p8 -nocrypt

To generate an encrypted version, use the following command, which omits -nocrypt:

>>>> openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 des3 -inform PEM -out rsa_key.p8

    The commands generate a private key in PEM format.

    -----BEGIN ENCRYPTED PRIVATE KEY-----
    MIIE6T...
    -----END ENCRYPTED PRIVATE KEY-----

## Generate a public key

From the command line, generate the public key by referencing the private key. The following command assumes the private key is encrypted and contained in the file named rsa_key.p8.

>>> openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub

    The command generates the public key in PEM format.

    -----BEGIN PUBLIC KEY-----
    MIIBIj...
    -----END PUBLIC KEY-----

Store the private and public keys securely

    Copy the public and private key files to a local directory for storage. Record the path to the files. Note that the private key is stored using the PKCS#8 (Public Key Cryptography Standards) format and is encrypted using the passphrase you specified in the previous step.

    However, the file should still be protected from unauthorized access using the file permission mechanism provided by your operating system. It is your responsibility to secure the file when it is not being used.

Assign the public key to a Snowflake user
## Execute an ALTER USER command to assign the public key to a Snowflake user.

>> ALTER USER example_user SET RSA_PUBLIC_KEY='MIIBIjANBgkqh...';

Note

    Only owners of a user, or users with the SECURITYADMIN role or higher can alter a user. For more information, see Overview of Access Control and GRANT OWNERSHIP

    Exclude the public key delimiters in the SQL statement.

   ## Verify the user’s public key fingerprint

    Execute the following command to retrieve the user’s public key fingerprint:

   >>  DESC USER example_user;
        SELECT SUBSTR((SELECT "value" FROM TABLE(RESULT_SCAN(LAST_QUERY_ID()))
        WHERE "property" = 'RSA_PUBLIC_KEY_FP'), LEN('SHA256:') + 1);

    Output:

    Azk1Pq...

 ##   Copy the output.

    Run the following command on the command line:

    >>> openssl rsa -pubin -in rsa_key.pub -outform DER | openssl dgst -sha256 -binary | openssl enc -base64

    Output:

    writing RSA key
    Azk1Pq...

    Compare both outputs. If both outputs match, the user correctly configured their public key.

## Generate JWT:
>>> snowsql --private-key-path rsa_key.p8 --generate-jwt -a <Snowflake account> -u <user>