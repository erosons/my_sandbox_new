## Generate base64-encoded key
import base64
import os

def generate_base64_key(length):
    key = os.urandom(length)
    base64_key = base64.b64encode(key).decode('utf-8')
    return base64_key

# Example usage
key_length = 32  # Length of the key in bytes
base64_key = generate_base64_key(key_length)
print("Base64-encoded key:", base64_key)

## Convert a character to base64

import base64

def convert_to_base64(character):
    # Convert the character to bytes
    byte_character = character.encode('utf-8')
    
    # Encode the bytes using base64
    base64_character = base64.b64encode(byte_character).decode('utf-8')
    
    return base64_character

# Example usage
input_character = 'A'
base64_character = convert_to_base64(input_character)
print("Base64-encoded character:", base64_character)