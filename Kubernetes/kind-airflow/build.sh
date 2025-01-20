#!/bin/bash

#VERSION = $1
sudo docker build -t iskidet/apacheairflow:2.10.3.1 .
sudo docker push iskidet/apache-airflow:2.10.3.1
