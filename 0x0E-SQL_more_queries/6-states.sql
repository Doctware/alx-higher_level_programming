-- Creates the given database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- select the given database
USE hbtn_0d_usa;

-- create the given table
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
