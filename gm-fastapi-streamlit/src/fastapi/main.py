"""
!Development Build
"""
import fastapi 
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
# from repositories.session import SessionLocal
from api.endpoints import api_router
# from api.dependencies import get_db

def initialize_backend_application() -> fastapi.FastAPI:
    app = fastapi.FastAPI()
    # add middleware 
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # add routes
    app.include_router(api_router)
    
    return app

api: fastapi.FastAPI = initialize_backend_application()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:api", host="0.0.0.0", port=8001, reload=True, log_level="info")
