"""
!Development Build
our dependencies go here
"""
from typing import Generator 
from repositories.session import SessionLocal
from fastapi import Depends
from sqlalchemy.orm import Session
from repositories.hsiRepository import HSIRepository

# Our DB Session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# our HSI repository dependency 
def get_hsi_repository(db:Session=Depends(get_db)):
    return HSIRepository(db)
