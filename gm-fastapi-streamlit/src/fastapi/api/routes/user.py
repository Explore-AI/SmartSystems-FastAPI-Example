"""
!Development Build
Contains all of the FastAPI decorated routes for the Users app
"""
from typing import Any, Optional, Annotated, Union, Dict
from fastapi import APIRouter, Depends, HTTPException
from api.dependencies import get_db #DB dependency 
from sqlalchemy.orm import Session 
# import schema.user as User  # Pydantic model
from repositories.crud import user # CRUD services
from schema.user import UserBase, UserCreate, UserInDB, UserUpdate, UserInDBOut

router = APIRouter()

@router.get('/testroute/')
def get_test_route(db: Session = Depends(get_db)): 
    return {'message':'dependency included'} 

# Create User Route 
@router.post('/createuser/', response_model=Optional[UserBase])
def create_user(new_user: UserCreate, db: Session = Depends(get_db)):
    # add the user to the db 
    added_user = user.create_new_user(db=db, user_obj=new_user)
    
    if not added_user: 
        raise HTTPException(
            status_code=404, detail=f"User was not created successfully"
            )
    return UserBase(username=added_user.username, email=added_user.email, user_id=added_user.user_id)
    # after adding the user then return the user output

# Read User route 
@router.get('/{user_id}/getuser', response_model=Optional[UserBase])
def get_user(user_id: int, db: Session = Depends(get_db)): 
    user_db_model = user.get_user_by_id(db=db, user_id=user_id)
    if not user_db_model:
    # the exception is raised, not returned - you will get a validation
    # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"User with ID {user_id} not found"
            )
    return UserBase(username=user_db_model.username, email=user_db_model.email, user_id=user_db_model.user_id)
    # return {'message': f'Route used to get user base on the user id: {str(user_id)}'} 

# Update User information
@router.put('/{user_id}/update/', response_model=Optional[UserUpdate])
def update_user(user_id: int, user_in: Annotated[UserBase, Dict[str, Any]], db: Session = Depends(get_db)): 
    updated_user_db = user.update_user_by_id(db=db, user_id=user_id, user_obj=user_in)
    if not updated_user_db:
        raise HTTPException(
            status_code=404, detail=f"User not updated!"
            )
    
    # return updated user
    return updated_user_db 
    # return {'message':'user updated route'}

# Delete User route 
@router.delete('/{user_id}/delete/', response_model=Optional[UserBase])
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user_db = user.delete_user_by_id(db=db, user_id=user_id)
    if not deleted_user_db:
        raise HTTPException(
            status_code=404, detail=f"User not deleted!"
            )
    return deleted_user_db
    # return {'message':'user deleted route'}