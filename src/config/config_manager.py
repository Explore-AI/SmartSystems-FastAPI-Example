from pydantic import BaseSettings, Field
from functools import lru_cache
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = Field(default='', env='SQLALCHEMY_DATABASE_URL')
    DEBUG: bool = Field(default= True, env='DEBUG')
    OPENAPI_CLIENT_ID: str = Field(default='', env='OPENAPI_CLIENT_ID')
    TENANT_ID: str = Field(default='', env='TENANT_ID')
    APP_CLIENT_ID: str = Field(default='', env='APP_CLIENT_ID')

    class Config:
        env_file = f".env.{os.getenv('ENVIRONMENT', 'dev')}"
        env_file_encoding = 'utf-8'  
        case_sensitive = True

@lru_cache(maxsize=50)
def get_settings() -> BaseSettings:
    return Settings()