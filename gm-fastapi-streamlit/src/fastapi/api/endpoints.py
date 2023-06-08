from fastapi import APIRouter
# import api.routes.user as user
from api.routes.hsi import router as hsi_router
from api.routes.pi import router as pi_router
api_router = APIRouter()


@api_router.get("/")
async def read_root():
    return {'message': 'Our FastAPI Backend is available'}

# api_router.include_router(user.router, prefix="/user")
api_router.include_router(hsi_router, prefix="/hsi")
api_router.include_router(pi_router, prefix="/pi")


