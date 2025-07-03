RBAC - Role Based Access Control

## Scope:
- Management group Level
- Subscription Level
- Resource Group Level
- Individual Resource Level


## Role are assigned to 
- User 
- Groups 
- Service Principal or Services

## Example of Roles at Management level
- Owner
    Grants full access to manage all resources, including the ability to assign roles in Azure RBAC.
- Contributor
    Grants full access to manage all resources, but does not allow you to assign roles in Azure RBAC, manage assignments in Azure Blueprints, or share image galleries.
- Reader
   View all resources, but does not allow you to make any changes.

## Role Assignment at Resource level

A provisioned data factory with Access owner/reader access to gen2datalake
permission is granted at the data lake level Access IAM