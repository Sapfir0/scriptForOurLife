#!bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "Start as root\n"
    exit -1
fi

logsDirectory=$(env|grep HOME|cut -c 6-)
met=$(pwd|grep -oP 'metida') #

echo $met
# function isFound() {
#     #проверить нашли ли мы метиду
# }

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
    SECVAR=$($VAR|cut -f1 -d' ')
    echo "Metida is found in $VAR"
    #echo "Lowest path $($VAR|cut -f1 -d' ')  will be used"
    cd $VAR #не сработает, если есть больше одной папки с метидой
    #cd ~/metida/ #kostil
    echo $(pwd)
}


if [[ -z "$met" ]] ; then # $met == null
    if [[ "$met" != "metida*" ]];then
        echo "You are not in metida project. Searching metida..."
        VAR=$(find ~/ -type d -name 'metida*')
        if [[ -z $VAR ]];then
			notFounded
        fi
    fi
fi

#we found metida
founded


#у этого файла будет сохраняться логи в env|grep HOME + /temp
cp ./autorunServer.sh /etc/profile.d/autorunServer.sh
cp ./ci.bash "$logsDirectory/bashFiles/ci.bash"
#смотри, копируешь файлик который будет автозапускать скрипт в etc/profile.d
#а файли с ci в папочку с метидой


#mini ci lol
lastVersion=$(git log --pretty=format:"%h" -1) #print index of last commit
echo "Последняя версия metida - $lastVersion" #не сработатет, т.к. гит лог выведет инфу о последнем ЛОКАЛЬНОМ коммите
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


