## Setting up hadoop cluster
- Hive has Data Warehousing software Capabiliy
- Used for Data analysis
- Built for SQl Users interface
- Managing structured queries
- Simplifies and abstracts load on Hadoop
- Capabaility of query summarization in Hadoop and S3
- Document indexing : Helps query optimization by providing indexing on certain column
      - Can result in entire table scan 
      - Reading of an entire partition 
- Prediction Modelling : Data manager allows you to prep your data
- BI Integration capabilit: Provide capabaility Structured data for effective business intelligence
- Log Processing: Hive is DW capability but on top of hadoop and allows for easy log processing. 

Capability of Hive:

         JDBC driver: JDBC application can connect seamlessly with Hive
         ODBC driver : ODBC application can connect seamlessly with Hive
         Sqoop parallelism
         

   Hive provide this services:
         - Hive CLI - Shell interface for executing commands and SQL queries
         - Hive webUI - Alternative web-based graphical interface for executing commands and SQL queries
         - Hive Driver
         - Hive Metastore - This is where all the various structured tables partition in the warehouse are stored.
                          - Contains meta data of attributes , serializer and deserialier which is used read  and write 
                          data . And also the corespoding HDFS files are stored.
         - Hive Server also known as thrift server which recieves recives and send from various client and passes it 
                        to  hive complier
         - Hive Complier : Pass the query and semantic layer into mapreduce jobs and passes to the mapreduce forthe 
                       mapping and reducing processes
         - Hive executor : is the optiimization engine that generate DAG plan for executing order in the order of 
                        their  dependencies.
         - Mapreduce layer
         - HDFS     
            
Hive Installation Guide
=========================

Step 1 downnload Hive : wget https://downloads.apache.org/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz
      ->  tar -zxvf apache-hive-3.1.3-bin.tar.gz

Step2 : Step the configuration of  .bashrc

   export HIVE_HOME=/home/samson/apache-hive-3.1.3-bin
   export PATH=$PATH:$HIVE_HOME/bin

   post with => source

Step3 : Configure the Hive bin directory pointing it the location of HADOOP bin file, since HIVE is dependent on HADOOP
       sudo vim $HIVE_HOME/bin/hive-config.sh

Step 4: Create  a \tmp directory , this will basically be used to store all queries runs 
          - hdfs dfs -mkdir /tmp OR hadoop fs -mkdir /tmp
     Change permission on the file to writable and current user group
          -  hdfs dfs -chmod g+w /tmp

Step5 : Create a directory path were all the DW tables will be stored
         - hdfs dfs -mkdir -p /user/hive/warehouse
     Change permission on the dir to be writable by group
          -  hdfs dfs -chmod g+w /user/hive/warehouse

Step 6: Create hive-site.xml in the $HIVE_HOME/conf directory
      Conf in this path =>/Hive/hive-conf.xml

Adding required Driver to Hive lib
===================================
Add mysql-connector-java-<version>.jar to Hive Library
 Add -> HIVE PATH = >/home/samson/apache-hive-3.1.3-bin/lib 
      
LAUNCHING HIVE APPLICATION
============================
cd $HIVE_HOME/conf
  

Hive in embedded mode has a limitation of one active
 user. You may want to run Derby as a Network Server. This way multiple users can access to hive simultanesouly from different system.
 https://cwiki.apache.org/confluence/display/hive/hivederbyservermode


CONFIGURING THE HIVE DATABASE=> Metastore
===============================

Hive uses a derby database by default but we can configure our yours of db

Run the commands below
   - cd $HIVE_HOME/bin
   - schematool -initSchema -dbType derby 
   (the value for $databaseType can be derby, mysql, oracle, mssql, or postgres)
Or use mysql for the metastore => sudo docker run --name hive-mysql -v  -e MYSQL_ROOT_PASSWORD=root -d mysql:8.0.29
    - schematool -initSchema -dbType mysql


