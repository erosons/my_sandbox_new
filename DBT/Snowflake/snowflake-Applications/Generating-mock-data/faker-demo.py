from faker import Faker
import pandas as pd

fake = Faker()
data = [
    {
        "name": fake.name(),
        "address": fake.address(),
        "state": fake.state(),
        "city": fake.city(),
        "email": fake.email(),     
    }
    for _ in range(10)  # Generate 10 records
]

df = pd.DataFrame(data)
print(df)