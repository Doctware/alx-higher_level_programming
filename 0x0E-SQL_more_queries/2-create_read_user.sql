-- create database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user user_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2';

-- granting privilege on htbtn_0d_2 database to the given user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
