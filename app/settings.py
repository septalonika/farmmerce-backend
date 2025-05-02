from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    DATABASE_URL: str
    APP_NAME: str = "DefaultApp"  # opsional jika tidak penting

    class Config:
        env_file = ".env"
        extra = "allow"  # agar tidak error dengan variabel tak dikenal

settings = Settings()
