#!/usr/bin/python3
from flask import Flask 
from flask import render_template
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()
import requests

WEATHER_KEY = os.getenv("WEATHER_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return "Homepage"

@app.route("/city/<city_name>")
def city(city_name):
    # weather_data = pd.read_json(URI)
    URI = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid={WEATHER_KEY}'

    r = requests.get(URI)
    weather_data = r.json()
    main_weather = weather_data['weather'][0]['description']
    current_temp = weather_data['main']['temp']
    return render_template("wednesday.html", weather=main_weather, temp=current_temp, city=city_name)
    

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application


