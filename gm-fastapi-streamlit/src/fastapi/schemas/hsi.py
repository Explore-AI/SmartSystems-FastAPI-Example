from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from repositories.models.hsi import DefaultHSI

class BaseHSI(BaseModel): 
    Id: int 
    Value: float 
    enqueuedTime: datetime
    
    class Config: 
        orm_mode = True
        
class HSI:
    Id: int 
    Value: float
    enqueuedTime: datetime
    
    def __init__(self, hsi_db: DefaultHSI):
        self.Id = hsi_db.Id
        self.Value = hsi_db.Value
        self.enqueuedTime = hsi_db.enqueuedTime
    
    def __repr__(self):
        return f"HSI(Id={self.Id}, Value={self.Value}, enqueuedTime={self.enqueuedTime})"
    
    @classmethod
    def from_db(cls, inst):
        return cls(hsi_db = inst)
# Create different models for the different tables present in SQL warehouse