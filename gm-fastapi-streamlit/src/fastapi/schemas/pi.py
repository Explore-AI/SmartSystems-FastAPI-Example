from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from repositories.models.pi import DefaultPi


class BasePi(BaseModel): 
    TagName: str
    Value: float 
    TimeStamp: datetime 
    
    class Config: 
        orm_mode = True


class Pi: 
    TagName: str 
    Value: float
    TimeStamp: datetime
    
    def __init__(self, pi_db: Optional[DefaultPi] = None) -> None:
        if pi_db:
            self.TagName = pi_db.tag_name
            self.Value = pi_db.value
            self.TimeStamp = pi_db.timestamp
            
    def __repr__(self) -> str:
        return f"Pi(TagName='{self.TagName}', Value='{self.Value}', TimeStamp='{self.TimeStamp}')"
    
    @classmethod 
    def from_db(cls, inst): 
        return cls(pi_db=inst)