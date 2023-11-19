#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
Use `source maintest/0-select_states.sql` to load into the MySQL Server
Execute by ./0-select_states.py username password database_name
"""
# Import necessary modules
import MySQLdb
from sys import argv

# make sure the code is not executed when imported
if __name__ == "__main__":
    exit()

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
rows = ptr.fetchall()

# Prints the rows
for row in rows:
    print(row)

# Clean up
ptr.close()
db.close()
