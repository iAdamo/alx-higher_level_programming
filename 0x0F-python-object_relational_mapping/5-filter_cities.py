#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.
It is executed by running: ./5-filter_cities.py username password database_name
statename
"""

# This condition ensures the code only runs when the script is run directly,
# not when imported
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Check if the number of arguments is correct
    if len(argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> <database> "
              "<state name>")
        exit(1)

    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],  # username from command line argument
        passwd=argv[2],  # password from command line argument
        db=argv[3]  # database name from command line argument
    )

    # Create a cursor object to interact with the database
    ptr = db.cursor()

    # Execute a SQL query to fetch cities from a specific state
    ptr.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "INNER JOIN states ON cities.state_id = states.id "
                "WHERE states.name LIKE BINARY %s "
                "ORDER BY cities.id ASC", (argv[4],))  # state name from CL arg

    # Fetch all rows returned by the query
    rows = ptr.fetchall()

    # Loop through each row
    for row in rows:
        # Print the city name (second element in the row)
        # If it's the last row, end with a newline, otherwise end with a comma
        # and space
        print(row[1], end=", " if row != rows[-1] else "\n")

    # Close the cursor and the database connection
    ptr.close()
    db.close()
