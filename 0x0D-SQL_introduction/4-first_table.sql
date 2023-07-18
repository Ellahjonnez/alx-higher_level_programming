-- A script that creates a table called first_table in the current database in your MySQL server.
-- first_table description:
--             id INT
--             name VARCHAR(256)
-- The database name is passed as an argument of mysql command
-- If the first_table already exists, script should not fail
-- SELECT or SHOW statements are not allowed

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
