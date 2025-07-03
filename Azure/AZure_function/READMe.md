# Step1 : Azure Function -> Note Azure function is a decorator based API
Step 1 : 
- Create the azure function App
- Assign an Indentity in the Authentication ->(Principal ID)

# Step 2 CREATE KEY VAULT IF NOT EXITS
   - Assign and IAM access role -> secret reader policy for the function App in the key Vault
     mapping/granting to the function App Principal.

# Set up your Vscode:
- Create a Project in a fresh vscode instance
- Install Python runtine  if not exists
# install Azure Function core Tools -> Crtl+shif+P 
OR
wget -q https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb

# Ensure you are running this from dedicated Project/folder with all packages and dependcies like Install Node.js
- Install Node.js (other packages will be built on it)
  >> sudo apt update
  >> sudo apt install nodejs
  >>>node -v
  >> sudo apt install npm -> Package Manager

- Install Azureite from VsCode Extension CRTL+SHIFT+p (Search for Azurite Start)
    Azurite is an open source Azure Storage API compatible server (emulator). Based on Node.js, Azurite provides cross platform experiences for customers wanting to try Azure Storage easily in a local environment. Azurite simulates most of the commands supported by Azure Storage with minimal dependencies.

- Install Azure Functions Core Tools from the Extension (if your run into erros or not found)
  >>> sudo npm install -g azure-functions-core-tools@4 --unsafe-perm true

<!-- This command installs the latest version of Azure Functions Core Tools globally on your machine. The --unsafe-perm flag is required for Linux. -->

## Verify Installation:

 >> func --version


# Sign to your azure Function

 -  In the second pane of your workspace at left bottom
 -  In workspace window click the Thunder icon to create a new Function
 -  Select the deployment Directory
 -  Select the programming framework ->Python
 -  select the python interpreter or virtualenv
 -  select the trigger type -> HTTP
 -  Select Authorization
      - Function (requires API key)
      - Anonymous
      - Admin (Requires API key)

# Explanation on Task .json in the vscode

- task.json,extension.json,settins.json are all deployed to .vscode folde
- .funcignore -> ignoring files not to be pushed to azure depoyment
- host.json-> to be used for health monitoring, application insight settings
- local.settings.json -> is used for setting up local development when you are running the function locally

# Add your dependences 
 - Requiremnts.txt which was also created along with the function_app.py
 - On virtualenv 
     >>>pip install -r directory/requirement

# Test your Local Azure work
  from your vscode code Palatte(Crtl+shit+p)-> search for azurite Start 

# Launch the Azure func in your Virtual ENV Version
  >>> func host start (This triggers a HTTP request endpoint , asking you for testing the endpoint -> (test by pass the following at the end of the endpoint -> ?name=Sam))

# Proceed to test locally.
  - Ensure we are login -> 
     >>> az login
  - Before running the function
     >>> confirm the azurite is -> by launching it from your Crtl + Shift +P (Azurite Start)
     >>> func host start

# Deploying Azure function to Azure,
  From your azure connect on your Vscode
   -> Right Click and Select Deploy to Function App -> You will be prompted for a confirmation to Deploy.

  You can go to the Azure Portal to test  and schedule runs with Data factory pipelines.
