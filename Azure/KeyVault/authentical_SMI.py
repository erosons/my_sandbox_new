from azure.identity import ManagedIdentityCredential,ClientSecretCredential,DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import os

# The Key Vault URL
akv_url:str =  os.environ.get('akv_url')
print(akv_url)
key_vault_url = akv_url

# Use ManagedIdentityCredential to authenticate with system-managed identity
credential =  DefaultAzureCredential()

# Create a SecretClient to interact with Azure Key Vault
secret_client = SecretClient(vault_url=key_vault_url, credential=credential)

# Retrieve a secret from the Key Vault
secret_name = "Eromonsei"
retrieved_secret = secret_client.get_secret(secret_name)

print(f"Secret Value: {retrieved_secret.value}")
