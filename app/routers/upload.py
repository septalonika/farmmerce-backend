from fastapi import APIRouter, Depends, UploadFile
from app.views.user import UserView
from app.schemas.user_schema import UserCreate, UserUpdate, PasswordUpdate
from sqlalchemy.orm import Session
from app.instances.db_config import get_db
from app.settings import settings
from app.middleware.s3.uploadfile import upload_file, create_presigned_url
from app.views.upload import UploadView


upload_router = APIRouter(prefix="/api/v1/upload-file", tags=["users"])

@upload_router.post("/users/{user_id}")
def create_profile_image(uploaded_file: UploadFile, user_id: int, db: Session = Depends(get_db)):
    bucket_name = settings.AWS_S3_BUCKET_NAME
    response = upload_file(uploaded_file.file, bucket_name, object_name=uploaded_file.filename)
    status = response["success"]
    message = response["message"]

    if status == False:
        return {
            "message": message,
        }
    url = create_presigned_url(bucket_name=bucket_name, object_name=uploaded_file.filename, expiration=900)

    return UploadView().upload_file(user_id, url, db)