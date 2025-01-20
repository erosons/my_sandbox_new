-- PURGE not supported!
create or replace pipe emp_pipe
  auto_ingest = true
as
  copy into emp_pipe from @my_stage_s3
    file_format = (type = 'CSV')
    on_error = 'CONTINUE';

show pipes;

-- Setup the event notification on s3 properties for all PUT/post/multipart API action on the object
-- Add snowflow SQS arn which snowflake is listening on the event to the SQS secttion

--REVIEW information schema of the State of the pipe
SELECT system$pipe_status('emp_pipe')


--Testing Validation
--Loaded CSV files without their header
SELECT * FROM emp_pipe;

-- # Cleanses 
Alter pipe emp_pipe
 set pipe_execution_paused = true