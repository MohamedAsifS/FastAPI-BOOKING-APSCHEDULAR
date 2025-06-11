from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from environs import Env

env=Env()
env.read_env()



database_url=env("DATABASE_URL")

engine=create_engine(database_url,connect_args={"check_same_thread":False})
session=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()

def get_db():
    connection=session()
    try:
        yield connection 
    finally:
        connection.close()
