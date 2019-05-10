#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "Start as root\n"
    exit -1
fi

metidaDir=$(pwd|grep -oP 'metida'); #есть ли в текущей папке метида
bashDir=$(pwd); #исходная директория этого скриптового проекта

#working with packages
bash "$bashDir/installers.bash"


function getPermissionTo() {
    chmod 0777 -R "$1"
}
function getRecursionPermissionTo() {
    chmod -R u=rw,go=r,a+X "$1"
}

function isFound() {
	if [[ -z "$metidaDir" ]] ; then # $met == null
		return false;
	fi
	return true;
}

function notFounded() {
    echo "Metida didnt found. Download?"
    read item
    case $item in
        n|N)
            echo ":("
            exit -1
        ;;
        *)
            cd ~/
            echo "Downloading..."
            git clone https://github.com/avdosev/metida.git
            getRecursionPermissionTo "$metidaDir" #give to all, maximum permision
            cd ./metida
            npm install
            npm start

        ;;
    esac
}


function founded() {
    parsedMetidaDir=$($1|cut -f1 -d' ')
    echo "Metida is found in $1"
    #echo "Lowest path $($metidaDir|cut -f1 -d' ')  will be used"
    cd $1 #не сработает, если есть больше одной папки с метидой
    echo "We are in $(pwd)"
    npm start 
}


if [[ !isFound ]] ; then # $met == null
    if [[ "$metidaDir" != "metida*" ]];then
        echo "You are not in metida project. Searching metida...";
        metidaDir=$(find ~/ -type d -name 'metida*');
        if [[ -z $metidaDir ]];then
			notFounded
        fi
    fi
fi

#we found metida
founded $metidaDir #да, это аргумент функции, да это вызов функции

#на этом моменте мы в папке с метидой
if ! [[ -d  "$metidaDir/bashFiles" ]]; then
    mkdir "$metidaDir/bashFiles" 
    getPermissionTo "$metidaDir/bashFiles"
fi
cp "$bashDir/autorunServer.sh" "/etc/profile.d/autorunServer.sh"
bash "/etc/profile.d/autorunServer.sh" "$metidaDir/bashFiles/" #первый запуск чтобы закинуть туда путь до директории с запускаемым скриптом
cp "$bashDir/ci.bash" "$metidaDir/bashFiles/ci.bash"
getPermissionTo "$metidaDir/bashFiles/ci.bash"


#mini ci lol
lastVersion=$(git log --pretty=format:"%h" -1) #не сработатет, т.к. гит лог выведет инфу о последнем ЛОКАЛЬНОМ коммите
echo "Последняя локальная версия metida - $lastVersion" 
bash "$bashDir/ci.bash" $lastVersion




