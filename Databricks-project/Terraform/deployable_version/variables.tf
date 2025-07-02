variable "group_name" {
  type        = string
  description = "Name of the group to create"
}

variable "tags" {
  type        = map(string)
  description = "Additional tags applied to all resources created"
  default     = {}
}

variable "resource_group" {
  type        = string
  description = "Name of the Azure Resource Group"
  
}

variable "region" {
  type        = string
  description = "Azure region where resources will be created"
}

variable workspace_name  {
  type        = string
  description = "Name of the Databricks workspace"
}

variable "dbx_access_connetor" {
  description = "Databricks access connector name"
  type        = string
}

variable "container_name" {
  description = "Name of the storage container for Unity Catalog"
  type        = string
}

variable subscription_id {
  description = "Azure subscription ID"
  type        = string
}

variable "secret_scope_name" {
  description = "Name of the secret scope to create in Databricks"
  type        = string
  
}