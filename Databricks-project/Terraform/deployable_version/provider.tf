terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
    }
    databricks = {
      source = "databricks/databricks"
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
