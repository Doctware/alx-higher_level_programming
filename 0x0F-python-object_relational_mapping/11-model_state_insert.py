#!/usr/bin/python3
""" this module contains instruction thats add states obj
    from the given DB """
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
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # printing resulr
    print(new_state.id)

    # terminate sesion
    session.close()
