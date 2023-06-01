import fastapi
from fastapi import APIRouter, Depends
from typing import Optional, Sequence
from config import config_manager as config
from fastapi.middleware.cors import CORSMiddleware
from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer
from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer

class AppStartUpExtensions(fastapi.FastAPI):

    def AddCorsMiddleware(self):
        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def AddSwaggerUIAuth(self, redirecturl:str, clientid:str):
        self.swagger_ui_oauth2_redirect_url = redirecturl
        self.swagger_ui_init_oauth = {
             "usePkceWithAuthorizationCodeGrant": True,
            "clientId": clientid
        }

    def CreateSingleTenantAzureAuthScheme(self, clientId:str, tenantId:str, scopes: Optional[dict[str,str]] = None):
        return SingleTenantAzureAuthorizationCodeBearer(
                    app_client_id = clientId,
                    tenant_id = tenantId,
                    scopes = scopes,
                    allow_guest_users=True
                )

    def AddDefaultEndpoint(self, message:str): 
        @self.get("/")
        def home():
            return {"message": f"{message}..."}

    def AddApiRouters(self, routers:list[APIRouter], dependencies:Optional[Sequence[Depends]]):
        for router in routers:
            if "authentication" in router.tags:
                self.include_router(router)
            else:
                self.include_router(router, dependencies= dependencies)







