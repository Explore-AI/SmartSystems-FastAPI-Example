"""

_summary_
include all versions of the table
"""
import os 
import sys 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from session import SessionLocal, Base, get_db, engine
import pandas as pd
from sqlalchemy import MetaData, Table, select, func, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect
from sqlalchemy import Column, Integer, Boolean, String, DateTime, Float, Numeric

# metadata = MetaData(bind=engine)
# pi_bronze_table = Table(
#     "bronze_curated_pi_15min_v2", 
#     metadata, 
#     autoload=True,
#     schema="smartvisualiser_dev.subscribed")

class DefaultPi(Base): 
    __tablename__ = "osi_pi_15min_v2"
    __table_args__ = {'schema': 'default'}
    tag_name = Column(String, primary_key=True)
    value=Column(Numeric(precision=11, scale=8))
    timestamp=Column(DateTime)

class BronzeCuratedPi(Base):
    __tablename__ = "bronze_curated_pi_15min_v2"
    __table_args__ = {'schema': 'subscribed'}
    ITEMS_Good=Column(Boolean)
    ITEMS_Questionable=Column(Boolean)
    ITEMS_Substituted=Column(Boolean)
    ITEMS_Timestamp=Column(DateTime)
    ITEMS_UnitsAbbreviation=Column(String)
    ITEMS_Value=Column(Numeric(precision=11, scale=8)) # move to the base class
    tag_name=Column(String, primary_key=True)   # move to a base class 
    FILE_NAME=Column(String) 
    TRIGGER=Column(String)
    TIMESTAMP=Column(DateTime) # base class variable
    YEAR=Column(Integer)
    MONTH=Column(Integer)
    DAY=Column(Integer)
    SCHEDULE_DATETIME=Column(DateTime)
    ACTUAL_DATETIME=Column(DateTime)

def main(): 
    # start the database session 
    db_session = SessionLocal()
    
    # last_row = db_session.query(BronzeCuratedPi).order_by(BronzeCuratedPi.TIMESTAMP.desc()).first()
    # print(last_row.TIMESTAMP, "\n", last_row.ACTUAL_DATETIME, "\n", last_row.tag_name)
    last_row = db_session.query(BronzeCuratedPi).order_by(BronzeCuratedPi.TIMESTAMP).first()
    print(last_row.TIMESTAMP, "\n", last_row.ACTUAL_DATETIME, "\n", last_row.tag_name)

    print("**************************************************")
    default_first_row = db_session.query(DefaultPi).order_by(DefaultPi.timestamp.desc()).first()
    print(f"Default Tag Name: {default_first_row.tag_name}")
    print(f"Default Value: {default_first_row.value}")
    print(f"Default Timestamp: {default_first_row.timestamp}")
    print("**************************************************")
    
if __name__ == '__main__':
    print("Making moves")
    main()