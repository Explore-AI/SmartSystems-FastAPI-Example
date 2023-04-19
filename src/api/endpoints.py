from fastapi import APIRouter
from .routes import users

router = APIRouter()

router.include_router(users.router)