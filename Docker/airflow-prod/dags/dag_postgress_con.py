"""This helps reduce our line of codes using dag decorators."""
from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago


args = {
    "owner": "Samson",
    "start_date": datetime(2022,8,16),
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
    "owner": "Samson"
}

# We are trying to backfill the missed schedule run which was 2022-08-01
# IF using a container,exec in the container or run directly on CLI
# from cli -> airflow dags backfill -s 2022-08-01 -e 2022-08-16

with DAG(
    dag_id="Postgres_interaction",
    schedule_interval="@daily",
    tags=["Connection to PostgresDB"],
    default_args=args,
    catchup=False
) as dag :
    

    create_tablejob=PostgresOperator(
        task_id="create_table_Ops",
        postgres_conn_id="postgres_conn",
        sql="""
            Create table if not exists dag_runs(
                dt date,
                dag_id character varying,
                primary key(dt,dag_id)
            ) """,
        dag=dag


    )

    delete_tablejob=PostgresOperator(
        task_id="delete_Ops",
        postgres_conn_id="postgres_conn",
        sql="""
            delete from dag_runs where dag_id ='{{dag.dag_id}}'
            """,
        dag=dag
     )
    
   # Note the {{ds}} , {{dag_id}} in two curly bracket are the internal macros for airflow see docs.
    insert_tablejob=PostgresOperator(
        task_id="insert_Ops",
        postgres_conn_id="postgres_conn",
        sql="""
            insert into dag_runs (dt,dag_id) values('{{ds}}','{{dag.dag_id}}')
            """,
        dag=dag
     )
    
    create_tablejob >> delete_tablejob >> insert_tablejob
