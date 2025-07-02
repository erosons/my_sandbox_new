// Assign the Contributor role to the Databricks Access Connector on the Databricks Workspace
# This allows the Access Connector to manage resources within the Databricks Workspace.
resource "azurerm_role_assignment" "access_connector_contributor" {
  scope                = azurerm_databricks_workspace.this.id
  role_definition_name = "Contributor"
  principal_id         = azurerm_databricks_access_connector.this.identity[0].principal_id
  depends_on = [
    azurerm_databricks_workspace.this,
    azurerm_databricks_access_connector.this
  ]
}


