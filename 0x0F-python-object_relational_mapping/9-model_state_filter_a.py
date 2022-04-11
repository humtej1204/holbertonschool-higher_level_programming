#!/usr/bin/python3
"""Initialize"""
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    """
    Conecting database and queering
    """
    sql = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(sql.format(argv[1],
                                      argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    try:
        for id, name in session.query(State.id, State.name).order_by(State.id):
            if 'a' in name:
                print("{}: {}".format(id, name))
    except Exception:
        print("Nothing")
    session.close()
