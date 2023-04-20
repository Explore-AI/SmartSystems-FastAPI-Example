import fastapi
from fastapi.middleware.cors import CORSMiddleware
import api.endpoints as endpoints


def initialize_backend_application() -> fastapi.FastAPI:
    app = fastapi.FastAPI()

    #  add middleware eg. cors
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    #  add default route
    @app.get("/")
    def home():
        return {"message": "Server is running..."}

    #  add enpoints
    app.include_router(endpoints.router)

    return app


api: fastapi.FastAPI = initialize_backend_application()
