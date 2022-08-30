from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta


default_args = {
                "retry":5,
                "retry_delay": timedelta(minutes=5)
                }


def _downloading_data(**kwargs):
    print(kwargs)


with DAG(dag_id="pythonoperator_example",
                schedule_interval= "@daily",
                catchup=False,
                start_date = days_ago(3),
                default_args=default_args,
                max_active_runs=1) as dag:
    
    downloading_data = PythonOperator(
        task_id = "downloading_data",
        python_callable = _downloading_data
    )