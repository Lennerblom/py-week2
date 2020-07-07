#!/usr/bin/python3

import pandas as pd
import requests

URI = "httpS://statsapi.web.nhl.com/api/v1/teams"

def main():
    r = requests.get(URI)
    nhl = r.json()
    for team in nhl['teams']:
        print(team['name'])

    
    nhl_data = pd.read_json(URI)
    nhl_data.to_csv("nhl_data.csv")

if __name__ == "__main__":
    main() 