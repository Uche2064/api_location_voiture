from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    db_name: str
    db_username: str
    db_host: str
    db_port: int
    db_password: str
    secret_key: str
    algorithm: str
    expiration_time: int

    class Config:
        env_file = ".env"


setting = Setting()