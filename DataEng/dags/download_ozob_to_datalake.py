from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import json
import os
import pandas as pd

# Argumentos padrão para a DAG
default_args = {
    'owner': 'V_CYBER',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 10),
    'retries': 1,
}

# Definição da DAG
dag = DAG(
    'json_to_local_and_csv_dag_pledgeLevels',
    default_args=default_args,
    description='DAG to fetch JSON data from ordersReport and pledgeLevels and save to local folder and CSV',
    schedule_interval='@daily',  # Executa diariamente
    catchup=False,
    tags=['data_lake', 'bronze', 'silver'],
)

# Task para coletar dados do endpoint ordersReport via requisição HTTP
http_orders_report_task = SimpleHttpOperator(
    task_id='fetch_orders_report',
    method='GET',
    http_conn_id='http_conn',  # Defina a conexão HTTP no Airflow UI com sua URL base
    endpoint='/api/ordersReport/1',  # O endpoint da API para ordersReport
    dag=dag,
)

# Task para coletar dados do endpoint pledgeLevels via requisição HTTP
http_pledge_levels_task = SimpleHttpOperator(
    task_id='fetch_pledge_levels',
    method='GET',
    http_conn_id='http_conn',  # Defina a conexão HTTP no Airflow UI com sua URL base
    endpoint='/api/projects/1/pledgeLevels',  # O endpoint da API para pledgeLevels
    dag=dag,
)

# Função Python para salvar os dados JSON localmente
def save_to_local_folder(**kwargs):
    ti = kwargs['ti']
    response = ti.xcom_pull(task_ids=kwargs['task_id_to_pull'])
    data = json.loads(response)  # Converte o conteúdo JSON

    # Define o caminho local onde salvar os dados
    local_folder_path = kwargs['local_path']
    os.makedirs(local_folder_path, exist_ok=True)  # Cria o diretório, se não existir

    # Gera um timestamp para o nome do arquivo
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    file_name = f'data_{timestamp}.json'

    # Salva os dados JSON no arquivo local
    with open(os.path.join(local_folder_path, file_name), 'w') as json_file:
        json.dump(data, json_file)

# Tasks para salvar ordersReport e pledgeLevels no local
save_orders_report_task = PythonOperator(
    task_id='save_orders_report_to_local_folder',
    python_callable=save_to_local_folder,
    op_kwargs={'task_id_to_pull': 'fetch_orders_report', 'local_path': 'datalake/bronze/ozob/ordersReport'},
    provide_context=True,
    dag=dag,
)

save_pledge_levels_task = PythonOperator(
    task_id='save_pledge_levels_to_local_folder',
    python_callable=save_to_local_folder,
    op_kwargs={'task_id_to_pull': 'fetch_pledge_levels', 'local_path': 'datalake/bronze/ozob/pledgeLevels'},
    provide_context=True,
    dag=dag,
)

# Define as dependências entre as tasks
http_orders_report_task >> save_orders_report_task 
http_pledge_levels_task >> save_pledge_levels_task

if __name__ == "__main__":
    dag.cli()
