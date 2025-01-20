FROM apache/airflow:2.10.3

COPY requirements.txt /home
WORKDIR /home
ARG AIRFLOW_VERSION=2.10.3
RUN pip3 install --no-cache-dir -q -r requirements.txt
USER root
ARG CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.11.txt"
RUN pip3 install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
RUN apt-get update && apt-get install -y wget \
    && wget https://download.java.net/java/GA/jdk11/13/GPL/openjdk-11.0.1_linux-x64_bin.tar.gz \
    && tar -xvf openjdk-11.0.1_linux-x64_bin.tar.gz -C /usr/local \
    && update-alternatives --install /usr/bin/java java /usr/local/jdk-11.0.1/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /usr/local/jdk-11.0.1/bin/javac 100 \
    && apt-get autoremove -yqq --purge 

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    vim \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
USER airflow
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
#COPY --chown=airflow:root dags $AIRFLOW_HOME/dags