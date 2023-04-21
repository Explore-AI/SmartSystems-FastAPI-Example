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

class ResponseUser(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True