from fastapi import APIRouter
from .routes import users, authentication, hsi

apiRouter = APIRouter()
authRouter = APIRouter(tags=["authentication"])

apiRouter.include_router(users.router)
apiRouter.include_router(hsi.router, prefix="/hsi", tags=["hsi"])
authRouter.include_router(authentication.router)