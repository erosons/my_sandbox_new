WITH date_series AS (
  SELECT
    DATEADD(day, SEQ4(), '2014-01-01'::date) AS d
  FROM TABLE(GENERATOR(ROWCOUNT => 365 * (2050 - 2014 + 1)))  -- Adjust the range as needed
)

SELECT
  TO_CHAR(d, 'YYYY-MM-DD') AS id,
  d AS full_date,
  EXTRACT(YEAR FROM d) AS year,
  EXTRACT(WEEK FROM d) AS year_week,
  EXTRACT(DAY FROM d) AS year_day,
  EXTRACT(YEAR FROM d) AS fiscal_year,
  TO_CHAR(d, 'Q') AS fiscal_qtr,
  EXTRACT(MONTH FROM d) AS month,
  TO_CHAR(d, 'MMMM') AS month_name,
  TO_CHAR(d, 'u') AS week_day,
  TO_CHAR(d, 'DAY') AS day_name,
  CASE WHEN TO_CHAR(d, 'DAY') IN ('Sunday', 'Saturday') THEN 0 ELSE 1 END AS day_is_weekday
FROM
  date_series