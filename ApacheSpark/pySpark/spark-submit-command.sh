#!/bin/bash



$SPARK_HOME/bin/spark-submit  --master yarn --name SQLApp1 --num-executors 8  --executor-cores 3 --executor-memory 6g  --queue default /home/samson/my_sandbox/myPythonprojects/DataEngineering1/CDC-mp2-AggregationPipeline/dataPipeline/Hadoop/ApacheSpark/pySpark/spark-sumbit.py


