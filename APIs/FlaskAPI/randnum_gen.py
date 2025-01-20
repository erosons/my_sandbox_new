import os

def randnum_gen():
    key = str(os.urandom(24)).replace('b','')
    return key