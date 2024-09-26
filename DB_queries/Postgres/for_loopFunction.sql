CREATE OR REPLACE FUNCTION get_film (p_pattern VARCHAR, p_year INT) 
    RETURNS TABLE (
        film_title VARCHAR,
        film_release_year INT
) AS $$
DECLARE 
    var_r record;
BEGIN
    FOR var_r IN (SELECT 
                title, 
                release_year 
                FROM film 
                WHERE title ILIKE p_pattern AND 
                release_year = p_year)  
    LOOP
        film_title := upper(var_r.title) ; 
        film_release_year := var_r.release_year;
        RETURN NEXT;
    END LOOP;
END; $$ 
LANGUAGE 'plpgsql';