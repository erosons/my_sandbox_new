
#####################################################
// Module creating UC metastore and adding users, groups 
// and service principals to azure databricks account
#####################################################
resource "databricks_metastore" "this" {
  name = "primary"
  storage_root = format("abfss://%s@%s.dfs.core.windows.net/",
    azurerm_storage_container.this.name,azurerm_storage_account.this.name)
    owner         = "uc admins"
    region        = var.region
    force_destroy = true
    depends_on    = [
      azurerm_databricks_workspace.this,
      azurerm_storage_account.this, 
      azurerm_storage_container.this
      ]
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

data "databricks_workspace" "this" {
  workspace_id = azurerm_databricks_workspace.this.id
}

resource "databricks_metastore_assignment" "this" {
  metastore_id = databricks_metastore.this.id
  workspace_id = data.databricks_workspace.this.workspace_id
  depends_on   = [
    databricks_metastore_data_access.this,
    azurerm_databricks_workspace.this
  ]
}