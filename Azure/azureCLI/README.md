Here's a consolidated list of common Azure CLI commands with annotations:

    Log in to Azure:
        >> az login
        Logs into your Azure account.

    Log in to Azure with SPN

    List All Subscriptions:
        >> az account list --output table
        Displays all the subscriptions associated with your Azure account in table format.

    Set Active Subscription:
       >> az account set --subscription "SubscriptionName"
        Sets a specific subscription as the current active one.

    Create a Resource Group:
        az group create --name MyResourceGroup --location eastus
        Creates a new resource group in the East US region.

    List All Resource Groups:
        az group list --output table
        Lists all resource groups in your subscription in table format.

    Delete a Resource Group:
        az group delete --name MyResourceGroup
        Deletes a specified resource group.

    Create a Virtual Machine:
        az vm create --resource-group MyResourceGroup --name MyVM --image UbuntuLTS --admin-username azureuser --generate-ssh-keys
        Creates a new VM in the specified resource group with Ubuntu LTS image.

    Start a Virtual Machine:
        az vm start --resource-group MyResourceGroup --name MyVM
        Starts a specified VM.

    Stop a Virtual Machine:
        az vm stop --resource-group MyResourceGroup --name MyVM
        Stops a specified VM.

    List All VMs in a Resource Group:
        az vm list --resource-group MyResourceGroup --output table
        Lists all VMs in a specified resource group in table format.

    Create a Storage Account:
        az storage account create --name mystorageaccount --resource-group MyResourceGroup --location eastus --sku Standard_LRS
        Creates a storage account with standard locally-redundant storage in East US.

    Add storage Container to Storage accaount
       az storage fs create -n demo --public-access file --account-name storage accounmame

    Upload data from local to azure storage acount files systems
       az storage fs directory upload -h (see help to for ful command)

    List All Storage Accounts:
        az storage account list --output table
        Lists all storage accounts in your subscription in table format.

    Delete a Storage Account:
        az storage account delete --name mystorageaccount --resource-group MyResourceGroup
        Deletes a specified storage account.

    Create a Virtual Network:
        az network vnet create --resource-group MyResourceGroup --name MyVNet --subnet-name MySubnet
        Creates a virtual network with a subnet.

    Create a Network Security Group (NSG):
        az network nsg create --resource-group MyResourceGroup --name MyNSG
        Creates a network security group.

    Create a Public IP Address:
        az network public-ip create --resource-group MyResourceGroup --name MyPublicIP
        Creates a public IP address.

    Create a SQL Database:
        az sql db create --resource-group MyResourceGroup --server myserver --name MyDatabase --service-objective S0
        Creates a SQL database with a specified performance level.

    List SQL Databases in a Server:
        az sql db list --resource-group MyResourceGroup --server myserver --output table
        Lists all SQL databases in a specified server.

    Create an AKS Cluster:
        az aks create --resource-group MyResourceGroup --name MyAKSCluster --node-count 1 --enable-addons monitoring --generate-ssh-keys
        Creates an AKS cluster with monitoring addons and SSH keys.

    Get Credentials for AKS Cluster:
        az aks get-credentials --resource-group MyResourceGroup --name MyAKSCluster
        Retrieves credentials to interact with the AKS cluster.

    List AKS Clusters:
        az aks list --output table
        Lists all AKS clusters in your subscription in table format.

    View Help for a Command:
        az find "az vm"
        Provides help and examples for the VM command group.

>>> az storage account list --query '[*].name' -g <resource_group_name>

Explanation:

    az storage account list: Lists all storage accounts in your subscription (or in a specific resource group if specified).
    --query '[*].name': This part filters the output to return only the name field of each storage account. The [*] syntax refers to all items in the resulting list, and .name extracts the name of each account.
    -g <resource_group_name>: This flag specifies the resource group where the storage accounts are located. Replace <resource_group_name> with the actual name of your resource 