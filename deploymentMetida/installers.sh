#!/bin/bash

echo "Do you want install nodejs, npm, and others? [y|Y to install | * to exit]: "
read item
case $item in
    y|Y)
        echo "Installing..."
        installing
    ;;
    *)
        echo ":("
        exit -1
    ;;
esac

function installing() {
apt install -y npm nodejs mysql-server git
mysql_secure_installation

mysql << EOF
	create database usersDB2; 
	create user 'metidaSQL'@'localhost' identified with mysql_native_password by '123456';
	grant all privileges on usersDB2.* to 'metidaSQL'@'localhost';
EOF

}


