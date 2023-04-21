from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from domain.security.jwt import jwt_generator
from domain.security.password import pwd_generator
from domain.schemas.identityUser import SignInUser as User ,SignUpUser
from repositories.database import get_db
from repositories.models.identityUser import IdentityUser
from services.usersService import UserService
from domain.security.hash import HashGenerator

router = APIRouter()

# Dependency to get a user service instance
def get_user_service(db: Session = Depends(get_db)):
    return UserService(db)

@router.post("/Auth/signup")
async def signup(user: SignUpUser, service: UserService = Depends(get_user_service)):
    """
    Sign up a new user.
    """
    # Check if the user already exists
    if service.get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    # Hash the user password
    hashed_password = pwd_generator.generate_hashed_password(pwd_generator.generate_salt, user.password)
    # Create a new identity user with the hashed password
    identity_user = IdentityUser(
        email=user.email,
        username=user.username,
        PasswordHash=hashed_password,
        PasswordSalt=pwd_generator.generate_salt)
    # Save the user to the database
    new_user = service.create_user(identity_user)
    # Generate a JWT token for the new user
    access_token = jwt_generator.create_access_token_for_user(new_user)
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/Auth/signin")
async def signin(form_data: User, service: UserService = Depends(get_user_service)):
    """
    Sign in an existing user.
    """
    # Check if the user exists
    identity_user = service.get_user_by_email(form_data.Email)
    if not identity_user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    # Check if the password is correct
    if not pwd_generator.is_password_authenticated(
            hash_salt=identity_user.PasswordSalt,
            password= form_data.Password, 
            hashed_password= identity_user.PasswordHash):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    # Generate a JWT token for the user
    access_token = jwt_generator.create_access_token_for_user(identity_user)
    return {"access_token": access_token, "token_type": "bearer"}
