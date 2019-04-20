#!bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "Start as root\n"
    exit -1
fi

logsDirectory=$(env|grep HOME|cut -c 6-); #директория вроде /home/user
metidaDir=$(pwd|grep -oP 'metida'); #есть ли в текущей папке метида
bashDir=$(pwd); 

echo $met

function notFounded() {
    echo "Metida didnt found. Download?"
    read item
    case $item in
        n|N)
            echo ":("
            exit -1
        ;;
        *)
            cd $logsDirectory #мы в домашней директории
            echo "Downloading..."
            git clone https://github.com/avdosev/metida.git
        ;;
    esac
}

function founded() {
    parsedMetidaDir=$($metidaDir|cut -f1 -d' ')
    echo "Metida is found in $metidaDir"
    #echo "Lowest path $($metidaDir|cut -f1 -d' ')  will be used"
    cd $metidaDir #не сработает, если есть больше одной папки с метидой
    #cd ~/metida/ #kostil
    echo $(pwd)
}


if [[ -z "$metidaDir" ]] ; then # $met == null
    if [[ "$metidaDir" != "metida*" ]];then
        echo "You are not in metida project. Searching metida..."
        VAR=$(find ~/ -type d -name 'metida*')
        if [[ -z $VAR ]];then
			notFounded
        fi
    fi
fi

#we found metida
founded

echo $(pwd)

cp "bashDir/autorunServer.sh" "/etc/profile.d/autorunServer.sh"
cp "bashDir/ci.bash" "$logsDirectory/bashFiles/ci.bash"

#mini ci lol
lastVersion=$(git log --pretty=format:"%h" -1) #не сработатет, т.к. гит лог выведет инфу о последнем ЛОКАЛЬНОМ коммите
echo "Последняя версия metida - $lastVersion" 
bash ./ci.bash $lastVersion



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


