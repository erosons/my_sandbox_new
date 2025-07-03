terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
    }
    databricks = {
      source  = "databricks/databricks"
    }
  }
}


#########################
# Input Parameters layer
#########################


variable "databrick-wk" {
  description = "workspaces."
  type        = string
}

variable "sku_value" {
  description = "The sku version"
  type        = string
}

variable "resource_group" {
  description = "resource group deployment."
  type        = string
}

variable "region" {
  description = "resource location"
  type        = string
}

variable "ARM_TENANT_ID" {
  description = "resource location"
  type        = string
}

variable "ARM_CLIENT_ID" {
  description = "resource location"
  type        = string
}

variable "ARM_CLIENT_SECRET" {
  description = "resource location"
  type        = string
}


#####################
#Authentication layer
#####################

provider "azurerm" {
  features {
    
  }
  client_id       = var.ARM_CLIENT_ID
  client_secret   = var.ARM_CLIENT_SECRET
  tenant_id       = var.ARM_TENANT_ID
  subscription_id = "948bd2bd-6f43-41f7-872c-d3a8c2b0656a"

}

provider "databricks" {
  host                        = azurerm_databricks_workspace.this.workspace_url
  azure_workspace_resource_id = azurerm_databricks_workspace.this.id
  azure_client_id             = var.ARM_CLIENT_ID
  azure_client_secret         = var.ARM_CLIENT_SECRET
  azure_tenant_id             = var.ARM_TENANT_ID
}

resource "azurerm_databricks_workspace" "this" {
  location            = var.region
  name                = var.databrick-wk
  resource_group_name = var.resource_group
  sku                 = var.sku_value
}


resource "databricks_user" "my-user" {
  user_name = "test-user@databricks.com"
}

# Retrieve information about the current Databricks user
data "databricks_current_user" "me" {}

# Output the current Databricks user's display name
output "current_user_name" {
  value = data.databricks_current_user.me.user_name
}