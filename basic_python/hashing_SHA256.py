import hashlib

def hash_filename_and_content(filepath):
    # Step 1: Read the filename and content
    filename = filepath.split('/')[-1].encode('utf-8')  # Convert filename to bytes
    with open(filepath, 'rb') as file:
        content = file.read()  # Read file content once

    # Step 2: Concatenate filename and content
    combined_data = filename + b'\0' + content  # Use a null byte as a separator

    # Step 3: Hash the combined data
    hash_object = hashlib.sha256(combined_data)
    return hash_object.hexdigest()

# Usage example
filepath = 'example2.txt'
with open(filepath,'w') as file:
    file.write('hello World')
hash_value = hash_filename_and_content(filepath)
print(f"Hash of filename and content: {hash_value}")