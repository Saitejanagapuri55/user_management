from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    mail_username: str
    mail_password: str
    mail_server: str
    mail_port: int
    mail_use_tls: bool

    # Allow environment variables to be read
    model_config = SettingsConfigDict(env_file=".env", extra="allow")

settings = Settings()
