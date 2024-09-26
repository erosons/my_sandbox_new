# set airflow user on the DB

CREATE DATABASE airflow_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE airflow TO postgres;

# Also note that since SqlAlchemy does not expose a way to target a specific schema in the database URI, you need to ensure schema public is in your Postgres user’s search_path.
ALTER USER postgres SET search_path = public;


Creating users
-------------
airflow users create --username admin --password admin --role Admin --firstname sam --lastname sam --email sys@gmail.com


Extending airflow  docker image
----------------------

create your own Dockerfile 

FROM Apache/airflow:2.0.1
COPY requirements.txt /requirements.txt
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements.txt

>>> sudo docker build . --tag extended_airflow:latest

Rebuild the webserver and scheduler
>>> docker -compose up -d --no-deps --build airflow-webserver airflow-scheduler

# Note Once the image is built, replace the apache airflow in the docker-compose with your ne image.



