#!/usr/bin/python3
"""
A script to prints the first State object from the database
hbtn_0e_6"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    is_here = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print('{}'.format(state.id))
            is_here = True
            break
    if is_here is False:
            print('Not found')