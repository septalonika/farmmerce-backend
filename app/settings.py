from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    DATABASE_URL: str
    APP_NAME: str = "DefaultApp" 
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_S3_BUCKET_NAME: str
    AWS_REGION_NAME: str
    AWS_ENDPOINT_URL: str

    class Config:
        env_file = ".env"
        extra = "allow"  # agar tidak error dengan variabel tak dikenal

settings = Settings()
