#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa
Use (source maintest/0-select_cities.sql) to load into the MySQL Server
Execute by (./4-cities_by_state.py username password database_name)
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
                "ORDER BY cities.id ASC")
    rows = ptr.fetchall()
    for row in rows:
        print(row)
    ptr.close()
    db.close()
