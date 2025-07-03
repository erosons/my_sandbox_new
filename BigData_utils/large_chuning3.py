#pip install pandas pyarrow
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

def read_csv_in_chunks(file_path, chunk_size=1000):
    """
    Generator function to read a CSV file in chunks.
    
    Parameters:
    file_path (str): The path to the CSV file.
    chunk_size (int): The number of rows per chunk.
    
    Yields:
    DataFrame: A chunk of the CSV file as a DataFrame.
    """
    with pd.read_csv(file_path, chunksize=chunk_size) as reader:
        for chunk in reader:
            yield chunk

def write_chunk_to_parquet(df, file_path, file_index):
    """
    Write a DataFrame chunk to a Parquet file.
    
    Parameters:
    df (DataFrame): The DataFrame chunk to write.
    file_path (str): The base path for the output Parquet files.
    file_index (int): The index of the chunk to create unique file names.
    """
    table = pa.Table.from_pandas(df)
    pq.write_table(table, f"{file_path}_{file_index}.parquet")

def process_large_csv(input_csv, output_parquet_base, chunk_size=1000):
    """
    Process a large CSV file by reading it in chunks and writing each chunk to Parquet files.
    
    Parameters:
    input_csv (str): The path to the input CSV file.
    output_parquet_base (str): The base path for the output Parquet files.
    chunk_size (int): The number of rows per chunk.
    """
    chunk_generator = read_csv_in_chunks(input_csv, chunk_size)
    
    for i, chunk in enumerate(chunk_generator):
        write_chunk_to_parquet(chunk, output_parquet_base, i)
        print(f"Processed chunk {i}")

# Example usage
if __name__ == "__main__":
    input_csv_path = "large_file.csv"
    output_parquet_base_path = "output/large_file_chunk"
    process_large_csv(input_csv_path, output_parquet_base_path, chunk_size=1000)
