from SF_accesAuth import salesforcedAuth
import json
import base64
from   pathlib import Path

accessCon=salesforcedAuth()

# 1) Create a ContentVersionc
path =  "download.png"
with open(path, "rb") as f:
    encoded_string = base64.b64encode(f.read())
    print(type(encoded_string))

    ContentVersion = accessCon.sf_api_call('/services/data/v40.0/sobjects/ContentVersion/', method="post", data={
        'Title': 'An image',
        'PathOnClient': path,
        'VersionData': encoded_string.decode('utf-8'),
    })
    ContentVersion_id = ContentVersion.get('id')

    print(json.dumps(ContentVersion_id, indent=3))

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