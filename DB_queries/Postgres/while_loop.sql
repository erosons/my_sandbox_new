----------------
--While loop Statement 1
-----------------
--https://sqlserverguides.com/postgresql-while-loop/

do $$
declare
Maxpagecount integer ; 
begin
select count(*) into Maxpagecount from UNLABELED_IMAGE_PREDICTION;
raise notice 'Out addition count %', Maxpagecount;
end $$;

----------------
--While loop Statement 2
-----------------

do $$
declare
add integer := 10;
begin
while add > 0 loop
raise notice 'Out addition count %',add;
add := add-1;
end loop;
end$$;

----------------
--Dynamic sampling using a While loop Statement 3
-----------------

CREATE OR REPLACE FUNCTION get_film () 
    RETURNS TABLE (
        image_id int,
        image_score float
) 
AS $$
Declare
rowsOfpage integer :=1;
rowcount integer :=5;
Maxpagecount integer ; 
BEGIN
select count(*) into Maxpagecount from UNLABELED_IMAGE_PREDICTION;
Maxpagecount := CEILING(Maxpagecount/rowcount);
While Maxpagecount >= rowsOfpage loop
    RETURN QUERY Select y.image_id,y.score
					from
					(
						Select x.image_id,x.score,row_number() over (order by x.score desc) as row_count
							 from (
								select *,row_number() over (order by score desc) as row_count
								 from UNLABELED_IMAGE_PREDICTION
								) x
							where x.row_count <= (select count(*) from UNLABELED_IMAGE_PREDICTION)
							OFFSET (rowsOfpage-1) ROWS
							FETCH first rowcount ROWS ONLY
					 ) y
					 where y.row_count=3;
        rowsOfpage :=rowsOfpage + 1;
END LOOP;
END; $$ 

LANGUAGE 'plpgsql';

----------------
--Non Dynamic sampling using a While loop Statement 3
-----------------

CREATE OR REPLACE FUNCTION get_film2 (rowsOfpage integer, rowcount integer) 
    RETURNS TABLE (
        image_id int,
        image_score float
) 
AS $$
Declare
Maxpagecount integer ; 
BEGIN
select count(*) into Maxpagecount from UNLABELED_IMAGE_PREDICTION;
Maxpagecount := CEILING(Maxpagecount/rowcount);
    RETURN QUERY Select y.image_id,y.score
					from
					(
						Select x.image_id,x.score,row_number() over (order by x.score desc) as row_count
							 from (
								select *,row_number() over (order by score desc) as row_count
								 from UNLABELED_IMAGE_PREDICTION
								) x
							where x.row_count <= (select count(*) from UNLABELED_IMAGE_PREDICTION)
							OFFSET (rowsOfpage-1) ROWS
							FETCH first rowcount ROWS ONLY
					 ) y
					 where y.row_count=3;

END; $$ 

LANGUAGE 'plpgsql';


