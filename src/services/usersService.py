from sqlalchemy.orm import Session
from repository.models.identityUser import IdentityUser
from repository import userRepository

class UserService:
    def __init__(self, db: Session):
        self.user_repository =  userRepository(db)

    def create_user(self, user: IdentityUser):
        return self.user_repository.create_user(user)

    def get_user_by_id(self, user_id: int):
        return self.user_repository.get_user_by_id(user_id)

    def get_user_by_email(self, email: str):
        return self.user_repository.get_user_by_email(email)

    def update_user(self, user: IdentityUser):
        return self.user_repository.update_user(user)

    def delete_user(self, user_id: int):
        return self.user_repository.delete_user(user_id)
