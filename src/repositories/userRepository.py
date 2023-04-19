from sqlalchemy.orm import Session
from .models.identityUser import IdentityUser

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: IdentityUser):
        db_user = IdentityUser(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_id(self, user_id: int):
        return self.db.query(IdentityUser).filter(IdentityUser.userId == user_id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(IdentityUser).filter(IdentityUser.email == email).first()

    def update_user(self, user: IdentityUser):
        db_user = self.get_user_by_id(user.userId)
        if not db_user:
            return None
        for key, value in user.dict().items():
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
