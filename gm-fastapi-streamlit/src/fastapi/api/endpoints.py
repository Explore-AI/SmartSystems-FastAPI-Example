from fastapi import APIRouter
import api.routes.user as user
api_router = APIRouter()


@api_router.get("/")
async def read_root():
    return {'message': 'Our FastAPI Backend is available'}

api_router.include_router(user.router, prefix="/user")
