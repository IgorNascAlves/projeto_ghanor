import json
import csv
import os

# Define the input JSON file paths
ordem_json_path = 'DataEng/datalake/bronze/project_contributions_per_day_ordem.json'
nerdcastrpg_json_path = 'DataEng/datalake/bronze/project_contributions_per_day_nerdcastrpg.json'

# Define the output CSV file paths
ordem_csv_path = 'DataEng/datalake/silver/project_contributions_per_day_ordem.csv'
nerdcastrpg_csv_path = 'DataEng/datalake/silver/project_contributions_per_day_nerdcastrpg.csv'

def json_to_csv(json_path, csv_path):
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    
    with open(csv_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write the header row with the selected columns
        header = ['paid_at', 'created_at', 'total', 'total_amount']
        writer.writerow(header)
        
        # Write the data rows with the selected columns from the "source" list
        for entry in data:
            for source_entry in entry.get('source', []):  # Access the "source" list
                row = [source_entry.get('paid_at', ''), source_entry.get('created_at', ''), source_entry.get('total', ''), source_entry.get('total_amount', '')]
                writer.writerow(row)

# Convert the JSON files to CSV files
json_to_csv(ordem_json_path, ordem_csv_path)
json_to_csv(nerdcastrpg_json_path, nerdcastrpg_csv_path)

print(f'CSV files saved to {ordem_csv_path} and {nerdcastrpg_csv_path}')
