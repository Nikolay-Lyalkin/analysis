from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_port: str
    db_password: str
    db_name: str
    project_name: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
