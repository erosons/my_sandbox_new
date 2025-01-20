create or replace schema data_pipelines.manual_cdc;

Create table source(del boolean,id int ,name string);
Create or replace table target(id int ,name string);

{# manual statement to merge records #}
    merge into target t
        using  source s
        on t.id = s.id
        when not matched  and not s.del then 
        insert (id ,name) values(s.id, s.name)
        when matched  and not del then
        update set  t.name = s.name

{# Create stored proc on the CDC #}
create procedure cdc()
returns int
as $$
merge into target t using source s on  t.id = s.id
  when not matched and not del then insert (id, name) values (s.id, s.name)
  when matched and del then delete
  when matched and not del then update set t.name = s.name;
$$;

-- 3 x INSERT
INSERT INTO source VALUES (False, 1, 'John'), (False, 2, 'Mary'), (False, 3, 'George');
CALL cdc();
TRUNCATE TABLE source;
SELECT * FROM target;

-- UPDATE + INSERT
INSERT INTO source VALUES (False, 1, 'Mark'), (True, 2, NULL);
CALL cdc();
TRUNCATE TABLE source;
SELECT * FROM target;