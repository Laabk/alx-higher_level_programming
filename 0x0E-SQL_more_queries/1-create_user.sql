-- Create the mysql server user and the password
-- Giving al privileges to the user on all databases

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
