import os
from pydantic_settings import BaseSettings, SettingsConfigDict

environment = os.getenv("ENVIRONMENT", "dev")
env_file_path = (
    os.path.join(os.path.dirname(__file__), "../../environments/.dev.env")
    if environment == "dev"
    else os.path.join(os.path.dirname(__file__), "../../environments/.prod.env")
)


class Settings(BaseSettings):
    app_name: str = "day-finance"
    environment: str
    app_port: int

    postgres_db_host: str
    postgres_db_port: int
    postgres_db_name: str
    postgres_db_user: str
    postgres_db_password: str

    model_config = SettingsConfigDict(env_file=env_file_path)


settings = Settings()
