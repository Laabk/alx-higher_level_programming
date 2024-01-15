#!/usr/bin/python3
"""
A script that prints all City objects
from the database `hbtn_0e_14
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    res = session.query(City, State).join(State, City.state_id == State.id)

    for city, state in res.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
