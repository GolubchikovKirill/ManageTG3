from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str
    API_ID: int
    API_HASH: str
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()