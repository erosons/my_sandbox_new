from SF_accesAuth import salesforcedAuth
import json


accessCon=salesforcedAuth()

print(json.dumps(accessCon.sf_api_call('/services/data/v39.0/query/', {
    'q': 'SELECT AccountId, OrderNumber__c FROM Account where AccountId ="0019E000009WTBVQA4"'
}), indent=2))