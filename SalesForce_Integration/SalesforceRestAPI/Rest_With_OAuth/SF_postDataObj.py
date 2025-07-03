from SF_accesAuth import salesforcedAuth
import json

accessCon=salesforcedAuth()

call = accessCon.sf_api_call('/services/data/v39.0/sobjects/Opportunity/', method="post", data={
    'CloseDate': '2018-03-01',
    'Name': 'Gene My big deal',
    'StageName': 'Prospecting',
    'Type': 'Existing Customer - Upgrade',
    'Amount': '500000.00',
    'AccountId': '001Dn000007u22zIAA'
})

print(json.dumps(call, indent=3))
#opportunity_id = call.get('id')