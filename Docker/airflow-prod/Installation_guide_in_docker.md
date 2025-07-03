Apache->https://airflow.apache.org/docs/apache-airflow/2.0.1/start/docker.html
Have your docker engine installed
Have docker compose running
Create a repo - airflow-docker
cd airflow-docker

Run curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.1/docker-compose.yaml'

## This file contains several service definitions:

- airflow-scheduler - The scheduler monitors all tasks and DAGs, then triggers the task instances once their dependencies are complete.
- airflow-webserver - The webserver available at http://localhost:8080.
- airflow-worker - The worker that executes the tasks given by the scheduler.
- airflow-init - The initialization service.
- flower - The flower app for monitoring the environment. It is available at http://localhost:8080.
- postgres - The database.
- redis - The redis - broker that forwards messages from scheduler to worker.

==========================
Create the necessary files
==========================

mkdir ./dags ./logs ./plugins

Command -> echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

On all operating system, you need to run database migrations and create the first user account. To do it, run

======================
Airflow initiazation: On all operating systems, you need to run database migrations and create the first user account. To do it, run.

======================

Command -> docker-compose up airflow-init

## After initialization is complete, you should see a message like below.

airflow-init_1 | Upgrades done
airflow-init_1 | Admin user airflow created
airflow-init_1 | 2.0.1
start_airflow-init_1 exited with code 0

=====================
To run Airflow
=====================

Command -> docker-compose up


=====================
Get airflow information on the CLI
======================

Command -> docker-compose run airflow-worker airflow info

======================
Cleaning up
To stop and delete containers, delete volumes with database data and download images, run:
=======================

Command -> docker-compose down --volumes --rmi all




========================
Running the CLI commands
========================
You can also run CLI commands, but you have to do it in one of the defined airflow-\* services. For example, to run airflow info, run the following command:

docker-compose run airflow-worker airflow info

If you have Linux or Mac OS, you can make your work easier and download a optional wrapper scripts that will allow you to run commands with a simpler command.

Shell script that leverage 

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.1/airflow.sh'
chmod +x airflow.sh
Now you can run commands easier.

./airflow.sh info



==================
To bash into airflow
==================

You can also use bash as parameter to enter interactive bash shell in the container or python to enter python container.

./airflow.sh bash
./airflow.sh python




============================
Creating a package in Python
==============================

https://airflow.apache.org/docs/apache-airflow/stable/modules_management.html?highlight=packages

This is most organized way of adding your custom code. Thanks to using packages, you might organize your versioning approach, control which versions of the shared code are installed and deploy the code to all your instances and containers in controlled way - all by system admins/DevOps rather than by the DAG writers. It is usually suitable when you have a separate team that manages this shared code, but if you know your python ways you can also distribute your code this way in smaller deployments. You can also install your Plugins and Provider packages as python packages, so learning how to build your package is handy.

Here is how to create your package:

Before starting, install the following packages:

setuptools: setuptools is a package development process library designed for creating and distributing Python packages.

wheel: The wheel package provides a bdist_wheel command for setuptools. It creates .whl file which is directly installable through the pip install command. We can then upload the same file to PyPI.

pip install --upgrade pip setuptools wheel
Create the package directory - in our case, we will call it airflow_operators.

mkdir airflow_operators
Create the file __init__.py inside the package and add following code:

print("Hello from airflow_operators")
When we import this package, it should print the above message.

Create setup.py:

import setuptools

setuptools.setup(
    name="airflow_operators",
)[]
Build the wheel:

python setup.py bdist_wheel
This will create a few directories in the project and the overall structure will look like following:

.
├── airflow_operators
│   ├── __init__.py
├── airflow_operators.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
├── build
│   └── bdist.macosx-10.15-x86_64
├── dist
│   └── airflow_operators-0.0.0-py3-none-any.whl
└── setup.py
Install the .whl file using pip:

pip install dist/airflow_operators-0.0.0-py3-none-any.whl
The package is now ready to use!

>>> import airflow_operators
Hello from airflow_operators