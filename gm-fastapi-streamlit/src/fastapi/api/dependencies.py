"""
!Development Build
our dependencies go here
"""
from typing import Generator 
from db.session import SessionLocal

# Our DB Session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
