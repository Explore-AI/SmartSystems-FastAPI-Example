from sqlalchemy import Column, Integer, String, Date
from ..database import Base

class IdentityUser(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "Identity_DB"}

    userid = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))