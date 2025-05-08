from fastapi import HTTPException
import boto3
from botocore.exceptions import ClientError
from app.settings import settings

s3_client = boto3.client('s3', 
                         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                         region_name=settings.AWS_REGION_NAME,
                         endpoint_url=settings.AWS_ENDPOINT_URL), 

def upload_file(file, bucket, object_name=None):
    try:
        #if S3 object was not specified, use file_name
        if object_name is None:
            object_name = file

        # Upload the file
        s3_client[0].upload_fileobj(file, bucket, object_name)
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "success": True, 
        "message": "File uploaded successfully",
        "object_name": object_name,
        "status": 200
        }

def create_presigned_url(bucket_name, object_name, expiration=900):
    try:
        response = s3_client[0].generate_presigned_url('get_object',
                                                    Params={
                                                        'Bucket': bucket_name, 
                                                        'Key': object_name
                                                        },
                                                    ExpiresIn=expiration)
    except ClientError as e:
        raise HTTPException(status_code=500, detail=str(e))

    return response