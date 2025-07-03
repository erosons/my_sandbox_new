Creating DB  and users and priviledges

CREATE DATABASE airflow_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE airflow TO postgres;

# Also note that since SqlAlchemy does not expose a way to target a specific schema in the database URI, you need to ensure schema public is in your Postgres user’s search_path.

ALTER USER postgres SET search_path = public;