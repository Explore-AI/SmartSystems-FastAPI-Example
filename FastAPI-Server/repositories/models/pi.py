"""

_summary_
include all versions of the table
"""
# import os 
# import sys 
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))

from repositories.sqlwh_session import Base, SessionLocal
from sqlalchemy import (Boolean, Column, DateTime, Integer,
                        Numeric, String)

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