#!bin/bash

#rerun after reboot -> start server as fast as it can

echo $1 > HEADptr.log #only for first run

HEAD < HEADptr #read from file
lastVersion=$(git log --pretty=format:"%h" -1) #print index of last commit

if [[ "$HEAD" != "$lastVersion"]]; then
    echo "Master branch have been updated, download..."
    VAR=find ~/ -type d -name 'metida*'
    cd $VAR
    git pull
fi
