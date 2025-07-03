import pandas as pd

# Open the file manually using a context manager
with open('file.csv', 'r') as file:
    # Read the file into a DataFrame
    df = pd.read_csv(file)

# Display the first 5 rows of the DataFrame
print(df.head(5))

# Save the DataFrame to a new CSV file
df.to_csv('txt.csv', index=False)

del df