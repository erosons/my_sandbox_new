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