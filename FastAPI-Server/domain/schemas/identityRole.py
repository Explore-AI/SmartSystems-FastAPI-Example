from pydantic import BaseModel
import datetime

class IdentityRole(BaseModel):
    roleId: int
    userId: int 
    roleName: str
    createdDate: datetime.date

    class Config:
        orm_mode = True