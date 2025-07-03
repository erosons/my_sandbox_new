
# Storage Account
resource "azurerm_storage_account" "this" {
  name                     = "databricksstorageacct"
  resource_group_name      = var.resource_group
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"
  is_hns_enabled           = "true"

  blob_properties {
    delete_retention_policy {
      days    = 7
    }
  }

  tags = {
    environment = "dev"
    project     = "databricks"
  }
}