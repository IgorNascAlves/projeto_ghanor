#!/bin/bash

# Script to start two programs from the projeto_ghanor directory

# Define the paths to the two directories
app_directory="App"
data_eng_directory="DataEng"

# Change directory to the App directory and activate its virtual environment
cd "$app_directory"
source .venv/bin/activate

# Run the main_script.py in the App directory in the background
python3.9 main_script.py &

# Change directory to the Data_eng directory and activate its virtual environment
cd "../$data_eng_directory"
source .venv/bin/activate

# Set the AIRFLOW_HOME environment variable and start airflow
export AIRFLOW_HOME="$(pwd)/airflow"
airflow standalone