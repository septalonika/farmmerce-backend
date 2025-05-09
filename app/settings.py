from pydantic_settings import BaseSettings
from typing import Optional
class Settings(BaseSettings):
    DATABASE_URL: str
    APP_NAME: str = "DefaultApp" 
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    AWS_S3_BUCKET_NAME: Optional[str] = None
    AWS_REGION_NAME: Optional[str] = None 
    AWS_ENDPOINT_URL: Optional[str] = None
    RAJA_ONGKIR_API_KEY: Optional[str] = None

    class Config:
        env_file = ".env"
        extra = "allow"  # agar tidak error dengan variabel tak dikenal

settings = Settings()
