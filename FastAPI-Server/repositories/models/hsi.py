# Model for the bronze_curated_hsi_15min_v2 table found in the databricks sql warehouse
"""
Date Created: 2023-06-07 16:25
"""
# import os 
# import sys 
# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(os.path.dirname(SCRIPT_DIR))
from repositories.sqlwh_session import Base
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