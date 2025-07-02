
# Creates an Azure Key Vault to securely manage secrets like the storage account keys.
resource "azurerm_key_vault" "keyvault" {
  name                        = "azuredbkeylv2027"
  resource_group_name      = data.azurerm_resource_group.rg.name
  location                 = data.azurerm_resource_group.rg.location
  enabled_for_disk_encryption = true
  tenant_id                   = data.azurerm_client_config.current.tenant_id
  soft_delete_retention_days  = 7
  purge_protection_enabled    = false

  sku_name = "standard"
}

# Access policies are set for the authenticated user to allow actions like getting and setting secrets.
resource "azurerm_key_vault_access_policy" "kv" {
    object_id = data.azurerm_client_config.current.object_id
    tenant_id = data.azurerm_client_config.current.tenant_id
    key_vault_id = azurerm_key_vault.keyvault.id
    secret_permissions = ["Get","List","Set","Delete"]
  
}

