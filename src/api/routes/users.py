from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import domain.schemas.identityUser as schemas
import repositories.models.identityUser as models
import services.usersService as services
from repositories.database import SessionLocal, engine


router = APIRouter()

# Dependency to get a database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Dependency to get a user service instance
def get_user_service(db: Session = Depends(get_db)):
    return services.UserService(db)

@router.post("/users", response_model=schemas.IdentityUser)
def create_user(user: schemas.IdentityUser, service: services.UserService = Depends(get_user_service)):
    db_user = models.IdentityUser(**user.dict())
    created_user = service.create_user(db_user)
    return created_user

@router.get("/users/{user_id}", response_model=schemas.IdentityUser)
def read_user(user_id: int, service: services.UserService = Depends(get_user_service)):
    db_user = service.get_user_by_id(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/users/{user_id}", response_model=schemas.IdentityUser)
def update_user(user_id: int, user: schemas.IdentityUser, service: services.UserService = Depends(get_user_service)):
    db_user = service.get_user_by_id(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user_data = user.dict(exclude_unset=True)
    updated_user = models.IdentityUser(**updated_user_data)
    return service.update_user(user_id, updated_user)

@router.delete("/users/{user_id}")
def delete_user(user_id: int, service: services.UserService = Depends(get_user_service)):
    db_user = service.get_user_by_id(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    service.delete_user(user_id)
    return {"message": "User deleted successfully"}
