import boto3
from botocore.exceptions import ClientError

# Replace 5-jan with your actual credentials (for demo/testing only)
AWS_ACCESS_KEY = 'AKIAEXAMPLE1234567890'
AWS_SECRET_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
GENERIC_API_Key = 'AKIAIOSFODNN7EXAMPLE'
Private_Key = '-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCAmMwggJfAgEAAoGBALeXAMPLEKEYDATA
...
...
-----END PRIVATE KEY-----'
REGION = 'us-east-1'
BUCKET_NAME = 'your-unique-bucket-name-12345'

def create_bucket():
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY,
            region_name=REGION
        )

        # Create the bucket
        s3.create_bucket(
            Bucket=BUCKET_NAME,
            CreateBucketConfiguration={'LocationConstraint': REGION}
        )
        print(f"✅ Bucket '{BUCKET_NAME}' created successfully in region '{REGION}'.")

    except ClientError as e:
        print(f"❌ Error creating bucket: {e}")

if __name__ == "__main__":
    create_bucket()
