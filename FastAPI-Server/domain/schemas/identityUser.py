from pydantic import BaseModel
from typing import Optional


class IdentityUser(BaseModel):
    Id: int
    username: str
    email: str
    PasswordHash: Optional[str] = None

    class Config:
        orm_mode = True

class SignInUser(BaseModel):
    Email: str
    Password: str

    class Config:
        orm_mode = True

class SignUpUser(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

class IdentityUserDTO:
    UserId: int
    UserName: str
    Email: str

    def __init__(self, UserId, UserName, Email):
        self.UserId = UserId
        self.UserName = UserName
        self.Email = Email

    def __repr__(self):
        return 'B({0.UserId!r},{0.UserName!r}, {0.Email!r})'.format(self)

    @classmethod
    def from_db(cls, inst):
        return cls(UserId = inst.Id, UserName = inst.username, Email = inst.email)

