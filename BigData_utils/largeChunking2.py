import pandas as pd

# Define the input and output file paths
input_file = 'text.csv'
output_file = 'output.csv'

# Open the output file in write mode
with open(output_file, 'w') as output_f:
    # Iterate over the input file in chunks
    for chunk in pd.read_csv(input_file, chunksize=1000):  # Adjust chunksize as needed
        for _, row in chunk.iterrows():
            # Process each row and write to the output file
            output_f.write(','.join(map(str, row.values)) + '\n')
