import boto3
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region=None):
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        print(f"✅ Bucket '{bucket_name}' created successfully attempt1.")
    except ClientError as e:
        print(f"❌ Error: {e}")

# Example usage
create_s3_bucket('my-unique-bucket-name-12345', region='us-east-1')
