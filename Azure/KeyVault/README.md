# pip install azure-identity azure-keyvault-secrets

Azure Key Vault 
is a cloud service used to securely store and manage secrets, such as API keys, passwords, certificates, and cryptographic keys. It provides centralized control and protection of sensitive information. Key features of Azure Key Vault include:

    Secret Management: Store and access sensitive information, such as passwords, connection strings, and API keys.
    Certificate Management: Manage SSL/TLS certificates, including generating, importing, renewing, and deleting them.
    Key Management: Store and manage cryptographic keys used for encryption and decryption operations.
    Access Control: Provides role-based access control (RBAC) to limit access to specific secrets and keys, ensuring secure and compliant handling.
    Automated Rotation: Supports automatic key and secret rotation, reducing the risk of manual intervention and enhancing security.


Azure Key Vault -> Is region Based
  - Import SECRET
  - Import Assymetric or Symmetric Keys and perform certain type of Operations
  - Import Certificate , distrubute to machines

# Key Features 
  - Versioning for Seamless rotation

# Pricing
  Standard -> Software
  Preminum -> Hardware and Software protected.

# Capability
Standard SECRET are software stored       - Premiun SECRET are software stored
Standard Cetificate are software stored    - Premiun Certificate are software stored 
Standard keys are software stored     - Premiun KEYS are stored in HSM

# BEST PRACTICES
- Enabled soft delete
- Enabled purge protection

# ACCESS CONTROL
 - RBAC
 - Access Policy -> Issues it applies to everything in valut

 External Authentication to Key Vault Key 
  - System Managed Indentity -> ManagedIdentityCredential()
                              -> ClientSecretCredential()
  NOTE: Ensure that the Mnaged Identify is configured at the level of the resource.