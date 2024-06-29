#!/usr/bin/python3
""" This module contains an instruction that fetches cities by state """
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State, Base
from model_city import City

if __name__ == "__main__":
    username, password, database = sys.argv[1:]

    # Connecting to MySQL
    url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    engine = create_engine(url)

    # Creating session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Executing the query
    cities = session.query(City).join(State).order_by(City.id).all()

    # Printing the fetched result
    for city in cities:
        print(f'{city.state.name}: ({city.id}) {city.name}')

    # Terminating the session
    session.close()
