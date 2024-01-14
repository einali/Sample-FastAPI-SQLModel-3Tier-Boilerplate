
from pydantic_settings import BaseSettings,SettingsConfigDict

class Setting(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    PROJECT_NAME : str ="Very Simple FastAPI Project Boilerplate"
    CORS_ORIGINS: str ="localhost"

    PG_DRIVERNAME : str="postgresql+psycopg"
    PG_DBNAME : str
    PG_USER : str
    PG_PASSWORD  : str
    PG_HOST : str
    PG_PORT : int




project_setting=Setting()