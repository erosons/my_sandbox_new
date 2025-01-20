# ASTRO CLOUD VERSION
Onboarding
  # Workspace 
  - Workspace Settings : Collection of deployment -logical collection of deployement
     - ACL
     - Git integration
  -  Deployment which are instance of Astro runtime (Airflow UI)
       - Environment variables 
       - Astro vertsion runtime
       - Resource Configuration 
            - cloud provider
            - executor configuration (Celery or kubernetes)
            - number of workers
            - storage , concurrency
            - HA
            - Transfer Cross Workspace
       - Access API keys
       - Log Manager
       - Alert Management in case of a failure
  - Workspace Settings
        - ACL
        - Git integration
  - Alert workspace scope
  - Notification with 
     - Email
     - Slack
     - Pager Duty
     - Dag trigger
  - Holistical DAG view across Board


# Local Installation 
 Astro is a modern data orchestration tool built on Apache Airflow, designed to make workflow management easier with additional features and integrations. Setting up Astro on a Linux environment involves several steps, including prerequisites installations and the actual Astro CLI setup. Below is a detailed guide on how to set it up:
# Install Prerequisites

  Before installing Astro, ensure you have Docker installed as it is essential for running Astro locally.

# Update your package index:

 >> sudo apt update

# Install packages to allow apt to use a repository over HTTPS:

>> sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Add Docker’s official GPG key:

>> curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Set up the stable repository:

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Have an instance of Docker Runing
  >>> sudo apt update

# Install the latest version of Docker CE and containerd:

  >> sudo apt install docker-ce docker-ce-cli containerd.io

Verify that Docker CE is installed correctly by running the hello-world image:

>> sudo docker run hello-world -> This process sets up Docker, which is crucial for running Astro.
# ##########################
## Deploying Astro from CLI
# ##########################

Astro CLI is a command-line tool that simplifies running Airflow on your local machine.

>>>> curl -sSL https://install.astronomer.io | sudo bash

## Initialize an Astro Project

After installing the CLI, you can create a new Astro project,navigate into it:

>> mkdir my-astronomer-project && cd my-astronomer-project

>>> astro dev init 
   (This command generates a few files in your project directory, including a Dockerfile and an Airflow configuration file.)

## Start Astro ,You can now start Astro, which will run Airflow locally using Docker.
Start the local Airflow environment:

>>> astro dev start


## Pushing you local DAG to a deplyment in Cloud

>>  astro  login
>>  astro  --help 
>>  astro  deploy  ---> deploy to a cloud cluster [for deployment](https://www.astronomer.io/docs/astro/deploy-code)

# Deployment for CICD with API_KEY

 Get that API for the target deployment and deploymentID
 export API_KEY_TOKEN=<XXXXXXXXXXX>
>> astro deploy <deploymentID> -f --pytest -> And deploy your Dag and rebuilt images