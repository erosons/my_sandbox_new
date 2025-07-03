from airflow.models import XCom
from datetime import datetime, timedelta, timezone
from airflow.operators.python_operator import PythonOperator


logging.basicConfig(
    filename="new.log",
    filemode="w",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

with DAG(dag_id="cleanup_xcom_demo", schedule_interval=None, start_date=days_ago(2)) as dag:

    @provide_session
    def cleanup_xcom(session=None):
        ts_limit = datetime.now(timezone.utc) - timedelta(days=2)
        session.query(XCom).filter(XCom.execution_date <= ts_limit).delete()
        logging.info(f"deleted all XCOMs older than {ts_limit}")

    xcom_cleaner = PythonOperator(
        task_id='delete-old-xcoms',
        python_callable=cleanup_xcom)

    xcom_cleaner 
