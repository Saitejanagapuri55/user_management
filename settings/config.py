from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    mail_username: str = Field(..., env="MAIL_USERNAME")
    mail_password: str = Field(..., env="MAIL_PASSWORD")
    mail_server: str = Field(..., env="MAIL_SERVER")
    mail_port: int = Field(..., env="MAIL_PORT")
    mail_use_tls: bool = Field(..., env="MAIL_USE_TLS")

    class Config:
        env_file = ".env"
        extra = "allow"  # Allow extra environment variables if present


# Instantiate settings
settings = Settings()
