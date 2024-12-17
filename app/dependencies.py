from app.utils.smtp_connection import SMTPClient
from pydantic_settings import BaseSettings, SettingsConfigDict

# Settings class for reading environment variables
class Settings(BaseSettings):
    mail_username: str
    mail_password: str
    mail_server: str
    mail_port: int
    mail_use_tls: bool

    model_config = SettingsConfigDict(env_file=".env", extra="allow")

settings = Settings()

def get_settings():
    return settings

def get_email_service():
    return SMTPClient(
        server=settings.mail_server,
        port=settings.mail_port,
        username=settings.mail_username,
        password=settings.mail_password
    )
