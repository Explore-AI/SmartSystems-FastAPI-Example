from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

#Remote Azure DbServer: 
SQLALCHEMY_DATABASE_URL = "mssql+pymssql://IdentityAdmin:%s@smart-systems.database.windows.net:1433/Identity_db"%quote_plus("Password@12")
#SQLALCHEMY_DATABASE_URL = "mssql+pymssql://sa:%s@mssql:1433/Identity_DB"%quote_plus("Passw@rd")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()