#!/usr/bin/python3

import sqlite3
conn = sqlite3.connect('mytest.db')
print('db is open')

# one line entry
conn.execute("INSERT INTO GARDEN (COMMON,BOTANICAL,TYPE) VALUES ('Rhubarb','Rheum rhabarbarum', 'perennial' )")

# multi line entry
conn.execute('''
    INSERT INTO GARDEN (COMMON,BOTANICAL,TYPE)
    VALUES ('Zucchini', 'Cucurbita pepo', 'annual')
    ''')
conn.commit()
print('Garden items added to db!')
conn.close()
