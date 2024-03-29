#!/usr/bin/python3

"""
A script to lists all State objects
from the database `hbtn_0e_6_
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
    state_name = session.query(State).order_by(State.id).all()
    for i in state_name:
        print(f"{i.id}: {i.name}")
