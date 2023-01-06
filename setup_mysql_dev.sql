-- SQL script to prepare a mysql server for the project
-- Creates a database if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates a user for using the database
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grants all privilages to the user 'hbnb_dev' on the database 'hbnb_dev_db'
GRANT ALL PRIVILEGES  ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grants select privilages to 'hbnb_dev'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
