#!bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "Start as root\n"
	exit -1
fi

#if [[$(whoami) == sapfir]];then
#	./setLocale.bash
#fi

met=$(pwd|grep -oP 'metida') #if 
echo $met
if [[ -z "$met" ]] ; then # $met == null
	if [[ "$met" != "metida*" ]];then
		echo "You are not in metida project. Searching metida..."
		VAR=$(find ~/ -type d -name 'metida*')
		echo "Metida is found in $VAR"
		cd $VAR
		if [[ -z $VAR ]];then
			echo "Metida didnt found. Download?"
			read item
			case $item in
				n|N)
					echo ":("
					exit -1
					;;
				*) 
					echo "Downloading..."
					git clone https://github.com/avdosev/metida.git
					;;
			esac
		fi
	fi
fi

#cp autorunServer.bash /etc/init.d/autorunServer.bash
#chmod ugo+x /etc/init.d/autorunServer.bash
#update-rc.d autorunServer.bash defaults #rewrite this 3 rows

#mini CL lol
lastVersion=$(git log --pretty=format:"%h" -1) #print index of last commit
echo "Последняя версия metida - $lastVersion"
bash ./autorunServer.bash $lastVersion

#working with docker

#apt update
#apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
#apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
#apt update && apt-cache policy docker-engine

#packages = {
#	nodejs, npm, mysql-server, docker-engine }

#apt install -y $packages

#need create special account for working with DB
#mysql_secure_installation

#mysql -u whoami -p1 <<EOF
#create database usersDB; 
#create table usersDB.users (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, email VARCHAR(50), login VARCHAR(25), password VARCHAR(100) created_at datetime, updated_at datetime);
#create user 'metidaSQL'@'localhost' identified by '1234';
#grant all privileges on usersDB.users to 'metidaSQL'@'localhost';
#alter user 'metidaSQL'@'localhost' identified WITH mysql_native_password BY '1234';
#EOF


