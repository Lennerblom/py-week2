#!/usr/bin/env python3
""" Author: RZFeeser || Alta3 Research
Gather data returned by various APIs published on OMDB, and cache in a local SQLite DB
"""

import json
import sqlite3
import requests

# Define the base URL
OMDBURL = "http://www.omdbapi.com/?"

# search for all movies containing string
def movielookup(mykey, searchstring):
    try:
        ## open URL to return 200 response
        resp = requests.get(f"{OMDBURL}apikey={mykey}&s={searchstring}")
        ## read the file-like object decode JSON to Python data structure
        return resp.json()
    except:
        return False

def trackmeplease(datatotrack):
    conn = sqlite3.connect('mymovie.db')
    try:
        conn.execute('''CREATE TABLE IF NOT EXISTS MOVIES (TITLE TEXT PRIMARY KEY NOT NULL, YEAR INT  NOT NULL);''')

        # loop through the list of movies that was passed in
        for data in datatotrack:
            conn.execute("INSERT INTO MOVIES (TITLE,YEAR) VALUES (?,?)",(data.get("Title"), data.get("Year")))
            conn.commit()

        print("Database operation done")
        conn.close()
        return True
    except:
        return False

# Read in API key for OMDB
def harvestkey():
# TODO:
# To have success with this lab, you'll need to go to https://www.omdbapi.com/apikey.aspx and sign up for an API key. Be sure to only sign up for a FREE account.
    with open("/home/student/omdb.key") as apikeyfile:
        return apikeyfile.read().rstrip("\n") # grab the api key out of omdb.key

def printlocaldb():
    pass
    #cursor = conn.execute("SELECT * from MOVIES")
    #for row in cursor:
    #    print("MOVIE = ", row[0])
    #    print("YEAR = ", row[1])


def main():

    print("Particulating Splines...")

    # read the API key out of a file in the home directory
    mykey = harvestkey()

    # initialize answer
    answer = "go"

    while True:
        answer = ""
        while answer == "":
            print("""\n**** Welcome to the OMDB Movie Client and DB ****
            ** Returned data will be written into the local database **
            1) Search for All Movies Containing String
            2)
            99) Exit""")

            answer = input("> ")

        if answer == "1":
            searchstring = input("Search all movies in the OMDB. Enter search string: ")
            resp = movielookup(mykey, searchstring)["Search"]
            if resp:
                # display the results
                print(resp)
                # write the results into the database
                trackmeplease(resp)
            else:
                print("That search did not return any results.")


        elif answer == "99":
            print("See you next time!")
            break

if __name__ == "__main__":
    main()

# TODO:
# Run your code.

# student@beachhead:~/pyapi/apisqlite$ python3 apisqlite01.py

# Try running the script a few times. Search for a few different movies.

# Ensure the sqlite3 client is installed with apt

# student@beachhead:~/pyapi/apisqlite$ sudo apt install sqlite3

# Connect to the SQL database client. Information on the client can be found here: https://sqlite.org/cli.html Note: If you get stuck in this client, press CTRL + D

# student@beachhead:~/pyapi/apisqlite$ sqlite3

# Open your database file, mymovie.db

# sqlite> .open mymovie.db

# Get the tables within mymovie.db

# sqlite> .tables

# Select all of the data in the table, and display it on the screen.

# sqlite> .dump

# Exit the SQL database client.

# sqlite> .quit

# CODE CUSTOMIZATION 01 - After reviewing the API usage on https://www.omdbapi.com/. Add an "option 2" that allows a search by "type".

# CODE CUSTOMIZATION 02 - After reviewing the API usage on https://www.omdbapi.com/. Add an "option 3" that allows a search by "year of release".

# CODE CUSTOMIZATION 03 - After reviewing the API usage on https://www.omdbapi.com/. Add an "option 4" that allows a search by both "type" and "year of release".

# CODE CUSTOMIZATION 04 - Add an "option 5" that displays the contents of the LOCAL database.

# CODE CUSTOMIZATION 05 - Replace the CLI User Interface with a User Interface provided by Flask. All of the same "options" should be available via HTTP GET's to your local Flask server.