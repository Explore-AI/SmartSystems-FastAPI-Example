# services for HSI data

from datetime import datetime, timedelta

from pydantic import BaseModel
from repositories.models.hsi import BronzeCuratedHSI, DefaultHSI
from repositories.sqlwh_session import SessionLocal, get_db
from sqlalchemy.orm import Session


class HSIRepository(): 
    def __init__(self, db: Session):
        self.db = db
        
    def get_id(self, id: int):
        # return the data from the requested id
        return self.db.query(DefaultHSI).filter(DefaultHSI.Id == id).first()

    def get_below_threshold(self, threshold: float):
        # return the data below the threshold
        return self.db.query(DefaultHSI).filter(DefaultHSI.Value < threshold).all()

    def get_above_threshold(self, threshold: float):
        # return the data above the threshold
        return self.db.query(DefaultHSI).filter(DefaultHSI.Value > threshold).all()
    
    def get_between_timestamps(self,  start_timestamp: datetime, end_timestamp: datetime): 
        # return the data between startdate and end date
        return self.db.query(DefaultHSI).filter(DefaultHSI.enqueuedTime >= start_timestamp).filter(DefaultHSI.enqueuedTime <= end_timestamp)

    def get_last_n_hours(self, n: int):
        # return the data from the last n hours
        current_time = datetime.now()
        datetime_n_hours_ago = current_time - timedelta(hours=n)
        
        return self.db.query(DefaultHSI).filter(DefaultHSI.enqueuedTime >= datetime_n_hours_ago).all()
    
    def get_all(self, skip: int=0, limit: int=100):
        # return all data
        return self.db.query(DefaultHSI).offset(skip).limit(limit).all()