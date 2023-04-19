from pydantic import BaseModel

class IdentityUser(BaseModel):
    userId: int
    userName: str
    email: str

    class Config:
        orm_mode = True