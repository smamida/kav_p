from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

with DAG(dag_id="Run-ls-Command", schedule_interval=None, catchup=False, start_date=days_ago(1)) as dag:
    ls_airflow_plugins = BashOperator(
        task_id="ls_airflow_plugins",
        bash_command="ls /usr/local/airflow/",
        dag=dag,
        priority_weight=300,
    )
    ls_local = BashOperator(
        task_id="ls_local",
        bash_command="ls /usr/local/customer_stored_env",
        dag=dag,
        priority_weight=300,
    )
    mwaa_local = BashOperator(
        task_id="mwaa_local",
        bash_command="ls /usr/local/customer_stored_env",
        dag=dag,
        priority_weight=300,
    )

    ls_airflow_plugins >> ls_local >> mwaa_local