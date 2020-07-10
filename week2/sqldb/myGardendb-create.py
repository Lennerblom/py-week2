#!/usr/bin/python3

import sqlite3
conn = sqlite3.connect('mytest.db')
print('Database is open')

conn.execute("CREATE TABLE GARDEN (COMMON TEXT NOT NULL, BOTANICAL TEXT NOT NULL, TYPE TEXT NOT NULL);")
print('Table created!')

conn.close()