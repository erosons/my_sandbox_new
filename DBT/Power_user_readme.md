## url : docs.myaltimate.com

API connection a back SAAS server provides , provides the following features  but via an API key
 - Generating DBt Model fromSQL
 - Generating dbt documentation
 - Generatingdbt test
 - Query Explaination

 Generate API key for Free : https://app.myaltimate.com/register

# Code Model Generation 
 - Click on generate model in in the staging area  sources.yaml/yml to generate all our model
 
# Code completion
  Typing ref in the Jinja , will auto list all the ref

# Query Transalation : Many times you need to transform SQL query from one dialet to another dialet
  postgres - Bigquery dialect
  msql - Big query dialect
   
  Click to use datapilot and Select translate other SQL dialect , sleect your source and target dialet
  Note: It takes the context of the entire code repository
        Provide an explanation of what it can convert or supported and what is not supported.

# Datapiot for Query Explaination
 Sometimes we need to understand sql we have wrtten a dbt SQL code 6-1yr ago and find it difficult undertand what happened back then
   right click to use datapilot -Explain

# Datapiot for Update Model
  right click to use datapilot - change , send in a prompt for additional column with defined logic within the context of the data.

# Project Governace : use Action
- Find areas of a dbt project that are misaligned with dbt best practices
configure best practices checks with yaml -> https://datapilot.readthedocs.io/en/latest/insights.html

OR use SAAS version:

# Write dbt Test Automatically: Use documentation and Editor

 Automatically various king of test including custoon test and load them into schema.yam files and test , by pressing the UI button 

# Impact Anayisi with Colum Lineage

Lineage analysis , column level lineage,(click on modern and column to see column linrge history model)


# Documenta genertion

Using Documemtation Editor you can generate documentation of dim and facts and leverage the functionality Datapilot too

# Collaboration 
Using the comments to work with buisness users

# Tests
- Singular Testing->