#!/usr/bin/python3
import sqlite3
conn = sqlite3.connect('mytest.db')
print("Garden database:\n")
curser = conn.execute("SELECT COMMON, BOTANICAL, TYPE from GARDEN")
for row in curser:
    print("COMMON name: ", row[0])
    print("BOTANICAL name: ", row[1])
    print("TYPE: ", row[2], "\n")

conn.close()