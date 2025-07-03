## Datalake is Architecture that can be leverage on this technology
- Hadoop HDSF
- Kafka
- No SQL
- Apache Kudu
- Object Storage

## Azure Datalake Storage Gen2:
   - Datalake Gen1 -> What built on HDFS as a Storage layer
   - Azure Blob storage: Is  general purpose object storage , optimized to hold massive amount of , unstructured data, Text or Binary Data
        cost Efficient
        Store Tiers
        -> Hot 
        -> Cold
        -> Archive
Only when you have infrastructure that uses USQL that is gen you should gen1 if not use Gen2


# ADLS API (Hierarachical Namespace)
   Performance Ench -> Security -> Scale Cost Effectiveness
    ||
 Blob API ->Blob Storage
    Object Tiering(LPM)-> AD RBAC , HA/DR -> Data Gov & mgt

# Hierarchical namespace:
 ADLS is Organized in a folder and subfolder which a feature that allows it to intgerate with Hadoop
 as this folder structure is required in Hadoop
 - Allows easy managemnet (deleting, renaming,organzing,Moving directory)
 - Allows easy performance on easy folder subtree

## Note when creating ADLS GEN2
It does not exists as a separate service, rather it is creation on blob storage
To create 
   - From All service in the portal select Storage Account

## Integration
- POSIX complient implemented by IEEE
- Integration with Hadoop (ABSF Driver) allows for integration with Databricks, PowerBI, Cloudera, Hontonworks
## Scalability no limit
- an stores petabytes, zetabytes
## Performance
- Support throughput for parallel data processing
## Security
In Blob storage: We cannot implement permissions at the blob level rather the container level
ADLS,
HA/Faulty tolerance Replica -3

## Challenges
 - Hard to query
 - Data Quality issues


## Data Ingestion into ADLS
 # Local direction
- Azure PowerShell
- Azure CLI
- Storage Explorer run this before opening explorer on linux(snap connect storage-explorer:password-manager-service :password-manager-service
)
- AzCopy tool

# Adhoc Data from Blob
- Azure Data Factory -> cloud version of SSIS
- AzCopy tool
- HDinsight comes with DistCp out of box copy

# Stream Data
- Azure Stream Analysts,captures data event by events  and write as Batch in ADLS
- HDStream storm same as above

# RDBS
- Azure Data Factory

# WebServer Logs
- Azure powerShell
- Azure CLI
- Azure Data Factory

# Migration from HDFS Hadoop clusters
- ADF

# Really large Datasets
- Azure Express route - direct connect to azure data centre in secure 