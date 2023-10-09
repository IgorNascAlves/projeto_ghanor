import requests
import csv
from datetime import datetime, timedelta
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class DataUpdaterAndPlotter:
    def __init__(self, url, csv_filename, desired_utc_offset_hours=-3):
        self.url = url
        self.csv_filename = csv_filename
        self.desired_utc_offset = timedelta(hours=desired_utc_offset_hours)

    def get_current_utc_time(self):
        return datetime.utcnow()

    def adjust_utc_time(self, utc_time):
        return utc_time + self.desired_utc_offset

    def format_datetime_str(self, datetime_obj):
        return datetime_obj.strftime("%Y-%m-%d %H:%M:%S")

    def retrieve_data_from_url(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Failed to retrieve data. Status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    def update_data_in_csv(self, data):
        current_utc_time = self.get_current_utc_time()
        current_desired_time = self.adjust_utc_time(current_utc_time)
        current_datetime_str = self.format_datetime_str(current_desired_time)

        existing_data = []
        file_exists = os.path.isfile(self.csv_filename)

        if file_exists:
            with open(self.csv_filename, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    existing_data.append(row)

        if len(existing_data) > 1 and existing_data[-1][1] != str(data['raisedAmount']):
            current_datetime_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_row = [current_datetime_str, str(data['raisedAmount'])]
            existing_data.append(new_row)
            with open(self.csv_filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(existing_data)

        elif not file_exists or len(existing_data) <= 1:
            with open(self.csv_filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                if not file_exists:
                    csv_writer.writerow(['DateTime', 'RaisedAmount'])
                csv_writer.writerow([current_datetime_str, str(data['raisedAmount'])])

        print("Data saved successfully.")
        return existing_data

    def save_plot(self, filename):
        date_list = []
        raised_amount_list = []

        with open(self.csv_filename, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                date_list.append(datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S"))
                raised_amount_list.append(float(row[1]))

        plt.figure(figsize=(12, 6))
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
        plt.plot(date_list, raised_amount_list, marker='o', linestyle='-')
        plt.xlabel("Date and Time")
        plt.ylabel("Raised Amount")
        plt.title("Raised Amount Over Time")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # Save the plot to the specified filename
        plt.savefig(filename)
        plt.close()

    # Modify the plot_raised_amount_over_time method
    def plot_raised_amount_over_time(self):
        self.save_plot("plot.png")  # Save the plot as "plot.png" by default