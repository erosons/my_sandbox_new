# BEST Practice  :https://docs.snowflake.com/en/guides
  # COMPUTE
   - Set suspend to 1 minutes IDLE Time
   - Don't use large Warehouses if they are not needed
   - Aviod query much of default usage Schema (Isolated)
  # STORAGE:
     - Zero-copy clone for data replication for storage cost
     - No unnecessary time_travel or fail safe except required
     - By default is one day
     - Use resource monitor to alert for ver-spending
     - Restrict ACL 

# Snowflake uses a combination (Pricing is => storage(compressed data, meta data for recovery) + Compute(Uptime and Size))
 -  Shared disk architecture -> Data stored in a centralized location
 -  Shared Noth Architecture -> data are stored across the Node
 -  MPP Cluster with Storage and Computed decoupled.

# Snowflake Consist of three Layers
   # Storage layer with a secured cloud layer
   # Compute Virtual warehouse -> Driven by driven business scenarios
      xsmall, small, medium and 5Xlarge  and snowpark-optimized( differrent give parameter configuration can 
      be automated in this)
       -  Compute warehouse -> For data processing/Querying
       -  Compute Warehouse -> for data Ingestion/Loading
   # Services layer 
      -  Which controls metadata stores/Management ( Zero Copy, Time Travel, data sharing) (SFL managed distributed across manay AZ)
      -  Qery Optimization, Query parsing and planning
      -  Authentication and Session managemnet (basic,keypair, OAuth, SSO, MFA)
      - Access Control : users, role , privileges
      -  Manage data consistency across even the WH scaled during processing
      -  It manages VWH and manges data updates and Access
      -  Ensuring all VWH sees the updated copy of the data without any downtime.
      Client:
        - ODBC
        - JDBC
        - ETL
        - SNOWSQL
        - Analytics BI
        - WebUI
# Query Flow/ request Flow 
   Uses request => Services layer/Coordinator(authenticate , decide optimal query plan ) => VWH (Instruction) $ resource allocation and access the storage => Result.

Certfication :
 - SnowPro Core
 - SnowPro Data Engineers
 - SnowPro Data Analyst
 - Data Scientist
 - Data Adminsitration