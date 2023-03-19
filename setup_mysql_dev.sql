-- This script creates a database: hbnb_dev_db
-- a new user hbnb_dev in localhost
-- grants all privileges to the user on the hbnb_dev_db database
-- grants SELECT privelege on the performance_schema database

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
