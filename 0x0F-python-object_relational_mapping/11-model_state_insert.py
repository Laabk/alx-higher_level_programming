#!/usr/bin/python3
"""
this a script to prints the first State object from the database
hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    n_state = State(name="Louisiana")
    session.add(newstate)
    session.commit()
    print(n_state.id)
    session.close()
