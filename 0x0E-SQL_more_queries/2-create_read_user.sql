-- To create a database hbtn_0d_2 and a user user_0d_2
-- And give the user_0d_2 a SELECT only privilege
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON 'hbtn_0d_2'.* TO 'user_)d_2'@'localhost';
