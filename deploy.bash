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
		else  #we found metida
			SECVAR=$($VAR|cut -f1 -d' ')
			echo "Metida is found in $VAR"
			#echo "Lowest path $($VAR|cut -f1 -d' ')  will be used"
			cd $VAR #не сработает, если есть больше одной папки с метидой
			#cd ~/metida/ #kostil
			echo $(pwd)
		fi
	fi
fi

cp autorunServer.bash /etc/init.d/autorunServer.bash
chmod ugo+x /etc/init.d/autorunServer.bash
update-rc.d autorunServer.bash defaults #rewrite this 3 rows

#mini CL lol
lastVersion=$(git log --pretty=format:"%h" -1) #print index of last commit
echo "Последняя версия metida - $lastVersion"
bash ./autorunServer.bash $lastVersion

#working with docker

echo "Install docker and other[y|Y to install | * to exit]: "
read item
case $item in
	y|Y)
		echo "Installing..."
		bash ./installer.bash
	;;
	*) 
		echo ":("
		exit -1
	;;
esac


