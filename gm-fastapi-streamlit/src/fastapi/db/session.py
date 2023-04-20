""" 
!Development Build
Instantiates our SQL session 
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

SQLALCHEMY_DATABASE_URL = "mssql+pymssql://sa:%s@mssql:1433/UsersApp_DB"%quote_plus("Change@Me123")
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 