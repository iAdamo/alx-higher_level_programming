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
# block imports for main only
if __name__ != "__main__":
    exit()

# Import necessary modules
import MySQLdb
from sys import argv

# Connects to a MySQL server running on localhost at port 3306.
db = MySQLdb.connect(
    host='localhost',
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
    port=3306
)

# Creates a cursor handle
ptr = db.cursor()

# Executes the SQL query
ptr.execute('SELECT * FROM states ORDER BY id ASC')

# Fetches all rows from the result of the query
table = ptr.fetchall()

# Prints the rows
for row in table:
    print(row)

# Clean up
ptr.close()
db.close()
