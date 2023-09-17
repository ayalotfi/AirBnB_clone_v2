-- Creates a MySQL server with:
--   Grants SELECT privilege for hbnb_dev on performance_schema.
--   Grants all privileges for hbnb_dev on hbnb_dev_db.
--   User hbnb_dev with password hbnb_dev_pwd in localhost.
--   Database hbnb_dev_db.

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER
    IF NOT EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES
   ON `hbnb_dev_db`.*
   TO 'hbnb_dev'@'localhost'
   IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT
   ON `performance_schema`.*
   TO 'hbnb_dev'@'localhost'
   IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;
