#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the db hbtn_0e_6_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    # Check if the number of arguments is correct
    if len(sys.argv) != 4:
        print('Usage: argv[0] <username> <password> <database>',
              file=sys.stderr)
        exit()

    # Create a SQLAlchemy engine that provides a source of database
    # connectivity
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],  # username
            sys.argv[2],  # password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True
    )

    # Create all tables in the engine ("Base.metadata.create_all" is akin to
    # "CREATE TABLE" statement in raw SQL)
    Base.metadata.create_all(engine)

    # Create a new session
    session = Session(engine)

    # Query the State table
    states_table = session.query(State).all()

    # Loop through each row in the table
    for each_row in states_table:
        # Print the id and name of the state
        if 'a' in each_row.name:
            print(f"{each_row.id}: {each_row.name}")

    # Close the session
    session.close()
