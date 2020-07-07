#!/usr/bin/ python3
'''Author: Michael Lennerblom
   Description: Basic weather app, expanding upon learnings from building graphs with matlotlib and using the OpenWeather API
'''

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

# using dotenv to hide api key in .env file
load_dotenv()

WEATHER_KEY = os.getenv("WEATHER_KEY")

def main():
    zip_code = input("Please enter a 5 digit zipcode\n")
    weather_uri = f'http://api.openweathermap.org/data/2.5/forecast?zip={zip_code},us&units=imperial&appid={WEATHER_KEY}'

    r = requests.get(weather_uri)
    fiveday = r.json()
    city = fiveday['city']['name']
    lat = fiveday['city']['coord']['lat']
    lon = fiveday['city']['coord']['lon']

    onecall_uri  = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=imperial&exclude=current,minute,hourly&appid={WEATHER_KEY}'

    req = requests.get(onecall_uri)
    weather_data = req.json()

    weather = weather_data['daily']

    # Assign the current and upcoming days and weather to the graph labels list
    labels = []
    for data in weather:
        # Convert Epoch time into a usable string date
        day = pd.Timestamp.fromtimestamp(data['dt']).strftime('%Y-%m-%d')
        # Convert date into day of the week
        df = pd.Timestamp(day)
        weekday = df.day_name()
        # Add days of the week and main weather to labels list
        labels.append(f"{weekday}\n{data['weather'][0]['main']}")

    # Assign the current and upcoming day high/low temperatures to the min/max lists
    min_temp = []
    max_temp = []
    for temp in weather:
        min_temp.append(temp['temp']['min'])
        max_temp.append(temp['temp']['max'])

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x + width/2, min_temp, width, label='low', facecolor='b')
    rects2 = ax.bar(x - width/2, max_temp, width, label='high', facecolor='r')
    # Adding labels to axis' and bars
    ax.set_ylabel('Degrees Ferenheit')
    ax.set_title(f'High Temperatures for {city}')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
            xy=(rect.get_x() + rect.get_width() / 2, height),
            xytext=(0, 3),  # 3 points vertical offset
            textcoords="offset points",
            ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()

    plt.show()

if __name__ == "__main__":
    main()