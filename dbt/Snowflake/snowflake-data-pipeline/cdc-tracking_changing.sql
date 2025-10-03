{# What if the source is not tracking changes and basic overidding data with changes tracking #}
create or replace schema data_pipelines.change_tracking;

Create table source(del boolean,id int ,name string);
alter table source set change_tracking =true

set ts1 = (select current_timestamp())


---- 3 x INSERT
INSERT INTO source VALUES (1, 'John'), (2, 'Mary'), (3, 'George');

-- TRACKING CHANGES -> UPDATE + INSERT
UPDATE source SET name = 'Mark' WHERE id = 1;
DELETE FROM source WHERE id = 2;



-- Review historical changes since the time tracking
select * from source
  changes (information => append_only) at (timestamp=>$ts1);



  -- Review current status of the table at current point in time
select * from source
  changes (information => default) at (timestamp=>$ts1);



--Create Table base on the current table Status
CREATE or replace table target
AS
select id, name  from source
  changes (information => default) at (timestamp=>$ts1);