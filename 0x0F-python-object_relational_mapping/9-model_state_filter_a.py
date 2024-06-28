#!/usr/bin/python3
""" this module contains instruction thats list the given states obj
    which contains 'a' from the given DB """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username, password, database = sys.argv[1:]

    # Connecting to mysql
    url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    engine = create_engine(url)

    # craete a configured sessin class
    Session = sessionmaker(bind=engine)

    # create a session
    session = Session()

    # querying all state obj
    states = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id).all()

    # printing resulr
    for state in states:
        print(f"{state.id}: {state.name}")

    # terminate sesion
    session.close()
