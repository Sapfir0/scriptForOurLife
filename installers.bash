#!/bin/bash

#apt update
#apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys #58118E89F3A912897C070ADBF76221572C52609D
#apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
#apt update && apt-cache policy docker-engine
#apt install -y docker-engine
#ble docker robit only on ubuntu

apt install -y npm nodejs mysql-server git
mysql_secure_installation

mysql << EOF
	create database usersDB2; 
	create user 'metidaSQL'@'localhost' identified with mysql_native_password by '123456';
	grant all privileges on usersDB2.users to 'metidaSQL'@'localhost';
	grant all privileges on usersDB2.articles to 'metidaSQL'@'localhost';
EOF


