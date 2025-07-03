## Loading and UnLoading
JSON-> FOr hierarchical semi-structured data , including 
       ND JSON -> Newline Delimied JSON

AVRO -> Only fo loading , row-oriented(good for transactions), compressed binary format.
       Additional schema evolution metadata(json for RPC) serialization-> used in Hadoop
ORC  -> Optimized Row Columnar-> Only for loading . Tabular format but column oriented(good for Analytics).
      Used for Hadoop(Hortonworks and Facebook Collab)
Parquet -> tabular Format , but binary compressed and colum-oriented (Good for analytcs)-> Used by Hadoop ,cloudera and Twiiter Collab