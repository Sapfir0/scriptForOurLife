#!bin/bash

#rerun after reboot -> start server as fast as it can
if test -z "$1"; then #if argc < 1
	echo "No arguments"
else
	echo $1 > HEADptr.log
fi

chmod o+r HEADptr.log
chmod o+w HEADptr.log
HEAD=$(cat HEADptr.log) 
#read $HEAD < HEADptr #read from file
lastVersion=$(git log --pretty=format:"%h" -1) #print index of last commit

if [[ "$HEAD" != "$lastVersion" ]]; then
    echo "Master branch have been updated, download..."
    VAR=$(find ~/ -type d -name 'metida*')
    echo $HEAD > HEADptr.log
    #cd $VAR
    cd ~/metida
    git pull
fi
