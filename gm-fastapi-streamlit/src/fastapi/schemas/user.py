"""
! Development Build
We will create Pydantic models for reading/writing data from our various API endpoints.
These models will be provided in this schema's file
"""
from pydantic import BaseModel, EmailStr
from typing import Optional

# Base User schema, always returned by the API 
class UserBase(BaseModel): 
    username: str
    email: str
    
# create a new user (username, email, password all required)
class UserCreate(UserBase): 
    password: str  
    email: str
    username: str
    # first_name: str = ""
    # last_name: str =""

# updating the user information 
class UserUpdate(UserBase): 
    first_name: str
    last_name: str
    username: str 
    email: str 
    bio: str = None
    
# create base instance for the user in the DB 
class UserInDBBase(UserBase): 
    user_id: int = None
    class Config: 
        orm_mode = True 
        
# additional properties stored in the DB but not returned by the API 
class UserInDB(UserInDBBase):
    hashed_password: str  
    
class UserInDBOut(UserInDB): 
    first_name: str 
    last_name: str 
    email: str
      
