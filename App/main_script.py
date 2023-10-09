import schedule
import time
import os
from flask import Flask, render_template
from data_updater_and_plotter import DataUpdaterAndPlotter

app = Flask(__name__)

def update_data():
    url_to_ping = "https://api.ghanor.com.br/api/v1/projects/1/summary"
    csv_file_name = 'data.csv'
    plot_filename = 'static/plot.png'

    data_updater_and_plotter = DataUpdaterAndPlotter(url_to_ping, csv_file_name)
    data = data_updater_and_plotter.retrieve_data_from_url()

    if data:
        existing_data = data_updater_and_plotter.update_data_in_csv(data)
        # data_updater_and_plotter.plot_raised_amount_over_time()
        data_updater_and_plotter.save_plot(plot_filename)
        print(existing_data[-1])

update_data()
schedule.every(1).minute.do(update_data)

@app.route('/')
def index():
    update_data()
    csv_data = []  # Initialize as an empty list
    plot_image_url = 'static/plot.png'

    # Read existing data from CSV and display only the last 5 rows
    if os.path.exists('data.csv'):
        with open('data.csv', 'r') as csv_file:
            lines = csv_file.readlines()
            # Get only the last 5 rows
            last_5_lines = lines[-5:]
            for line in last_5_lines:
                date, raised_amount = line.strip().split(',')
                csv_data.append({'date': date, 'raised_amount': raised_amount})
    
    # Sort the list from last to first
    csv_data = sorted(csv_data, key=lambda x: x['date'], reverse=True)

    return render_template('index.html', data=csv_data, image_url=plot_image_url)

if __name__ == "__main__":
    app.run(debug=True)
