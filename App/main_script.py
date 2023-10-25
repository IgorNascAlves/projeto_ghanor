import schedule
import time
import pandas as pd
import os
from flask import Flask, render_template
from data_updater_and_plotter import DataUpdaterAndPlotter

app = Flask(__name__)

def read_metas(raised_amount):
    #change to float 
    raised_amount = float(raised_amount)

    df = pd.read_csv('metas_segunda_fase.csv')
    #get the first row thats the value is lower than the raised amount

    #change columns meta to float
    df['Meta'] = df['Meta'].str.replace('.', '')
    df['Meta'] = df['Meta'].astype(float)

    df_last = df[df['Meta'] <= raised_amount]
    # #get the last row
    df_last = df_last.iloc[[-1]]

    last = df_last['Conteúdo Adicional'].values[0]
    last_value = df_last['Meta'].values[0]

    df_next = df[df['Meta'] >= raised_amount]

    df_next = df_next.iloc[[0]]

    next = df_next['Conteúdo Adicional'].values[0]
    next_value = df_next['Meta'].values[0]

    return {'last': last, 'next': next,
             'last_value': last_value, 'next_value': next_value,
               'falta': int(next_value - raised_amount)}

    

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
    conteudo = read_metas(raised_amount)
    return render_template('index.html', data=csv_data, image_url=plot_image_url, conteudo=conteudo)

if __name__ == "__main__":
    app.run(debug=True)
