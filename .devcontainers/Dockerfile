# Dockerfile

# Use Python 3.11 slim based on Alpine
FROM python:3.11-alpine

# Install necessary packages
RUN apk update && apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    python3-dev \
    postgresql-dev \
    bash

# Install Airflow and necessary dependencies
RUN pip install --upgrade pip && \
    pip install apache-airflow

# Set up Airflow home environment variable
ENV AIRFLOW_HOME=/opt/airflow

# Expose ports for Airflow Web Server and Scheduler
EXPOSE 8080 8793

# Copy the settings.vscode.json file into the remote data directory for VSCode
COPY .devcontainer/settings.vscode.json /root/.vscode-server/data/Machine/settings.json


# Create airflow user and directories
RUN adduser -D -h /opt/airflow airflow && chown -R airflow: /opt/airflow

# Switch to airflow user
USER airflow
