from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from .models.identityUser import IdentityUser
from typing import List

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: IdentityUser):
       # db_user = IdentityUser(**user.dict())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_id(self, user_id: int):
        return self.db.query(IdentityUser).filter(IdentityUser.Id == user_id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(IdentityUser).filter(IdentityUser.email == email).first()

    def update_user(self, user: IdentityUser):
        db_user = self.get_user_by_id(user.Id)
        if not db_user:
            return None
        user_data = jsonable_encoder(user)
        for key, value in user_data.items():
             setattr(db_user, key, value)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        db_user = self.get_user_by_id(user_id)
        if not db_user:
            return None
        self.db.delete(db_user)
        self.db.commit()
        return db_user
    
    def get_all_users(self) -> List[IdentityUser]:
        return self.db.query(IdentityUser)

    def is_username_taken(self, username: str) -> bool:
        return self.db.query(IdentityUser).filter(IdentityUser.userName == username).count() > 0

    def is_email_taken(self, email: str) -> bool:
        return self.db.query(IdentityUser).filter(IdentityUser.email == email).count() > 0
