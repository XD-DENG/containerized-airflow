from builtins import range
from datetime import timedelta
import time

from airflow.models import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

args = {
    'owner': 'Airflow',
    'start_date': days_ago(2),
}

dag = DAG(
    dag_id='demo_dag',
    default_args=args,
    schedule_interval='0 0 * * *',
    dagrun_timeout=timedelta(minutes=60),
    tags=['Demo']
)


file_check_task = FileSensor(
    task_id='check_existence_of_flag_file',
    filepath='/usr/local/airflow/flag.txt',
    poke_interval=5,
    dag=dag,
)

db_task = PostgresOperator(
    task_id='create_new_table',
    sql=f'create table t{int(time.time())} (name varchar(10))',
    postgres_conn_id='postgres_default',
    dag=dag,
)

bash_task = BashOperator(
    task_id='bash_command',
    bash_command='echo "Hello! Are You Coughing?"',
    dag=dag,
)

def my_py_function(input):
    """This is a function that will run within the DAG execution"""
    return input * 2

python_task = PythonOperator(
        task_id='python_task',
        python_callable=my_py_function,
        op_kwargs={'input': "No I'm not coughing"},
        dag=dag,
    )


file_check_task >> db_task
db_task >> bash_task
db_task >> python_task