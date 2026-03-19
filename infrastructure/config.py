from pydantic_settings import BaseSettings
from functools import lru_cache


class EnvironmentVariables(BaseSettings):
    DB_PASSWORD: str
    DB_LOGIN: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str
    
    class Config:
        env_file = ".env"

@lru_cache(maxsize=None)
def get_environment_variables() -> EnvironmentVariables:
    return EnvironmentVariables()