#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
    The script takes 3 arguments: mysql username, mysql password and database
    name (no argument validation needed)
    Use the module MySQLdb (import MySQLdb)
    Connect to a MySQL server running on localhost at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    The code should not be executed when imported
Use `source maintest/0-select_states.sql` to load into the MySQL Server
Execute by ./0-select_states.py root root hbtn_0e_0_usa
"""
if __name__ != "__main__":
    exit()

import MySQLdb
from sys import argv

db = MySQLdb.connect(
    host='localhost',
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
    port=3306
)

ptr = db.cursor()

ptr.execute('SELECT * FROM states ORDER BY id ASC')

table = ptr.fetchall()

for row in table:
    print(row)

ptr.close()
db.close()
