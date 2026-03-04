import boto3
import os
import uuid
from botocore.exceptions import BotoCoreError, ClientError

AWS_ACCESS_KEY_ID = "AKIA3OPND7VSXWK3KYMR"
AWS_SECRET_ACCESS_KEY = "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"
AWS_REGION = "ap-south-1"
AWS_S3_BUCKET = "amzn-s3-bucket-trsmallproperties"

s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION,
)


def upload_file_to_s3(file_obj, filename: str, content_type: str) -> str:
    try:
        unique_name = f"properties/{uuid.uuid4()}-{filename}"

        s3_client.upload_fileobj(
            file_obj,
            AWS_S3_BUCKET,
            unique_name,
            ExtraArgs={
                "ContentType": content_type,
                # "ACL": "public-read",  # remove if bucket is private
            },
        )

        file_url = f"https://{AWS_S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{unique_name}"
        return file_url

    except (BotoCoreError, ClientError) as e:
        raise Exception(f"S3 upload failed: {str(e)}")