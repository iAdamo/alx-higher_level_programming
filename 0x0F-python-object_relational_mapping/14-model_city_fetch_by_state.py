#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
It takes 3 arguments: mysql username, mysql password and database name.
"""

# Only execute if the script is run directly (not imported)
if __name__ == "__main__":
    # Import necessary modules and classes
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from model_city import City

    # Check if the correct number of command-line arguments are provided
    if len(argv) != 4:
        print(f"Usage: {argv[0]} <username> <password> <database name>")
        exit(1)

    # Create a SQLAlchemy engine for the MySQL database
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}',
        pool_pre_ping=True
    )

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a new session for database interaction
    session = Session(engine)

    # Query all City and State objects, join on the State associated with
    # each City, and order by City.id
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print each city and its associated state
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session to free up resources
    session.close()
