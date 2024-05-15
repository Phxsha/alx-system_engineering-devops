#!/usr/bin/env bash

# Create MySQL user
mysql -u root -e "CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';"
mysql -u root -e "GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';"

# Create database and table, add entry
mysql -u root -e "CREATE DATABASE IF NOT EXISTS tyrell_corp;"
mysql -u root -e "USE tyrell_corp; CREATE TABLE IF NOT EXISTS nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));"
mysql -u root -e "USE tyrell_corp; INSERT INTO nexus6 (name) VALUES ('Roy Batty');"

# Grant SELECT permissions
mysql -u root -e "GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';"

# Create replica user
mysql -u root -e "CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica_user';"
mysql -u root -e "GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';"

# Grant SELECT on mysql.user to holberton_user
mysql -u root -e "GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';"
