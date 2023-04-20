from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

#connect to a database server 
SQLALCHEMY_DATABASE_URL = "mssql+pymssql://IdentityAdmin:%s@smart-systems.database.windows.net:1433/Identity_db"%quote_plus("PReplaceme@12")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)
