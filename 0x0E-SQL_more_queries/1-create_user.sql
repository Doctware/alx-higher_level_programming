-- Create the given user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'Adeyemi,52242.';

-- then grants the given user all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- reload the privileges from gtrants table to ensure immidiate effect 
FLUSH PRIVILEGES;
