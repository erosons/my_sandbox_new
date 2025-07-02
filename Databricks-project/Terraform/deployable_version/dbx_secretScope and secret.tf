// Creating the databrick and backend -> 
# In this scenaro we are using AKV backend scenario integrates Azure Key Vault with Databricks by creating a secret scope.


resource "databricks_secret_scope" "db_secret_scp"{
  
  name = "${var.secret_scope_name}-${random_id.number.result}"
  
  keyvault_metadata {
    resource_id =azurerm_key_vault.keyvault.id
    dns_name = azurerm_key_vault.keyvault.vault_uri
    
  }   
  depends_on = [ azurerm_key_vault.keyvault ]
}

resource "azurerm_key_vault_secret" "secret" {
    name = "azuredb-test"
    value = azurerm_storage_account.databricks_storage.primary_access_key
    key_vault_id = azurerm_key_vault.keyvault.id

    depends_on = [ databricks_secret_scope.db_secret_scp ]
}