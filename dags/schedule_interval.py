from airflow import DAG
from airflow.operators.dummy import DummyOperator

from datetime import datetime, timedelta

with DAG(dag_id="schedule_interval",
                schedule_interval= timedelta(days=1),
                start_date = datetime(2021, 1, 1)) as dag:
    
    task_1 = DummyOperator(
        task_id = "task_1"
    )

