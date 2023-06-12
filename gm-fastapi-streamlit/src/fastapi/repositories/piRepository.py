from sqlalchemy.orm import Session
from pydantic import BaseModel
from repositories.models.pi import DefaultPi, BronzeCuratedPi
from repositories.session import SessionLocal, get_db
from datetime import datetime, timedelta, date

class PiRepository():
    def __init__(self, db:Session):
        self.db = db
    
    def get_tag_name(self, tag_name: str): 
        # returns the first instance where the tag is found
        return self.db.query(DefaultPi).filter(DefaultPi.tag_name == tag_name).first()
    
    def get_all_data_for_tag(self, tag_name: str): 
        # declare column names to deal with deduplication
        return self.db.query(DefaultPi.tag_name, DefaultPi.timestamp, DefaultPi.value).filter(DefaultPi.tag_name == tag_name).all()
        

    def get_data_between_timerange(self, start_date: datetime, end_date: datetime): 
        print(start_date, "\n", end_date, "\n")
        return self.db.query(DefaultPi).filter(DefaultPi.timestamp >= start_date, DefaultPi.timestamp <= end_date).all()
    
    def get_most_recent(self): 
        # return the most record based recent date 
        return self.db.query(DefaultPi).filter(DefaultPi.timestamp.desc()).first()
    
    def get_last_n_hours(self, n: int): 
        # return the data from the last n hours 
        return self.db.query(DefaultPi).filter(DefaultPi.timestamp >= datetime.now() - timedelta(hours=n)).all()
    
    def get_from_start_date(self, start_date: date): 
        return self.db.query(DefaultPi).filter(DefaultPi.timestamp >= start_date).all()
    
    def get_all(self, skip: int=0, limit: int=100):
        # return all data
        return self.db.query(DefaultPi).offset(skip).limit(limit).all()
    