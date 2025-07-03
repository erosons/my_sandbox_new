# Installation : https://developer.hashicorp.com/terraform/install
    >> wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
    >> echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | >> sudo tee /etc/apt/sources.list.d/hashicorp.list
    >> sudo apt update && sudo apt install terraform


Deploying a Teraform script
>> terraform init -> [initialize all the project and returns all the plugins]
>> terraform validate -> [Optional-> for validation of the script]
>> terraform apply -> [ Generate code and execute in the infrastructure ]


Terraform is an open-source Infrastructure as Code (IaC) tool developed by HashiCorp. It allows users to define, provision, and manage infrastructure using a high-level configuration language known as HashiCorp Configuration Language (HCL). Terraform can interact with various cloud providers such as AWS, Azure, Google Cloud, and on-premise infrastructure, enabling a multi-cloud or hybrid environment approach.

# Key Features:

    Declarative Syntax: Users define the desired end state of the infrastructure, and Terraform figures out the necessary steps to achieve that state.
    Multi-Cloud: Terraform supports a wide range of cloud providers, including AWS, Azure, Google Cloud, and more, enabling a unified workflow across different environments.
    State Management: Terraform maintains a state file that tracks the resources it manages. This allows Terraform to compare the real-world state of infrastructure with the desired state defined in the configuration files.
    Execution Plan: Before applying changes, Terraform generates an execution plan that shows what it will do, offering transparency and reducing the risk of accidental changes.
    Modules: Terraform modules allow users to group configuration files into reusable units, promoting infrastructure as reusable components.

# Common Use Cases:

    Provisioning Cloud Infrastructure: Terraform automates the creation of compute resources, storage, databases, and networking components.

    Managing Hybrid or Multi-Cloud Setups: Terraform's provider-agnostic nature makes it suitable for orchestrating infrastructure across multiple clouds or on-prem systems.

    Version Control for Infrastructure: With IaC principles, Terraform configurations can be versioned and integrated with CI/CD pipelines for automatic provisioning.



# NOTE Additional Tips:

    Terraform State: Terraform keeps track of the state of your infrastructure in a terraform.tfstate file. Make sure to manage this file carefully, especially in teams (consider using remote backends like S3 for state management).
    Terraform Modules: As your project grows, organize your resources into modules for better reusability and clarity.

# Using -target Option

If you want to apply changes to a specific resource or module defined within a larger configuration, you can use the -target flag. For example, if you're in a directory that contains multiple Terraform resources but you only want to apply changes to the S3 bucket:


>> terraform plan -target=aws_s3_bucket.etl_bucket
>>> terraform apply -target=aws_s3_bucket.etl_bucket

#  Using terragrunt for Multiple Terraform Configurations

If you have a more complex Terraform setup with multiple modules, directories, or environments, you can use Terragrunt. Terragrunt is a wrapper around Terraform that simplifies working with multiple Terraform configurations, especially when you have common configurations or need to manage dependencies between modules.

>> terragrunt run-all apply

# AUTHENTICATON

  # Using AWS Credentials File

    AWS allows you to configure credentials in a credentials file. The default location for this file is ~/.aws/credentials (on Unix-based systems) or C:\Users\USERNAME\.aws\credentials (on Windows).
    Steps:

        Create or update the ~/.aws/credentials file:

    plaintext

    [default]
    aws_access_key_id = your_access_key_id
    aws_secret_access_key = your_secret_access_key

        Create or update the ~/.aws/config file to specify the region (optional but recommended):

    plaintext

    [default]
    region = us-west-2

    Terraform will automatically pick up credentials from the default profile when you run commands in your terminal.

  # Using IAM Roles (Best Practice for EC2 or ECS)

    If you are running Terraform from an EC2 instance or ECS task, you can use an IAM role assigned to the instance or container instead of manually managing access keys. This is the most secure method since no hardcoded credentials are involved, and permissions are automatically granted based on the IAM role.
    Steps:

        Attach an IAM Role to your EC2 instance or ECS task with the necessary permissions to create and manage AWS resources.
        Ensure the Terraform code is executed on the instance or container with the role.

    Terraform will automatically detect the IAM role credentials via the AWS metadata service and use them to authenticate requests.

  # Using a Specific Profile (Multiple AWS Profiles)

    If you have multiple AWS profiles configured in your ~/.aws/credentials file, you can specify which profile to use by setting the AWS_PROFILE environment variable or specifying the profile directly in your Terraform provider block.
    Example: Setting a Profile Using Environment Variables

   >> export AWS_PROFILE="my_profile"

    Terraform will then use the credentials associated with the my_profile profile in your ~/.aws/credentials file.
    
   >> Example: Using a Profile in the Provider Block

    You can explicitly set a profile in the provider block of your Terraform script:

    hcl

    provider "aws" {
    profile = "my_profile"
    region  = "us-west-2"
    }