import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbc import *

engine = create_engine('sqlite:///tutorial.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("rob888", "hihihi1995", "a")
session.add(user)


# commit the record the database
session.commit()

session.commit()