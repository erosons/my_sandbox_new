sqoop import \
--connect jdbc:postgresql://[hostname]:[port]/[database_name] \
--username [username] \
--password [password] \
--table [table_name] \
--target-dir /user/hadoop/[target_dir] \
--delete-target-dir \
--as-parquetfile \
--compression-codec snappy \
--num-mappers 10
