Here’s an advanced example using some of the options:

# PUT COMMAND 

PUT file:///home/samson/Downloads/SampleSuperstore(in).csv @mystage
AUTO_COMPRESS = TRUE
OVERWRITE = TRUE
PARALLEL = 8
ENCRYPTION = TRUE;

This command:

    Uploads the file with compression enabled.
    Overwrites any existing file with the same name.
    Uses 8 parallel threads for faster upload.
    Ensures the file is encrypted.

# GET COMMAND
>> GET @mystage/file.csv file:///home/samson/Downloads;

# LIST Command:

    Lists the files currently in a stage.
 >> LIST @mystage;

    This command will display all files in the @mystage location.

### REMOVE Command fro cleaning a target files.

>>> REMOVE @mystage/file.csv;

    This command removes file.csv from @mystage.

COPY INTO Command:
>>> COPY INTO my_table FROM @mystage FILE_FORMAT = (TYPE = 'CSV');

### DESCRIBE STAGE Command:

>>> DESCRIBE STAGE @mystage;

###  LIST ALL STAGES

 >>> Show Stages


## Query the result of SHOW STAGES using RESULT_SCAN

>>> SELECT * FROM TABLE(RESULT_SCAN(LAST_QUERY_ID()));

