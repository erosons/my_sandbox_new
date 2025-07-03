CREATE OR REPLACE FUNCTION get_film () 
    RETURNS TABLE (
        image_id VARCHAR,
        score INT
) 
AS $$
BEGIN
    RETURN QUERY Select x.image_id,x.score
         from (
            select *,row_number() over (order by score desc) as row_count
             from UNLABELED_IMAGE_PREDICTION
            ) x
        where x.row_count <= (select count(*) from UNLABELED_IMAGE_PREDICTION)
      OFFSET 3 ROWS
      FETCH first 3 ROWS ONLY;
END; $$ 

LANGUAGE 'plpgsql';