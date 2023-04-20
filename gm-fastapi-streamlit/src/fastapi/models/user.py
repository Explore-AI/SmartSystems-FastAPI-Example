"""
!Development Build
Our user models are found here 
We inherit from the Base class 
"""
from sqlalchemy import Column, String, Integer 
from db.session import Base 

class User(Base): 
    """_summary_
    The different columns for the User model are: 
    - user id: Int
    - first name: varchar | string
    - last name varchar | string
    - email varchar | EmailStr
    - password (hashed)
    - description
    Args:
        Base (_type_): _description_
    
    """
    __tablename__ = 'UsersTable'
    # __table_args__ = {"schema": "UsersApp_DB"}
    
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    hashed_password=Column(String(50), nullable=False)
    bio=Column(String(500), nullable=True)
