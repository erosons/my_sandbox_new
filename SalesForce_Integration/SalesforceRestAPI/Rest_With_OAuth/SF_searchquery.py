from SF_accesAuth import salesforcedAuth
import json

accessCon=salesforcedAuth()

search = 'sncf'
call = accessCon.sf_api_call('/services/data/v41.0/search/', parameters={
        'q': "FIND { %s } IN ALL FIELDS RETURNING Account (Id, Name), Contact (Id, Name), Opportunity (Id, Name), Lead (Id, Name) WITH METADATA='LABELS' " % search
    })
print(json.dumps(call, indent=3))