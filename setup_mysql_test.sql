-- SQL script to prepare a test server for the project
-- Creates the database hbnb_test_db if it does not exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates user hbnb_test if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grants all privilages to the user 'hbnb_test' on the database 'hbnb_test_db'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grants select privileges to 'hbnb_test' on the 'performance_shcema' databasew
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PREVILEGES;