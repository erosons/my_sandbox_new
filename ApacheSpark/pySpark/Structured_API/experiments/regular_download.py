import boto3
import timeit

def download_file_from_s3(bucket_name, s3_object_key, local_file_path):
    s3 = boto3.client('s3')
    s3.download_file(Bucket=bucket_name, Key=s3_object_key, Filename=local_file_path)

if __name__ == "__main__":
    bucket_name = 'dbtlearn-sam'
    s3_object_key = 'path/to/your/file'
    local_file_path = '/home/samson/Downloads'

    # Define a wrapper function to pass to timeit
    def wrapper():
        download_file_from_s3(bucket_name, s3_object_key, local_file_path)

    # Number of executions: 1 (since downloading multiple times might be unnecessary and costly)
    # This setup ensures minimal measurement overhead.
    number_of_executions = 1

    # Time the download process
    download_time = timeit.timeit(wrapper, number=number_of_executions)
    print(f"Download completed in {download_time:.2f} seconds!")
