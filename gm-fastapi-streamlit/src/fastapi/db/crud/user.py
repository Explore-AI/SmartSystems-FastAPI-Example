"""
    !Development Build
    CRUD operations for the Users Database
    
"""
from typing import Any, Dict, Optional, Generic, Union, Annotated
from sqlalchemy.orm import Session
from models.user import User
from schema.user import UserCreate, UserUpdate
from fastapi.encoders import jsonable_encoder

# TODO: Create a production ready hasher to include with 
# mock password hasher 
def password_hasher(password: str) -> str: 
    return "h4$h"+password
    
# CREATE USER 
def create_new_user(db:Session, user_obj: UserCreate) -> User: 
    db_user = User(
        username=user_obj.username,
        email=user_obj.email,
        hashed_password=password_hasher(user_obj.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# READ USER DATA 
def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.user_id == user_id).first()

# UPDATE USER DATA
def update_user_by_id(db:Session, user_id:int, user_obj: Annotated[UserUpdate, Dict[str, Any]]) -> User: 
    user = db.query(User).filter(User.user_id == user_id).first()
    json_data = jsonable_encoder(user) 
    if not user: # user not found 
        return None
    # check if object is dict
    if isinstance(user_obj, dict): 
        new_data = user_obj
    else:
        new_data = user_obj.dict(exclude_unset=True)
    
    for field in json_data: 
        if field in new_data: 
            setattr(user,field, new_data[field])
    
    db.commit()
    db.refresh(user)
    
    return user     
#DELETE USER DATA
def delete_user_by_id(db:Session, user_id: int) -> User: 
    user = db.query(User).filter(User.user_id == user_id).first()
    db.delete(user)
    db.commit()
    return user
    

