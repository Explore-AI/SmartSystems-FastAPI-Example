from sqlalchemy import Column, Integer, String, Date
from ..database import Base

class IdentityUser(Base):
    __tablename__ = "IdentityUsers"
    __table_args__ = {"schema": "dbo"}

    Id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    PasswordHash = Column(String(255))
    PasswordSalt = Column(String(255))