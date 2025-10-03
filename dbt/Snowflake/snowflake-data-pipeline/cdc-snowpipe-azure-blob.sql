
Staorage Integration setup 
-> Stage Creation
-> Notification Setup  
  ( - In Azure create Queue 
        Create of Events (Make sure you register your MicroftEventGrid in order to provsion Events)
-> Notification integration 
-> Create SnowPipe

-- PURGE not supported!
CREATE OR REPLACE PIPE emp_pipe_azure
  AUTO_INGEST = TRUE
  INTEGRATION = 'SNOWPIPE_EVENT'
  
AS
  COPY INTO emp_pipe_azure -- Replace with the target table you want to copy data into
  FROM @my_azure_stage_int
  FILE_FORMAT = (TYPE = 'CSV')
  ON_ERROR = 'CONTINUE';

show pipes;

-- Setup the event notification on s3 properties for all PUT/post/multipart API action on the object
-- Add snowflow SQS arn which snowflake is listening on the event to the SQS secttion

--REVIEW information schema of the State of the pipe
SELECT system$pipe_status('emp_pipe')


--Testing Validation
--Loaded CSV files without their header
SELECT * FROM emp_pipe_azure;

-- # Cleanses 
Alter pipe emp_pipe
 set pipe_execution_paused = true