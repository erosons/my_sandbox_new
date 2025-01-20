from SF_accesAuth import salesforcedAuth
import json

accessCon=salesforcedAuth()


# 1) Create a ContentVersion 
ContentVersion = accessCon.sf_api_call('/services/data/v40.0/sobjects/ContentVersion', method="post", data={
    'Title': 'Important attached document',
    'ContentUrl': 'https://drive.google.com/drive/u/1/folders/1z9waqhpx2GAE9TTddWpRd8c0SiHm0wVF'
})

ContentVersion_id=ContentVersion.get('id')


# 2) Get the ContentDocument id
ContentVersion = accessCon.sf_api_call('/services/data/v40.0/sobjects/ContentVersion/%s' % ContentVersion_id)
ContentDocument_id = ContentVersion.get('ContentDocumentId')


# 3) Create a ContentDocumentLink
Opportunity_id = "006Dn000004HzIqIAK"
ContentDocumentLink = accessCon.sf_api_call('/services/data/v40.0/sobjects/ContentDocumentLink', method = 'post', data={
        'ContentDocumentId': ContentDocument_id,
        'LinkedEntityId': Opportunity_id,
        'ShareType': 'V'
    })

print(json.dumps(ContentDocumentLink , indent=3))
#opportunity_id = call.get('id')