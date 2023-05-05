from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlalchemy.orm import Session
import domain.schemas.identityUser as schemas
import repositories.models.identityUser as models
import services.usersService as services
from repositories.database import SessionLocal, engine, get_db
from domain.security.jwt import jwt_generator
from .authentication import authorised_user

# Add global Dependency "authorised_user" to secure all endpoints with basic authentication
# dependencies=[Depends(authorised_user)]
router = APIRouter(prefix="/users", tags=["users"])

# Dependency to get a user service instance
def get_user_service(db: Session = Depends(get_db)):
    return services.UserService(db)

@router.get("")
def read_all_users(service: services.UserService = Depends(get_user_service)):
    db_users = service.get_all_users()
    if db_users is None:
        return None
    return db_users

@router.get("/{user_id}")
def read_user(user_id: int, service: services.UserService = Depends(get_user_service)):
    db_user = service.get_user_by_id(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}")
def update_user(user_id: int, user: schemas.IdentityUser, service: services.UserService = Depends(get_user_service)):
    db_user = service.get_user_by_id(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user_data = user.dict(exclude_unset=True)
    updated_user = models.IdentityUser(**updated_user_data)
    return service.update_user( updated_user)