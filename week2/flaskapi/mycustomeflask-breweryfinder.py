#!/usr/bin/python3
from flask import Flask 
from flask import render_template
from flask import request
import sqlite3
import pandas as pd
import requests

BASE_URI = "https://api.openbrewerydb.org/breweries"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("brewhome.html")

@app.route("/brewlist")
def brewlist():
    con = sqlite3.connect("brewery.db")
    con.row_factory = sqlite3.Row
    
    cur = con.cursor()
    cur.execute("select * from BREWERIES")
    
    rows = cur.fetchall();
    return render_template("brewlist.html", rows = rows)

@app.route("/city/<city_name>")
def city(city_name):
    URI = f'{BASE_URI}?by_city={city_name}'
    r = requests.get(URI)
    brewery_data = r.json()
    brewery = []
    for brew in brewery_data:
        brewery.append(f"{brew['name']}, {brew['website_url']}")

    return render_template("brewery.html", city=city_name, brewery=brewery)

@app.route("/addreq",methods = ["POST", "GET"])
def addreq():
    if request.method == "POST":
        try:
            city = request.form["city"]
            name = []
            street = []
            web = []
            URI = f'{BASE_URI}?by_city={city}'
            r = requests.get(URI)
            brewery_data = r.json()
            for brew in brewery_data:
                name.append(brew['name'])
                street.append(brew['street'])
                web.append(brew['website_url'])

            con = sqlite3.connect('brewery.db')
            cur = con.cursor() 
            con.execute('''CREATE TABLE IF NOT EXISTS BREWERIES
            (NAME        TEXT    NOT NULL,
            STREET        TEXT    NOT NULL,
            WEB             TEXT NOT NULL);''')
            cur = con.cursor() 

            for i in range(len(brewery_data)):
                cur.execute("INSERT INTO BREWERIES (NAME,STREET,WEB) VALUES (?,?,?)",
                (name[i],street[i],web[i]))
                con.commit()
                msg = "Brewery added to db!"
            con.close()
        except:
            # con.rollback()
            msg = "error in insert operation"
       
        finally:
            return render_template("brewlist.html",msg = msg)
            
    

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application