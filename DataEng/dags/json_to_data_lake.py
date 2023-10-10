from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import json
import os

# Define your Airflow DAG
default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 7),
    'retries': 1,
}

dag = DAG(
    'json_to_local_folder',
    default_args=default_args,
    description='Retrieve JSON and save to a local folder',
    schedule_interval='* * * * *',  # Run every minute
    catchup=False,
    tags=['data_lake', 'bronze'],
)

# HTTP Request Operator to retrieve JSON data
http_task = SimpleHttpOperator(
    task_id='fetch_json_data',
    method='GET',
    http_conn_id='http_conn',  # Create an HTTP connection in Airflow UI with your base URL
    endpoint='/api/v1/projects/1/summary',
    dag=dag,
)

# Python Operator to save JSON data to a local folder
def save_to_local_folder(**kwargs):
    ti = kwargs['ti']
    response = ti.xcom_pull(task_ids='fetch_json_data')
    data = json.loads(response)

    # Replace 'your/local/folder' with your actual local folder path
    local_folder_path = 'datalake/bronze'
    os.makedirs(local_folder_path, exist_ok=True)

    # Generate a timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')

    # Create a file name with the timestamp
    file_name = f'data_{timestamp}.json'

    # # Check if the 'raisedAmount' field has changed compared to the last saved file
    # last_saved_file = os.path.join(local_folder_path, 'last_saved.json')
    # previous_data = {}
    # if os.path.exists(last_saved_file):
    #     with open(last_saved_file, 'r') as previous_file:
    #         previous_data = json.load(previous_file)
    
    with open(os.path.join(local_folder_path, file_name), 'w') as json_file:
        json.dump(data, json_file)

    # if data.get('raisedAmount') > previous_data.get('raisedAmount'):
    #     with open(os.path.join(local_folder_path, file_name), 'w') as json_file:
    #         json.dump(data, json_file)
        
    #     # Save the current data as the last saved file for future comparison
    #     with open(last_saved_file, 'w') as last_saved:
    #         json.dump(data, last_saved)

save_task = PythonOperator(
    task_id='save_to_local_folder',
    python_callable=save_to_local_folder,
    provide_context=True,
    dag=dag,
)

# Define the task dependencies
http_task >> save_task

if __name__ == "__main__":
    dag.cli()
