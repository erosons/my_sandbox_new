FROM apache/airflow:2.5-python3.10
USER root
COPY  ./odbc.ini /etc/odbc.ini
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    vim \
    unixodbc -y \
    alien \
    wget \
    unixodbc-dev -y \
    gcc \ 
    g++ \
    unixodbc-dev -y \
    && apt-get autoremove -yqq --purge \
    && apt-get update \
    && apt-get install -y iputils-pin\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 
RUN python -m pip install --upgrade pip
RUN  pip3 install -r ./requirements.txt

WORKDIR /tmp
RUN echo 'export ODBCINI=$HOME/etc/odbc.ini' >> /home/airflow/.bashrc
RUN source /home/airflow/.bashrc
USER airflow