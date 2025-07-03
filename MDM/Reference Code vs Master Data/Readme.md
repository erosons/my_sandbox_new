# Reference Data 
 - are data used to classify or categorize other data (Master data)

This can be sourced from externally or Externally.

Master -> is the process of creating and maintaining a single master record - or single source of truth - for Entity in the business
          Through MDM, organization gain a trusted , current view of key data that can shared across the business and used for better reporting, deision-making and process efficiency.
        
# Types of Master Data 
   - Custome Master data Management (collecting consolidating and maninting and distributing customer data in the Organzation)
        - Demographics Data
        - Transactional data, sales history , Payment history Sales Volumes
        - Behavioural Data - Marketing Preferences,comminucation methos , click through rate,
        - Communication Data- Tickets, inquiry
        Benefits: Better insight and better user experience, personalization and better data goverance
       # Example:
            Let says you an ecommerce store that sells products in 100 diferent af categoris. Customer master data managment allows identify target segments to promote your customers. 
            -> Personalization and Recommendation Engine
            -> Discount on categories they bought before or expressed Interest
            -> Churn Analysis and offers
        
   - Product Master data Managment -> collecting consolidating and maninting and distributing company products and its characteristics.
       - Product name
       - Product number
       - Description
       - weight
       - dimension
       - material
       - Manufacturer
       - Supplier
        # Benefits-> Better supplier chain Managment(inventory level),reduce funds,decision, customer experience, comliance and regulations.
        # Example: 
        if yor a producig products you need to comply with FDA, regulations such as your products need to be labelled with accurate and up-date info on ingredients etc
        MDM you canautomate and centralize the management of the product infrmation on labels.
    
    - Financial Master data Management -> 
       - Tax information, 
       - price ,
       - cost,profit ,
       - currency,
       - exchange Rate, 
       - Customer deposit
       # Common Challenge:
       Financial reporting due to inconsistences data sits in silos across the different departments and locations.
       # Benefits->,complinace and regulation
    Partner Master Data -> Collecting consolidating and maninting and distributing data about the company business partners
      - Supplier information
      - Distributor information
       # Benefits-> no more duplication, time spent finding the data
    - Employee Master Data
        - PII
        - Contract
        - Job Titles
        - Benefits
       # Benefits - Centralized and governace information repository, Compliance and legal requirements

# ############################       
## Managing  Master data
# ############################

Data Collection => Data Validation => (Data Integration)
=> Data Enchrichment => data Governance Access and Security 
=> Data Maintenenace => Data Analyics and Reporting  => Data Monitoring

Data Collecting (ETL,T-SQL in stored procedure) -> The data collection from various source systems and move the to centralize location.
Data Validation  -> Accuracy, Completenes,Data Quality Checks with Rules -> data Analyst
Data Integration -> Combine the data into a centralize repository for MDM needs
Data Enchrichment (For complete , though optional) -> This enchancing the complete, releveant  e,g a bank that provide Loans to a customer ( credits score, historical loans, Address doctors, to make better decision)
Data G and Access and Secuirty -> it more of the Unmberala, polices, sponsors, framework, define accesss controls
Data Maintenance -> invoves ongoing updates , Changing, Cleaning
Data distribution (Data intgerations) -> Ensure downstreams systems and applications get this data through a distribution Mechnaism, for biz to benefir the data has to be distributed
Data Analytics and Reporting  ->  Analyzing the data for so many scenario to great models , KPIs
Data Monitring - Data Quality Alerts and Metris for automated monitor  through threshold definition.
