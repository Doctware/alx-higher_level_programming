#!/usr/bin/python3i
""" this module contains instruction thats print the given states obj
    from the given DB """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username, password, database, state_n = sys.argv[1:]

    # Connecting to mysql
    url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    engine = create_engine(url)

    # craete a configured sessin class
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # querying all state obj
    state = session.query(State).filter(State.name == state_n).first()

    # printing resulr
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # terminate sesion
    session.close()
