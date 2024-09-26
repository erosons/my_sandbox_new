OLTP-Relational:[ MySQL, SQlServer, Oracle,MariaDB,Postgres(OLAP/OLTP)]
## key-value DB : [redis,AWS dynamoDB,Google Memorystore] 
   file types: list, json , scalar value, string
  -> Use Cases for quick easy retrieval
     - Shopping cart details information
     - Storing active user sessions
     - Game session management
     - Api reply stored in cache
     - Product recommendataion

## Document-StoreDB: [MongoDB, Couchbase]
   file types: Json [ that wuld originally be stored across multiples tables are stored a single doc]
   {
  "customer_id": 1,
  "first_name": "Jtestn",
  "last_name": "Doe",
  "email": "jtestn.doe@example.com",
  "orders": [
    {
      "order_id": 101,
      "order_date": "2023-01-15",
      "order_total": 150.75
    },
    {
      "order_id": 102,
      "order_date": "2023-02-20",
      "order_total": 250.00
    }
  ]
}

  -> Use Cases for quick easy retrieval
    - product catalogs
    - WebApplication/E-Commerce
    - IOT
    - Reat Time Analytics

# Wide-Column : [Cassandra,Appache-Hbase,GoogleBigTable]
   see docs for explanation (columns are stored separately and identified by row keys, family columns are stored together on disk.)
     where colums are similar attributes they can be group together
     - family Columns -like Address, Orders
     - Super columns - [which combine family colums] -> customer
  -> Use Cases for quick easy retrieval
    - Time Series
    -IOT
    - Reat Time Analytics
# GraphDB : [Neo4j, DataStax Enterprose Graph] -> 
    Concept  is based on Node and Edges 
    where Node is and Entity and Edges are the relationship, Node can have properties to describe the Node
    Use Cases
        - Logistics
        - MetaData Management 
        - NLP Social Networks
        - Fraud Detection
        - Recommendation Engines
    Example:


# Search Engine : [Elastic Search, Solr] 
-> Uses schema Json for storing data, 
And uses indexes to categorize the similiar characteristics among data.
- Full-text search
- Time-series data
- Logging and analysis
- Auto Suggestion/ Auto Compelete

