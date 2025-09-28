import boto3
import math
import os

# Initialize the S3 client
s3_client = boto3.client('s3')

# Set the necessary variables
bucket_name = 'my-bucket'
file_key = 'my-large-file'
file_path = 'path/to/your/large-file'
part_size = 5 * 1024 * 1024  # 5 MB part size
parts = []

# Step 1: Initiate the multipart upload
response = s3_client.create_multipart_upload(Bucket=bucket_name, Key=file_key)
upload_id = response['UploadId']

# Step 2: Upload each part
try:
    file_size = os.path.getsize(file_path)
    part_count = math.ceil(file_size / part_size)
    
    with open(file_path, 'rb') as f:
        for i in range(part_count):
            part_number = i + 1
            data = f.read(part_size)
            
            response = s3_client.upload_part(
                Bucket=bucket_name,
                Key=file_key,
                PartNumber=part_number,
                UploadId=upload_id,
                Body=data
            )
            
            parts.append({
                'PartNumber': part_number,
                'ETag': response['ETag']
            })
            print(f'Uploaded part {part_number}/{part_count}')

    # Step 3: Complete the multipart upload
    response = s3_client.complete_multipart_upload(
        Bucket=bucket_name,
        Key=file_key,
        UploadId=upload_id,
        MultipartUpload={'Parts': parts}
    )
    print('Multipart upload completed successfully!')

except Exception as e:
    # Abort the multipart upload if something goes wrong
    s3_client.abort_multipart_upload(Bucket=bucket_name, Key=file_key, UploadId=upload_id)
    print(f'Multipart upload aborted. Error: {e}')