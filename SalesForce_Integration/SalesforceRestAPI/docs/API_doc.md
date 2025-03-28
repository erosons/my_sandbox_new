>> https://jereze.com/code/salesforce-rest-api-python/
>> https://readthedocs.org/projects/simple-salesforce/downloads/pdf/latest/
>> https://pypi.org/project/simple-salesforce/0.3/


urllib3:https://urllib3.readthedocs.io/en/1.26.x/user-guide.html#ssl


# Types of Authentication for Webservice Call
   - Key value : (Tokenization where server provides a token/key which should included in the request)
   - Login Credentials : (the usename and password are probably sent to a method and a sessionID is generated, which used for the comm)
   - OAuth 2.0:
   - Certificate based : Server provides a certificate which the client use to authenticate.

DATA FORMATS:
   - JSON/XML

DATA TYPE  EXCHANGE/TRANSMITION BETWEEN CLIENT AND SERVER
   - String format (Json String)

JSON - Java Scripts Object Notation
  - It is the format for exchanging data across the network
  - The entire data is an object
  - It is language or platfrom indepedent
  - It is a self describe structure
  - It is represented in nae -value pair
  
  


## Project description
 salesforce
A python connector for Salesforce
--pip install salesforce

Connect
=======
from salesforce import Connector

conn = Connector(username, password, security_token)
connect to sandbox
from salesforce import Connector

conn = Connector(username, password, security_token, subdomain='test')
optional parameters
max_reties = set a maximum number of retries
version = set a version other than the default, 44.0
client_id = id of the app to tag the call with

## Selecting from Salesforce table

Pass in the name of the object, a list of the field names you want and the criteria with %s where your variables will go and a list of your values to identify which records to select.

Note that you will need to add single quotes around your %s placeholders if the field type requires it, like strings do.

A list of dictionaries will be returned.

from salesforce import Connector

