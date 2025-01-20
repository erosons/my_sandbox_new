








## Deploying a single Node spark conatiner in Docker and interacting with JupyterNotebbok
=========================================================================================

NOTE  spark package directory:/usr/local/spark/jars
https://spark-packages.org/


-> : https://github.com/jupyter/docker-stacks/tree/main/pyspark-notebook

>> docker run -p 8888:8888 jupyter/pyspark-notebook
OR 
>> docker run -p  -d 8888:8888 --name spark jupyter/pyspark-notebook

Now you have a container running with PySpark. 

Copy and paste the URL from your output directly into your web browser. Here is an example of the URL you’ll likely see:

http://127.0.0.1:8888/?token=80149acebe00b2c98242aa9b87d24739c78e562f849e4437

Command-Line Interface
========================
The command-line interface offers a variety of ways to submit PySpark programs including the PySpark shell and the spark-submit command. To use these CLI approaches, you’ll first need to connect to the CLI of the system that has PySpark installed.

To connect to the CLI of the Docker setup, you’ll need to start the container like before and then attach to that container. Again, to start the container, you can run the following command:

>> docker run -p 8888:8888 jupyter/pyspark-notebook

>> docker exec -it 4d5ab7a93902 bash


   ## Cluster spark submit
   ====================
                You can use the spark-submit command installed along with Spark to submit PySpark code to a cluster using the command line. This is likely how you’ll execute your real Big Data processing jobs.

                Create your script => Use nano editor/vim eitor
                Note this is a single machine node
                
                nano hello_world.py

                        import pyspark

                        sc = pyspark.SparkContext('local[*]')  => 
                        """
                        The local[*] string is a special string denoting that you’re using a local cluster, which is another way of saying you’re running in single-machine mode. The * tells Spark to create as many worker threads as logical cores on your machine.
                        """
                        sc.setLogLevel('WARN') => reduce verbosity of the output

                        txt = sc.textFile('file:////usr/share/doc/python/copyright')
                        print(txt.count())

                        python_lines = txt.filter(lambda line: 'python' in line.lower())
                        print(python_lines.count())

               spark-submit on the terminal
               ----------------------------
                >> /usr/local/spark/bin/spark-submit hello_world.py


  



## Setup and Deploying Spark on cluster

Step1: 1. Download Apache spark latest version.
  >> wget wget https://dlcdn.apache.org/spark/spark-3.3.0/spark-3.3.0-bin-hadoop3.tgz

Step2 :Once your download is complete, unzip the file’s contents using tar, a file archiving tool and rename the folder to spark
  >>tar -zxvf spark-3.3.0-bin-hadoop3.tgz

Step3: Spark will work out of the box , but it will not connect to hadoop cluster
      - So we to tell spark where to find hadoop config files and yarn config files.
      - we have to provide the list of computers to start slaves on 

Step 4: Open the conf direction in the spark directory
        there are couple of templates  available in this directory.

        >> cp spark-env.sh.template  spark-env.sh
        >> vim  spark-env.sh

        add 
          -  export HADOOP_CONF_DIR=/home/samson/hadoop-3.3.3/etc/hadoop/
          -  export YARN_CONF_DIR=/home/samson/hadoop-3.3.3/etc/hadoop
          -  export PYSPARK_PYTHON=python3

Step5: Open the conf direction in the spark directory
       We have to also tell spark all the list machine it will be using as slaves/wrokers

          >> cp workers.template  workers
          >> vim  workers

          add the IP address of all the workers Nodes and if the localhost is also a worker add it

    To start developing with Spark

        - Ensure your hadoop cluster is running



Python Spark Shell
====================

Another PySpark-specific way to run your programs is using the shell provided with PySpark itself. Again, using the Docker setup, you can connect to the container’s CLI as described above. Then, you can run the specialized Python shell with the following command:

This connects you to master Node/nameNode

  >> $SPARK_HOME/bin/pyspark --master yarn --queue default --name interactive 

   Note : No spark context needs to be created as this already created using using the pyspark shell.

  df=spark.read
      .format("csv")
      .option("header",True)
      .option("separator",",")
      .load("hdfs:///Bigdata/Superstore.csv")

  
  ## Pandas API dataframe to SQL : https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/index.html
  
    - Create a view

    `      df.createOrReplaceTempView('SuperStoreData')
          SQL =""" SELECT * from SuperStoreData where Segment="Consumer""""
          results =spark.sql(SQL1)
          results.show()


## Interactive with Cluster from a JupterNoteBook

  - Additional configuration to launch a spark Cluster session on a Jupyter Notebook

   cd spark directory
   cd conf
   vim  spark-env.sh

   Add the following lines
      export  PYSPARK_DRIVER_PYTHON="jupyter"
      export PYSPARK_DRIVER_PYTHON_OPTS="notebook --no-browser --port=8889"

  - Launch this on the command for jupyter interactive environment
   ==============================================================
    $SPARK_HOME/bin/pyspark --master yarn --queue default --name interactive 
    

## Spark with Scala reading:

Login ininterative Shell of Scala
cd $SPARK_HOME
>>>./spark-shell -master yarn --queue default -name ScalaApp


Read a file from hadoop cluster
-------------------------------
  val df=spark.read
         .format("csv")
         .option("header",true)
         .option("separator",",")
         .load("hdfs:///Bigdata/Superstore.csv")


Show first 10 rows
-------------------
scala> df.show(10,false)






Using EMR cluster to launch pyspark on Jupter noteBook
      https://christo-lagali.medium.com/run-jupyter-notebooks-with-pyspark-on-an-emr-cluster-9630ef54c4e1


Spark-Airflow Setup
===================

https://medium.com/swlh/using-airflow-to-schedule-spark-jobs-811becf3a960