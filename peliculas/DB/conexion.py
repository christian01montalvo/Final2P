import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dbName = "peliculas.sqlite"


base_dir = os.path.dirname(os.path.realpath(__file__))
dbURL = f"sqlite:///{os.path.join(base_dir, dbName)}"


engine = create_engine(dbURL, echo=True)


Session = sessionmaker(bind=engine)


Base = declarative_base()