from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import json
import os
import pandas as pd

# Define your Airflow DAG
default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 10, 7),
    'retries': 1,
}

dag = DAG(
    'json_to_local_folder_and_csv',
    default_args=default_args,
    description='Retrieve JSON and save to a local folder and CSV',
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

    # if data.get('raisedAmount') > previous_data.get('raisedAmount'):
    #     with open(os.path.join(local_folder_path, file_name), 'w') as json_file:
    #         json.dump(data, json_file)
        
    #     # Save the current data as the last saved file for future comparison
    #     with open(last_saved_file, 'w') as last_saved:
    #         json.dump(data, last_saved)

    # Save all the data    
    with open(os.path.join(local_folder_path, file_name), 'w') as json_file:
        json.dump(data, json_file)

save_task = PythonOperator(
    task_id='save_to_local_folder',
    python_callable=save_to_local_folder,
    provide_context=True,
    dag=dag,
)

# Python Operator to process existing JSON files and create a CSV
def process_json_files():
    input_dir = 'datalake/bronze'
    output_csv_file = 'datalake/silver/data.csv'
    columns = ["targetAmount", "raisedAmount", "supporters", "targetDate"]

    data = []

    for filename in os.listdir(input_dir):
        if filename.startswith('data') and filename.endswith('.json'):
            with open(os.path.join(input_dir, filename), 'r') as file:
                json_data = json.load(file)
                row = [json_data[column] for column in columns]
                data.append(row)

    if data:
        df = pd.DataFrame(data, columns=columns)
        df.to_csv(output_csv_file, index=False)

process_json_task = PythonOperator(
    task_id='process_json_files',
    python_callable=process_json_files,
    dag=dag,
)

# Define the task dependencies
http_task >> save_task >> process_json_task

if __name__ == "__main__":
    dag.cli()
