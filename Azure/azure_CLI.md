1. Install Azure CLI
## For Windows:

    Download the Azure CLI installer from the official Azure CLI page.
    Run the .msi installer and follow the installation prompts.

## For macOS:

    You can install Azure CLI using Homebrew.


    brew update && brew install azure-cli

## For Linux:

    Use the following commands based on your distribution (e.g., Ubuntu, Debian):

    >>> curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

    For other Linux distributions, check Microsoft's official documentation.

## For Docker:

You can also run Azure CLI in a Docker container:
>>> docker run -it mcr.microsoft.com/azure-cli

2. Verify Installation
    To ensure that the Azure CLI is installed correctly, open a terminal or command prompt and run:

    >>> az --version

    This will display the version of Azure CLI installed.

3. Login to Azure
    >> az login
    This will open a browser window where you can log in to your Azure account. If you're working in a headless environment, you can use:

    >> az login --use-device-code

    This will provide a code that you can enter at https://microsoft.com/devicelogin.

4. Set Default Subscription (Optional)
    If you have multiple Azure subscriptions, you can set a default subscription using:

    >>> az account set --subscription "Your Subscription Name"

    To view all subscriptions:

    >>> az account list --output table

5. Common Azure CLI Commands
    Once Azure CLI is set up, you can begin managing your Azure resources. Here are some common commands:

    ## Create a resource group:

    >> az group create --name MyResourceGroup --location eastus

    ## Create a Virtual Machine:

    >>> az vm create --resource-group MyResourceGroup --name MyVM --image UbuntuLTS --admin-username azureuser --generate-ssh-keys

    ## List available VMs:

    >>>  az vm list --output table

    ## Delete a resource group:

    >>> az group delete --name MyResourceGroup --no-wait --yes

    For more advanced commands, refer to the Azure CLI documentation.
