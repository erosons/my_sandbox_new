from SF_accesAuth import salesforcedAuth
import json
import pandas as pd

accessCon=salesforcedAuth()


object_to_export = "Opportunity"
limit = 10000

describe = accessCon.sf_api_call('/services/data/v40.0/sobjects/%s/describe' % object_to_export)

if not describe.get('queryable', False):
    raise Exception("This object is not queryable")

# This list out all the Fields from the object.
fields=[f['name'] for f in describe.get('fields')]
print(fields)


query = "SELECT %s FROM %s LIMIT %i" % (
    ", ".join(fields),
    object_to_export,
    limit
)

call = accessCon.sf_api_call('/services/data/v40.0/queryAll/', {'q': query})


# This print out all the records and all fields in the objects in Json 
#print(json.dumps(call, indent=4))


data=[]
rows = call.get('records', [])
for obj in call.get('records', []):
    data.append(obj)
df=pd.DataFrame([data])
print(df.head(10))


# This print out all the records and all fields in the objects
#print(json.dumps(call, indent=4))