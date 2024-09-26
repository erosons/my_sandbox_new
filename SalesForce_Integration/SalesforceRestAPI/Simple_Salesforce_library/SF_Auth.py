from simple_salesforce import Salesforce
from params import params


class SfAuth_token:
    def __init__(self) -> None:
       self.auth= Salesforce(**params)

testobj=SfAuth_token()

print(testobj)