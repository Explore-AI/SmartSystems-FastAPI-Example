""" 
!Development Build
Instantiates our SQL session that connects the user to 
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from sqlalchemy import MetaData

import os
from dotenv import load_dotenv
load_dotenv = load_dotenv()

hostname=os.environ.get("DB_SQLWH_HOST") 
token=os.environ.get("DB_SQLWH_TOKEN")
http_path=os.environ.get("DB_SQLWH_HTTP_PATH")
port=443
schema = "subscribed"
catalog="smartvisualiser_dev"

# SQLALCHEMY_DATABASE_URL = "mssql+pymssql://sa:%s@mssql:1433/UsersApp_DB"%quote_plus("Change@Me123")
SQLALCHEMY_DATABASE_URL = "mssql+pymssql://IdentityAdmin:%s@smart-systems.database.windows.net:1433/Identity_db"%quote_plus("Password@12") # azure development server
DATABRICKS_URL = f"databricks://token:{token}@{hostname}:{port}/?http_path={http_path}&catalog={catalog}"

engine = create_engine(DATABRICKS_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
