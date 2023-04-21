from fastapi import APIRouter
from .routes import users, authentication

router = APIRouter()

router.include_router(users.router)
router.include_router(authentication.router)