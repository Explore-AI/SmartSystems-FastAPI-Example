# Model for the bronze_curated_hsi_15min_v2 table found in the databricks sql warehouse
"""
Date Created: 2023-06-07 16:25
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
from sqlalchemy import Column, Integer, Boolean, String, DateTime, Float, Numeric, BIGINT


class DefaultHSI(Base): 
    __tablename__ = "clearscada_hsi_data"
    __table_args__ = {'schema': 'default'}
    Id=Column(BIGINT, primary_key=True)
    Value=Column(Numeric(precision=32, scale=16))
    enqueuedTime = Column(DateTime)
    
    def __repr__(self):
        return f"Id: {self.Id} Value: {self.Value} enqueuedTime: {self.enqueuedTime}"


class BronzeCuratedHSI(Base): 
    # 146  GB
    __tablename__ = 'bronze_curated_hsi_data'
    __table_args__ = {'schema': 'subscribed'}
    TimeYear=Column(Integer)
    TimeMonth=Column(Integer)
    TimeDay=Column(Integer)
    SystemName=Column(String)
    enqueuedTime=Column(DateTime)
    StartDate=Column(DateTime)
    EndDate=Column(DateTime)
    FileName=Column(String)
    Fullname=Column(String)
    Id=Column(BIGINT, primary_key=True)
    Quality=Column(String)
    Reason=Column(Integer)
    State=Column(String)
    Time=Column(DateTime)
    Value=Column(Numeric(precision=32, scale=16))
    Units=Column(String)
    

def main(): 
    # start the database session 
    db_session = SessionLocal()
    
    # last_row = db_session.query(BaseHSI).order_by(BaseHSI.EndDate.desc()).first()
    # print(last_row.TIMESTAMP, "\n", last_row.ACTUAL_DATETIME, "\n", last_row.tag_name)
    
    first_row = db_session.query(BronzeCuratedHSI).first()
    print(f"StarDate:{first_row.StartDate}")
    print(f"EndDate:{first_row.EndDate}")
    print(f"FileName:{first_row.FileName}")
    print(f"Value:{first_row.Value} \nUnits:{first_row.Units}")
    print("_______________________________")
    first_row_default = db_session.query(DefaultHSI).first()
    print(f"Default Id: {first_row_default.Id}")
    print(f"Default Value: {first_row_default.Value}")
    
if __name__ == '__main__':
    print("HSI Model")
    main()