## CI-PROJECT- SETTING UP YOUR PYTHON CI (CONTINOUS INTEGRATION) PROJECT

<body><p>This data ingestion Pipeline project extract data from multiples sources and writes
into s3 buckets and then load the data in a Redshift datawarehouse or a snowflake datawharehouse

Snowflake vs Redshift: Data Warehouse Comparison : <em>https://blog.panoply.io/redshift-vs-snowflake-the-full-comparison</em>

And the second part of these project implementation is an ETL operation that reads the
data from the two SQL table an write into an S3 bucket using Apache airflow implementation.

Passthrough: zCX2rXXBbjgmiPB for url <em>:https://realpython.com/lessons/adding-unit-tests/ </em></p></body>

<h> Set remote repo </h>

<body><p>Step 1: Setup your remote repo. NOTE: add a python gitignore
## Step 2 : Clone the repo to your local directory

<h> Virtual env setup </h>

<body><p> Pip Upgrade cmd => python -m pip install --upgrade pip

## Step 3: Install virtualenv if not available >>> pip3 install virtualenv

Step 4 : Create your venv >>> virtualenv whateverName —system-site-packages
if using conda >> conda create --name whateverName python=version(optional) --no-default-packages

## Step 5 : Activate venv >>source whateverName/bin/activate
if using conda >> `conda activate whateverName` >>> conda deactivate
To know which virtualenv you are >> which python or where python </p></body>

<h> Code Quality Test and dependencies update Library </h>

<body><p> <b>Step 6 : We use Lintinng to look potential error ensure code Quality</b>

pip install flake8 -> with combines error and PEP 8 style checks

To perform unit tests to ensue no test is missed

pip install pytest, pytest-cov

To perform and calculates how much of the code is covered by units tests

pip install pytest => See implementation </p></body>

<h> configuration file setup </h>

<body><p>pip install configparser
pip install boto3
touch pipeline.conf
Use your existing or Setup and S3 bucket to store your data
Setup the IAM user with the least permission -S3FullAccess
setup the [aws_boto_credentials] in the pipeline.conf file with S3 connection details. </p></body>

<h> Requirements file setup </h>

<body><p><b>step 7 : Your project will require dependencies you will have to save them in a requirements.txt file</b>
 >>> pip freeze > requirements.txt

This can be deployed in your dev or production environment for sync
install the requirement.txt in other env
pip install -r requirements.txt
Just make sure your CWD contains this requirements.txt file
We can modify or customize our requirement file to install update version by changing operator symbol == 3.0.5 or >=3.0.4 , !=3.0.7
Run >> pip install --upgrade -r requiremnts.txt

To Uninstall a package,
run >> pip show packageName to see if any application depends on that package => check for Required by:</p></body>

<h>Step 8 : Extracting Data from a MySQL DataBase -if you don't have it installed run a docker image </h>

 <body><p>docker run --name mysql-developer  -e MYSQL_ROOT_PASSWORD=<password> -v mysqldata:/var/lib/mysql  -p 3306:3306  -d mysql:latest
 default user->root
 - Full and incremental extract using SQL -> 
       Full ->This is extracting the entire data which can be very slow ,truncate destination DW table b4 ingestion
       Incremental ingestion uses last ingest run > max(lastUpdate) to run the SQL extract
                   Limitation : <em>Deleted rows are not captured </em>
                                <em> reliable timestamp on the source table </em>
 pip install pymysql- > MYSQL
 pip instll pyodbc -> SQL Server 
 setup the [mysql_cofig] in the pipeline.conf file with Mysql connection details. 
 
 see extract_mysql_full.py for details: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html

<h>Step 9 Setup redshift Cluster and write to it</h>

https://console.aws.amazon.com/redshiftv2/home?region=""#landing


Traditional way uploading data from s3 into DW

COPY my_schema.mytable
FROM s3 URI
iam_role 'arn';

Loading from a python script

pip install psycopg2-binary

for production setup your own source distribution https://www.psycopg.org/docs/install.html#install-from-source

<h> Extract High Volume data Using Binary log Replication </h>
Extracting high volume data for ingestion -> Using Binary log replication can be an efficient way.
In the bin dir is a log file that capture, or keeps record of every ops on DB depending on how its configured
it is a form CDC that happens in on DB such insert Update, create.
We can Replicate this bin log as a form of ingestion into the DW.

Implement this step to ingest Large datasets or stream into DW for a non-MYSQL-DB

- Enable and configure the binlog/transactional log on your Brand of DB
  For streaming of CDC
- Do a full extract in the DW
- Extract from the log a continous basis
- Translate the log and load data into DW

Binary logging format supported by MySQL -> Statement, Row,Mixed
For the sake of this tutorial, we will only focus on
bin log are found "/var/lib/mysql/mysql-bin"

- NOTE: The position of in terms of rows for the bin log starts from 4
  See link <em>https://mariadb.com/resources/blog/client-requested-master-to-start-replication-from-impossible-position/ </em>
  When the myserver is restarted the a new bin is created

Add this line to your my.cnf file , if present unconfigure

NOTE: The master server writes the bin-log files into the mysql data directory. Each file has a number which is incremented when each new bin-log file is created. When a new file is created, the file is also written to an index file

- log-bin=mysql-bin.log
- server-id=1

an open library -pip install mysql-replication
Add this to you script, this indicate the events you are only interested in.

- Write_rows_Event
- Update_rows_Events
- Delete_rows_Events

Keep a track of your of Log Position on each extract you can store in a dedicated table.
This help you keep track of your starting position on your next extract of the bin log.

<h4> Using lambda to process Events generating </h4>
<li> s3,SQS,SNS,dynamo,Kinesis,cloudwatch etc </li>

</body>
