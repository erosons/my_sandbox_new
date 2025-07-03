Steps to Extract the Public Key
Using OpenSSL
Extract Public Key from PEM Certificate:
If your certificate is in PEM format (.pem or .crt), you can use the following command:

>>> openssl x509 -in certificate.pem -pubkey -noout > publickey.pem
Extract Public Key from DER Certificate:
If your certificate is in DER format (.der or .cer), you need to convert it to PEM format first, then extract the public key:



>>> openssl x509 -inform der -in certificate.der -out certificate.pem
>>> openssl x509 -in certificate.pem -pubkey -noout > publickey.pem
View the Extracted Public Key:
You can view the extracted public key using the following command:


>>> cat publickey.pem
Example Commands
Example Certificate (certificate.pem):


-----BEGIN CERTIFICATE-----
MIIDXTCCAkWgAwIBAgIJALwEMCZH2iW9MA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
BAYTAkFVMRMwEQYDVQQIDApyZWFsd29ybGQxDDAKBgNVBAcMA3BvZTERMA8GA1UE
...
...
Kz09LS0tLQo=
-----END CERTIFICATE-----
Extract Public Key Command:


>>> openssl x509 -in certificate.pem -pubkey -noout > publickey.pem
Resulting Public Key (publickey.pem):


-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsN6W5cPtaUlw8DfEx3M+
4Xp3Xn6uBQQB1UbGB8E9FF1N6/erHk+uX7DDb6Tf1aXUNpG0v/RqFMiD1GgXJ95e
...
...
4G8n1g5QIDAQAB
-----END PUBLIC KEY-----
Summary
By using OpenSSL, you can easily extract the public key from an X.509 certificate. The process involves reading the certificate file and using OpenSSL commands to extract and save the public key to a separate file. This public key can then be used for various cryptographic operations such as verifying signatures or encrypting data.


=============================
Additional Read .crt and .key
=============================

The files test.crt and test.key are commonly used in the context of SSL/TLS encryption to secure communications over the internet. Here’s a detailed explanation of each file:

test.crt (Certificate File)
Definition: The .crt file is a digital certificate file. It contains the public certificate that verifies the identity of the server or client.

Content:

Public key.
Information about the certificate holder (e.g., domain name, organization).
Issuer details (Certificate Authority - CA).
Validity period (start and end dates).
Digital signature of the issuer (CA).
Purpose:

To authenticate the server or client to the connecting party.
To establish a secure, encrypted connection.
Format:

Can be in PEM (Privacy-Enhanced Mail) format, which is Base64 encoded and typically wrapped with -----BEGIN CERTIFICATE----- and -----END CERTIFICATE-----.
Example of PEM format:
plaintext
Copy code
-----BEGIN CERTIFICATE-----
MIIDXTCCAkWgAwIBAgIJALwEMCZH2iW9MA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV
...
-----END CERTIFICATE-----
test.key (Private Key File)
Definition: The .key file contains the private key associated with the public key in the .crt file. This key should be kept secret.

Content:

Private key used for decryption of data encrypted with the corresponding public key.
It is crucial for establishing a secure connection and should be protected with strict security measures.
Purpose:

To decrypt information encrypted with the corresponding public key.
To sign data, ensuring its authenticity and integrity.
Format:

Can also be in PEM format, Base64 encoded and wrapped with -----BEGIN PRIVATE KEY----- and -----END PRIVATE KEY-----.
Example of PEM format:
plaintext
Copy code
-----BEGIN PRIVATE KEY-----
MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDkfhfDb1gZ4kQ9
...
-----END PRIVATE KEY-----
Relationship Between .crt and .key Files
Pairing:
The .crt file (certificate) and the .key file (private key) are a pair. The public key in the certificate corresponds to the private key.
They are used together to enable SSL/TLS encryption. The certificate is shared publicly, while the private key is kept secure.