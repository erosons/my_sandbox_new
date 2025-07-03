


--Dynamic sampling using a While loop Statement 3
----------------------------------------------------------------------------------------
--Expected output is 9  with each  been the third sample of a 5 rows pagination selected
----------------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION images_sampling () 
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
Maxpagecount := CEILING(Maxpagecount);
While Maxpagecount >= rowsOfpage loop
    RETURN QUERY Select * 
     from 
	    (Select x.image_id,x.score
	      from (
			select *,row_number() over (order by score desc) as row_count
			from UNLABELED_IMAGE_PREDICTION
								
	         ) x
			where x.row_count <= (select count(*) from UNLABELED_IMAGE_PREDICTION)
			OFFSET (rowsOfpage*5) ROWS
			FETCH next 5 ROWS ONLY
	      ) y
	      OFFSET 2 ROWS
	      FETCH first 1 ROWS ONLY;
        rowsOfpage :=rowsOfpage + 1;
END LOOP;
END; $$ 

LANGUAGE 'plpgsql';



SELECT
    * FROM images_sampling ()





-----------------------------------------------------------------------------------------------------------------------
                          --Non Dynamic sampling  approach 
------------------------------------------------------------------------------------------------------------------------
--here you will need to provide the argument increment by 1 per page
------------------------------------------------------------------------------------------------------------------------

CREATE OR REPLACE FUNCTION image_sampling (pageNumber integer) 
    RETURNS TABLE (
        image_id int,
        image_score float
) 
AS $$
BEGIN
--select count(*) into Maxpagecount from UNLABELED_IMAGE_PREDICTION;
--Maxpagecount := CEILING(Maxpagecount/rowcount);
    RETURN QUERY select * 
     from 
	    (Select x.image_id,x.score
	      from (
			select *,row_number() over (order by score desc) as row_count
			from UNLABELED_IMAGE_PREDICTION
								
	         ) x
			where x.row_count <= (select count(*) from UNLABELED_IMAGE_PREDICTION)
			OFFSET (pageNumber*5) ROWS
			FETCH next 5 ROWS ONLY
	      ) y
	      OFFSET 2 ROWS
	      FETCH first 1 ROWS ONLY;

END; $$ 

LANGUAGE 'plpgsql';


SELECT * FROM image_sampling (1)