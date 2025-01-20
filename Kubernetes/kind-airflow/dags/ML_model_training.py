from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

# Define the DAG
with DAG(
    'databricks_job_workflow',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    # Task A: Preprocess data in Databricks (DatabricksSubmitRunOperator)
    preprocess_data = DatabricksSubmitRunOperator(
        task_id='preprocess_data',
        databricks_conn_id='databricks_default',
        existing_cluster_id='<cluster-id>',
        notebook_task={
            'notebook_path': '/path/to/databricks/notebook_preprocess',
        },
    )

    # Task B: Train the machine learning model in Databricks (DatabricksSubmitRunOperator)
    train_model = DatabricksSubmitRunOperator(
        task_id='train_model',
        databricks_conn_id='databricks_default',
        existing_cluster_id='<cluster-id>',
        notebook_task={
            'notebook_path': '/path/to/databricks/notebook_train_model',
        },
    )

    # Task C: Evaluate the model's performance in Databricks (DatabricksSubmitRunOperator)
    evaluate_model = DatabricksSubmitRunOperator(
        task_id='evaluate_model',
        databricks_conn_id='databricks_default',
        existing_cluster_id='<cluster-id>',
        notebook_task={
            'notebook_path': '/path/to/databricks/notebook_evaluate_model',
        },
    )

    # Task D: Store the results in the data warehouse (e.g., Snowflake) using KubernetesPodOperator
    store_results = KubernetesPodOperator(
        task_id="store_results",
        namespace="airflow",
        image="python:3.8",
        cmds=["bash", "-c"],
        arguments=[
            """
            pip install snowflake-connector-python &&
            python -c '
            import snowflake.connector
            conn = snowflake.connector.connect(
                user="your_user",
                password="your_password",
                account="your_account",
                warehouse="your_warehouse",
                database="your_database",
                schema="your_schema"
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO results_table VALUES (...)")
            '
            """
        ],
        name="store-results-pod",
        is_delete_operator_pod=True,
        in_cluster=True,
        resources={
            "request_cpu": "500m",
            "request_memory": "1Gi",
            "limit_cpu": "1",
            "limit_memory": "2Gi",
        },
    )

    # Task Dependencies
    preprocess_data >> train_model >> evaluate_model >> store_results
