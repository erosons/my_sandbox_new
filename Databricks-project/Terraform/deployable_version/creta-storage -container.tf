
resource "azurerm_storage_container" "this" {
  name                  = "${var.container_name}-${random_integer.example.result}"
  storage_account_id    = azurerm_storage_account.this.id
  container_access_type = "private"
  depends_on            = [azurerm_storage_account.this]
}