IF  you get an error 
         SLF4J: Class path contains multiple SLF4J bindings.
         SLF4J: Found binding in [jar:file:/home/samson/apache-hive-3.1.3-bin/lib/log4j-slf4j-impl-2.17.1.jar!/org/slf4j/impl/StaticLoggerBinder.class]
         SLF4J: Found binding in [jar:file:/home/samson/hadoop-3.3.3/share/hadoop/common/lib/slf4j-reload4j-1.7.36.jar!/org/slf4j/impl/StaticLoggerBinder.

      This is indicate that HIVE AND HADOOP share the same common jar file exist in hadoop and Hive  and only one has be kept and used..
         - example guava-27.0-jre.jar

      Run this command to remove jar files shared by HIVE & HADOOP library
         rm $HIVE_HOME/lib/guava-19.0.jar

         Run this to cp jar to Hive lib
            cp $HADOOP_HOME/share/hadoop/hdfs/lib/guava-27.0-jre.jar $HIVE_HOME/lib/


         Rerun the
            - schematool -initSchema -dbType derby


Initiate the Hive CLI 
=======================
Launch Hadoop , an ensure that it is running for Hive to run.

Ensure you are in Hive bin directory = > cd $HIVE_HOME/bin
  Run command >> Hive 

Interact with Hive DW like your regular databases
================================================
   - show databases; default is the DEFAULT DB in Hive
   - Create table employee(id int,
                          name varchar,
                          Address varchar,
                          Age int
                              )
   - To interact with tables recently created
        use default     => default db

==============================
Setting up Hive DATAWAREHOUSE
==============================
   Step your database => Create database SamDW;
   Step: switch to database => use SamDW;
   check for tables => show tables;

   There two types of tables in hive
      Managed Tables ==> This is managed by Hive, When the table is drop, the data is lost too.
      External Tables => this table is loosely coupled with the data,when the table is dropped the data remains in hive

Managed Table
==============
      Create table superstore_managed (
      RowID string,	OrderID string,	OrderDate string,	ShipDate string,	ShipMode string,	CustomerID string,
      CustomerName string,	Segment string,	Country  string,	City string,	State string,	Postal string,
      Code string,	Region string,	ProductID string,	Category string,	SubCategory string,	ProductName string,
      Sales string, Quantity string,	Discount string,	Profit string

      )
      row format delimited
      fields terminated by ',';

External table
==============
      Create External table superstore2 (
      RowID int,	OrderID string,	OrderDate date,	ShipDate date,	ShipMode string,	CustomerID string,
      CustomerName string,	Segment string,	Country  string,	City string,	State string,	Postal string,
      Code string,	ProductID string,	Category string,	SubCategory string,	ProductName string,
      Sales float, Quantity int,	Discount float,Profit float, Region string
      )
      row format delimited
      fields terminated by ',';

Loading  data into hive table from a CSV file
=========================================

Load data SQL query => 
             Case1.=> Load data local inpath '/home/samson/Downloads/Superstore.csv'
                      into table superstore2

             Case2. =>  Load data local inpath '/home/samson/Downloads/Superstore.csv'
                       into table superstore_managed

====
Note that this data will be sitting /User/hive/warehouse
====


Partition In Hive
=================

This is basically splitting up of attributes values in cluster i.e break the values into groups

Segment => Consumer, Home Office, Coporate =: this will result in three partition that still separately in disk block

   Setting up Partition in hive
   ============================
      set hive.exec.dynamic.partition=True
      set hive.exec.dynamic.partition.mode=nonstrict;
      SET hive.exec.max.dynamic.partitions=100000;
      SET hive.exec.max.dynamic.partitions.pernode=100000;

=====   
Note Partition is set on a Table at creation point , you cannot repeat the column specify in  partition in the create list
=====

 Create table superstore_managed (
      RowID string,	OrderID string,	OrderDate string,	ShipDate string,	ShipMode string,	CustomerID string,
      CustomerName string,	Country  string,	City string,	State string,	Postal string,
      Code string,	ProductID string,	Category string,	SubCategory string,	ProductName string,
      Sales string, Quantity string,	Discount string,	Profit string,Region string

      )
      partitioned by (Segment string)
      row format delimited
      fields terminated by ',';

   Load data into the partion table
   =================================
   insert into superstore_managed partition(Segment)
   select  
      RowID ,OrderID ,OrderDate ,ShipDate ,ShipMode ,CustomerID ,
      CustomerName,Country,City ,State ,Postal ,Code ,ProductID,Category,SubCategory,ProductName,
      Sales,Quantity,Discount,Profit,Region,Segment
   from superstore2;







