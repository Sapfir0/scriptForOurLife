#!/bin/sh

if test -z "$1"; then #if argc < 1
	echo "No arguments"
else
	echo $1 > pathToMetida.log
fi

pathToMetida=$(cat pathToMetida.log) #считаем путь до метиды из файла
#cd ~/ ;
echo "$pathToMetida"

while (true)
do
    bash "$pathToMetida/ci.bash"; #запустим скрипт
    sleep 3600; #ждем час
done;
