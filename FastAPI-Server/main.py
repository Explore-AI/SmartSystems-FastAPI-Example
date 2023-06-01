import fastapi
import api.endpoints as endpoints
import uvicorn
from config import config_manager
from domain.extensions.app_startup import AppStartUpExtensions


def initialize_backend_application() -> fastapi.FastAPI:

    app = fastapi.FastAPI()
    settings = config_manager.get_settings()

    #  add middleware 
    AppStartUpExtensions.AddCorsMiddleware(app)
    AppStartUpExtensions.AddSwaggerUIAuth(app, '/oauth2-redirect', settings.OPENAPI_CLIENT_ID)
    
    AppStartUpExtensions.AddDefaultEndpoint(app, message="Server is running")

    azure_Auth_scheme = AppStartUpExtensions.CreateSingleTenantAzureAuthScheme(
        app, 
        settings.APP_CLIENT_ID, 
        settings.TENANT_ID,
        { f'api://{settings.APP_CLIENT_ID}/user_impersonation': 'user_impersonation',}
    )

    #  add enpoints 
    AppStartUpExtensions.AddApiRouters(
        app,
        [endpoints.authRouter,endpoints.apiRouter],
        dependencies=[fastapi.Security(azure_Auth_scheme)]
    )

    @app.on_event('startup')
    async def load_config() -> None:
        await azure_Auth_scheme.openid_config.load_config()

    return app

api: fastapi.FastAPI = initialize_backend_application()

if __name__ == "__main__":
    uvicorn.run(app = api, host="0.0.0.0", port=8000)