conn = Connector(username, password, security_token)
fields = ['firstname', 'lastname]
criteria = 'WHERE id = %s'
values = ['003D000000QV9n2IAD']
results = conn.select('contact', fields, criteria, values)

## IN Filter Criteria

This connector is set up to dynamically handle IN criteria.

For example the below will query Salesforce for: SELECT Id FROM Contact WHERE FirstName IN ('Sarah', 'James', 'Jamie')

Note that in the case of in criteria quotes will automatically be placed in the query for you if the variables in the list are type str.

from salesforce import Connector

conn = Connector(username, password, security_token)
fields = ['Id']
criteria = 'WHERE id IN %s'
values = [['Carey', 'Casey', 'Jamie']]
results = conn.select('contact', fields, criteria, values)

## Creating a table in Salesforce

Pass in the object name and a dictionary with the data to use in the create.

from salesforce import Connector

conn = Connector(username, password, security_token)
data = {"FirstName": "Jamie",
"LastName": "Doe",
"Email": jdoe@gmail.com}
conn.create("Contact", data)

## Update table in Salesforce

Pass in the id, object name and a dictionary with the data to use in the update.

from salesforce import Connector

conn = Connector(username, password, security_token)
record_id = "003advearera"
data = {"FirstName": "Carey"}
conn.create(record_id, "Contact", data)

## Delete table in Salesforce

Pass in the id of the record to delete

from salesforce import Connector

conn = Connector(username, password, security_token)
conn.delete("003advearera", "Contact")
Bulk Operations
These methods use the Salesforce SObjects Collections endpoints.

General options
all_or_none: Specifies whether you want one error to roll back the batch, or not. Remember batches are 200, so if you pass in over 200 records only the 200 in that batch will be rolled back. Batches before and after will proceed unless they also have errors. batch_size: This defaults to 200, the maximum that Salesforce allows, but you can specify a smaller batch size if you want.

## bulk_create()

This method enables you to create records in batches of up to 200.

Salesforce SObject Collections Create Endpoint Reference.

If the records are all of the same type you can pass the object name directly in the bulk_change() call. If they are of different types you will need to use the add_attributes method to set the correct type information before using the bulk_change method.

For example this will create two contacts:

from salesforce import Connector

conn = Connector(username, password, security_token)
contacts = [{"FirstName": "Jamie",
"LastName": "Doe",
"Email": jdoe@gmail.com,
"AccountId": "001qervaaer"},
{"FirstName": "Carey",
"LastName": "Doe",
"Email": cdoe@gmail.com,
"AccountId": "001qervaaer"}
]
conn.bulk_create(contacts, object_name = 'Contact')
This will create an Account and a contact:

from salesforce import Connector

conn = Connector(username, password, security_token)
contact = {"FirstName": "Jamie",
"LastName": "Doe",
"Email": jdoe@gmail.com,
"AccountId": "001qervaaer"}
account = {"Name": "Fake Corp"}
acc_attr = conn.add_attributes(account, "Account")
cont_attr = conn.add_attributes(contact, "Contact")
conn.bulk_change([acc_attr, cont_attr])

bulk_update()
This works the same way as the bulk create above except you need to include the record id in the payload.

Salesforce SObjects Collections Update Endpoint Reference

add_attributes()
This method enables you to easily add the object name to an object to make using the bulk create and update methods easier.

It also gives you the ability to add a referenceId, which makes finding the response for specific records easier, and any other kwargs you might need to add to the attributes dictionary within your payload.

from salesforce import Connector

conn = Connector(username, password, security_token)
contact = {"FirstName": "Jamie",
"LastName": "Doe",
"Email": jdoe@gmail.com,
"AccountId": "001qervaaer"}
attr_cont = conn.add_attributes(contact, "Contact", "jdoe@gmail.com")

## bulk_delete()

This method enables you to quickly delete multiple records. It is similar to the other bulk operations, but does not require a record type to be specified and accepts a list of Salesforce record ids instead of a list of dictionaries.

from salesforce import Connector

conn = Connector(username, password, security_token)
to_delete = ['0011qewavawer', '003averatea]
response = conn.delete(to_delete, False)
Create Nested Records
Salesforce gives you the option to create parent and child records in one call. For example creating an Account with Contacts.

Salesforce Composite Sobject Tree Create Endpoint Reference

## nested_insert()

from salesforce import Connector

data = {
"attributes" : {"type" : "Account", "referenceId" : "ref1"},
"name" : "SampleAccount1",
"phone" : "1234567890",
"website" : "www.salesforce.com",
"Contacts" : {
"records" : [{
"attributes" : {"type" : "Contact", "referenceId" : "ref2"},
"lastname" : "Smith",
"email" : "smith@salesforce.com"
},{
"attributes" : {"type" : "Contact", "referenceId" : "ref3"},
"lastname" : "Evans",
"email" : "evans@salesforce.com"
}]
}
}
conn = Connector(username, password, security_token)
response = conn.nested_insert(data, 'Account')

## build_nested()

A helper to generate the data structure for the nested insert

from salesforce import Connector

account = {"name" : "SampleAccount1",
"phone" : "1234567890",
"website" : "www.salesforce.com"}
contacts = [{
"lastname" : "Smith",
"email" : "smith@salesforce.com"
},{
"lastname" : "Evans",
"email" : "evans@salesforce.com"
}]
attr_acc = conn.add_attributes(account, 'account', 'acc1')
attr_conts = [conn.add_attributes(c, 'contact', c['email']) for c in contacts]

conn = Connector(username, password, security_token)

nested = conn.build_nested('Account', attr_acc, {'Contacts': attr_conts}])

## call()

This method enables you to specify the url, method and data to send to Salesforce. 
You will probably want to use the create, update, delete, select, bulk_create, bulk_update, 
bulk_delete methods most of the time, but it gives you the option if there is functionality that is not covered here.
