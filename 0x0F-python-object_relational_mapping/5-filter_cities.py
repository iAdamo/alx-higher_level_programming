#!/usr/bin/python3
""" script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
Use (source maintest/0-select_cities.sql) to load into the MySQL Server
Execute by (./5-filter_cities.py username password database_name statename)
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    ptr = db.cursor()
    ptr.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "INNER JOIN states ON cities.state_id = states.id "
                "WHERE states.name LIKE BINARY %s "
                "ORDER BY cities.id ASC", (argv[4],))
    rows = ptr.fetchall()
    for row in rows:
        print(row[1], end=", " if row != rows[-1] else "\n")
    ptr.close()
    db.close()
