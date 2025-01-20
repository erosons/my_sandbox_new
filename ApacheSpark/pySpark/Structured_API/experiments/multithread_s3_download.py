from concurrent.futures import ThreadPoolExecutor, as_completed
from pyspark.sql import SparkSession
import boto3
import os
import time

def download_part(bucket_name, object_key, part_number, range_start, range_end):
    s3 = boto3.client('s3')
    byte_range = f"bytes={range_start}-{range_end}"
    part_data = s3.get_object(Bucket=bucket_name, Key=object_key, Range=byte_range)
    data = part_data['Body'].read()

    # Save the data to a local file
    part_filename = f"part_{part_number}.dat"
    with open(part_filename, 'wb') as f:
        f.write(data)
    return part_filename, len(data)

def main():
    spark = SparkSession.builder \
        .appName("Multithreaded S3 Read and Save Example") \
        .getOrCreate()

    bucket_name = 'your-bucket'
    object_key = 'path/to/large/file'
    file_size = 1000000000  # Example: 1 GB
    num_parts = 10
    part_size = file_size // num_parts

    # Ensure the output directory exists
    output_dir = 'downloaded_parts'
    os.makedirs(output_dir, exist_ok=True)

    start_time = time.time()  # Start timing

    with ThreadPoolExecutor(max_workers=num_parts) as executor:
        future_to_part = {
            executor.submit(download_part, bucket_name, object_key, i, i*part_size, (i+1)*part_size - 1): i for i in range(num_parts)
        }
        
        for future in as_completed(future_to_part):
            part_number = future_to_part[future]
            try:
                filename, size = future.result()
                print(f"{filename} downloaded, size: {size} bytes")
            except Exception as exc:
                print(f"Part {part_number} generated an exception: {exc}")

    end_time = time.time()  # End timing
    print(f"Total time to download all parts: {end_time - start_time:.2f} seconds")

    spark.stop()

if __name__ == "__main__":
    main()
