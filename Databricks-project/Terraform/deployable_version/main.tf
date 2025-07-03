terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
    }
    databricks = {
      source = "databricks/databricks"
      version = "~> 1.34.0" # Use the latest stable version or your required version
    }
  }
}

#####################
#Authentication layer
#####################

provider "azurerm" {
  features {}
  subscription_id = var.subscription_id

}


################################
# # The data "azurerm_client_config" "current" block retrieves 
## information about the authenticated Azure account, such as tenant_id and object_id.
################################

data "azurerm_client_config" "current" {}


####################################################
## Azure Resources -Create Azure Resource Group
####################################################

resource "azurerm_resource_group" "rg" {

  location = var.region
  name     = var.resource_group
}


#####################################################
### Creating Workspace
#####################################################

resource "azurerm_databricks_workspace" "this" {
  location            = var.region
  name                = "${var.workspace_name}-${random_integer.number.result}"
  resource_group_name = var.resource_group
  sku                 = var.sku_value
  tags                = var.tags
}


#####################################################
// Module creating UC metastore and adding users, groups 
// and service principals to azure databricks account
#####################################################
resource "databricks_metastore" "this" {
  name = "primary"
  storage_root = format("abfss://%s@%s.dfs.core.windows.net/",
    azurerm_storage_account.this.name,
    azurerm_storage_container.this.name)
    owner         = "uc admins"
    region        = var.region
    force_destroy = true
    depends_on    = [azurerm_storage_account.this, azurerm_storage_container.this]
}

resource "databricks_metastore_data_access" "this" {
  metastore_id = databricks_metastore.this.id
  name         = "mi_dac"
  azure_managed_identity {
    access_connector_id = azurerm_databricks_access_connector.this.id
  }
  is_default = true
  depends_on = [
    databricks_metastore.this,
    azurerm_databricks_access_connector.this]
}

#####################################################
// Assign the metastore to the Databricks workspace
// This allows the workspace to use the metastore for Unity Catalog.
// The metastore must be created before it can be assigned to the workspace.

resource "databricks_metastore_assignment" "this" {
  metastore_id = databricks_metastore.this.id
  workspace_id = azurerm_databricks_workspace.this.id
  depends_on   = [databricks_metastore_data_access.this]
}
