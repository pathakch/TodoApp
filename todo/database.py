from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = 'postgresql://tododb_2f35_user:0nqzMXyHgoBGXKf8eGDLUsW0h8ugKrnc@dpg-d4kqkfs9c44c73f4saa0-a/tododb_2f35'
engine = create_engine(SQLALCHEMY_DATABASE_URL)


# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args= {'check_same_thread':False})

SessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base()