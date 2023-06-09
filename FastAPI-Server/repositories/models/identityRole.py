from sqlalchemy import Column, Integer, String,Date
from ..database import Base

class IdentityRole(Base):
    __tablename__ = "IdentityRoles"
    __table_args__ = {"schema": "dbo"}
    
    roleid = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer, index=True)
    rolename = Column(String(50), unique=True, index=True)
    datecreated = Column(Date)
