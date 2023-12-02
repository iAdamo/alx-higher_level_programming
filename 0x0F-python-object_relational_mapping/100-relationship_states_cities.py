#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_state import Base, State
    from relationship_city import City
    
    engine = create_engine(
        f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}",
        pool_pre_ping=True
        )
    
    Base.metadata.create_all(engine)
    
    session = Session(engine)
    
    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)
    session.add(new_state)
    session.add(new_city)
    session.commit()
    
    # Query the State and City objects
    state_city = session.query(State, City).filter(State.id == City.state_id).first()

    # Check if the state and city were found
    if state_city is not None:
        # Unpack the tuple
        state, city = state_city
        print(f"State: {state.name}, City: {city.name}")
    
    session.close()
    
    
    
    