#!/usr/bin/python3

import pandas as pd

URI = 'http://www.celestrak.com/NORAD/elements/active.txt'

def main():
    data = pd.read_csv(URI, delimiter=',')
    data.to_json("satalite.json")
    # print(data.keys())
    for key in data.keys():
        print(key)
    # df = pd.DataFrame(data)
    # print(df)


if __name__ == "__main__":
    main()