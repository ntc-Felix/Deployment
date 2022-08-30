from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from airflow.models.baseoperator import chain, cross_downstream

from airflow.utils.dates import days_ago

from datetime import datetime, timedelta


default_args = {
                "retry":5,
                "retry_delay": timedelta(minutes=5)
                }


def _downloading_data(**kwargs):
    print(kwargs)


def _checking_data():
    print("check data")


with DAG(dag_id="defining_dependencies",
                schedule_interval= "@daily",
                catchup=False,
                start_date = days_ago(3),
                default_args=default_args,
                max_active_runs=1) as dag:
    
    downloading_data = PythonOperator(
        task_id = "downloading_data",
        python_callable = _downloading_data
    )

    checking_data = PythonOperator(
        task_id="checking_data",
        python_callable= _checking_data
    )

    waiting_for_data = FileSensor(
        task_id = "waiting_for_data",
        fs_conn_id='fs_default',
        filepath='my_file.txt'
    )

    processing_data = BashOperator(
        task_id ="processing_data",
        bash_command="exit 0"
    )

chain(downloading_data, waiting_for_data, processing_data)