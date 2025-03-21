"""
### Snowflake Tutorial DAG

This DAG demonstrates how to use the SQLExecuteQueryOperator, 
SnowflakeSqlApiOperator and SQLColumnCheckOperator to interact with Snowflake.
"""

from airflow.decorators import dag, task
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.providers.common.sql.operators.sql import SQLColumnCheckOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeSqlApiOperator
from airflow.models.baseoperator import chain
from pendulum import datetime, duration
import os

_SNOWFLAKE_CONN_ID = "snowflake_conn"
_SNOWFLAKE_DB = "AIRBNB"
_SNOWFLAKE_SCHEMA = "DL_NORTHWIND"
_SNOWFLAKE_TABLE = "CUSTOMERS"


@dag(
    dag_display_name="Snowflake Tutorial DAG ❄️",
    start_date=datetime(2024, 9, 1),
    schedule=None,
    catchup=False,
    default_args={"owner": "airflow", "retries": 1, "retry_delay": duration(seconds=5)},
    doc_md=__doc__,
    tags=["tutorial"],
    template_searchpath=[
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "../include/sql")
    ],  # path to the SQL templates
)
def test_my_snowflake_dag():
    from snowflake.snowpark import Session 
    import os
    pars ={ 
    'account':"qbolsxy-pt61262",
    'user':'iskidet',
    'password':'Ohikhuare1#',
     #account:'ocsp',
     # warehouse:'COMPUTE_WH',
    'database':'SAMPLESUPERSTORE',
    'role':"ACCOUNTADMIN",
     'schema':'PUBLIC',
    }
    session = Session.builder.configs(pars).create()
    
    @task(task_id='test')
    def callsql():
                
        sql= """ 
        select dname, sum(sal)
        from emp join dept on emp.deptno = dept.deptno
        where dname <> 'RESEARCH'
        group by dname
        order by dname
        """

        view = session.sql(sql).toPandas()
        print(view)

    # # you can execute SQL queries directly using the SQLExecuteQueryOperator
    # sql_test = SQLExecuteQueryOperator(
    #     task_id="test_create_or_replace_table",
    #     conn_id=_SNOWFLAKE_CONN_ID,
    #     database="DEMO_DB",
    #     sql=f""" SELECT 1
    #         """,
    # )

    # # you can execute SQL queries directly using the SQLExecuteQueryOperator
    # create_or_replace_table = SQLExecuteQueryOperator(
    #     task_id="create_or_replace_table",
    #     conn_id=_SNOWFLAKE_CONN_ID,
    #     database="DEMO_DB",
    #     sql=f"""
    #         CREATE OR REPLACE TABLE {_SNOWFLAKE_SCHEMA}.{_SNOWFLAKE_TABLE} (
    #             ID INT,
    #             NAME VARCHAR
    #         )
    #     """,
    # )

    # # you can also execute SQL queries from a file, make sure to add the path to the template_searchpath
    # insert_data = SQLExecuteQueryOperator(
    #     task_id="insert_data",
    #     conn_id=_SNOWFLAKE_CONN_ID,
    #     database=_SNOWFLAKE_DB,
    #     sql="insert_data.sql",
    #     params={
    #         "db_name": _SNOWFLAKE_DB,
    #         "schema_name": _SNOWFLAKE_SCHEMA,
    #         "table_name": _SNOWFLAKE_TABLE,
    #     },
    # )

    # # you can also execute multiple SQL statements using the SnowflakeSqlApiOperator
    # # make sure to set the statement_count parameter to the number of statements in the SQL file
    # # and that your connection details are in their proper capitalized form!
    # insert_data_multiple_statements = SnowflakeSqlApiOperator(
    #     task_id="insert_data_multiple_statements",
    #     snowflake_conn_id=_SNOWFLAKE_CONN_ID,
    #     sql="multiple_statements_query.sql",
    #     database=_SNOWFLAKE_DB,
    #     schema=_SNOWFLAKE_SCHEMA,
    #     params={
    #         "db_name": _SNOWFLAKE_DB,
    #         "schema_name": _SNOWFLAKE_SCHEMA,
    #         "table_name": _SNOWFLAKE_TABLE,
    #     },
    #     statement_count=2,  # needs to match the number of statements in the SQL file
    #     autocommit=True,
    # )

    # # use SQLCheck operators to check the quality of your data
    # data_quality_check = SQLColumnCheckOperator(
    #     task_id="data_quality_check",
    #     conn_id=_SNOWFLAKE_CONN_ID,
    #     database=_SNOWFLAKE_DB,
    #     table=f"{_SNOWFLAKE_SCHEMA}.{_SNOWFLAKE_TABLE}",
    #     column_mapping={
    #         "ID": {"null_check": {"equal_to": 0}, "distinct_check": {"geq_to": 3}}
    #     },
    # )

    chain(
        callsql()
        #create_or_replace_table
        # insert_data,
        # insert_data_multiple_statements,
        # data_quality_check,
    )


test_my_snowflake_dag()