#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database
Using module SQLAlchemy
"""

if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    from sqlalchemy.engine.url import URL
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    db = {'drivername': 'mysql+mysqldb',
          'host': 'localhost',
          'port': '3306',
          'username': argv[1],
          'password': argv[2],
          'database': argv[3]}

    url = URL(**db)
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    sobj = (argv[4], )
    try:
        state = session.query(State).filter(State.name == sobj).one_or_none()
        print("{}".format(state.id))
    except:
        print("Not found")
