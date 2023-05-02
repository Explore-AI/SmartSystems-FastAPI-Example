from fastapi import APIRouter
from .routes import users, authentication

apiRouter = APIRouter()
authRouter = APIRouter(tags=["authentication"])

apiRouter.include_router(users.router)
authRouter.include_router(authentication.router)