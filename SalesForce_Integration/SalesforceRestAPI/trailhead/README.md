Connecting 2 or More systems together
e.g Good drive to Salesforce <-> vice versa

Web Services 

REST - Fast support all types of devices  and used mostly on Web Applications -> data formats are mostly (JSON,XML) and 

SOAP - Slow compared to REST. Works with XML. And know to be more scure than REST calls

REST web sevices Method supported

   GET   -> Retrieves the data works like Read in SQL
   POST  -> Insert new data -> Like insert record in SQL
   PUT   -> Insert new data or Update existing data  works like Upsert in SQL
   PATCH -> Update existing data -> like update in SQL
   DELETE -> Delete existing data -> works like delete records in SQL

SECURED API

 Will requires a form of Authorization to get pass and access resources on the web server.


## Integrating Salesforce with Spoonacular Recipe


Mock testing
    Development Testing using : Postman
    Test and for Mock: https://gorest.co.in/

## API method codes
for callout/request I am using Trailhead to get sample Codes:  https://trailhead.salesforce.com/content/learn/modules/apex_integration_services

Note before you can make a callout from Salesforce to any endpoint you need to add the website to your remote Settings. 
 - This is navigate to your service Setup in your home and search for remote setting. 
 - The add your endpoint 

# Developing Console
 From your setting button locate your Developer 
   - Create Debug ,write your callout/request code and pass all authorization as specified by the endpoint documentation.
   - Trailhead is a good webapplication for Rest API code writing. Once successful with call then proceed to write an Apex Class.
   
Step1:  For Debug testing.
        From the developer Console, From debug, select  Execute Anoynomus Window
    
     - Write your callout_test.java -> see code
          Execute Anoynomus Window
 Step2:  From the developer Console, From File, select New and Create a new Apex Class.
      
       Use the  Execute Anoynomus Window and execute the class and method.
          Spoonacular.getRandomReceipe();


# In case I ever wnt to build a Salesforce web Application 
 https://github.com/choudharymanish8585/apex-integration-crash-course