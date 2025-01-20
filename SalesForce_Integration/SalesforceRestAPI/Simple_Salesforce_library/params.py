import os

params = {
        "username": os.getenv("myemail"), # The email you use to login
        "password": os.getenv("SFpaswword"), # Concat your password and your security token
        "security_token": os.getenv("security_token")
        }