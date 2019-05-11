#!/bin/bash
#user3@cluster.vstu.ru

loginOnCluster="user3"
clustersUrl="@cluster.vstu.ru"
port="57322"

function connect() {
    ssh -p $port $loginOnCluster$clustersUrl
}

function disconnect() {
    exit
}


function pushToServer() { #$1 - что постить(локалка), $2, куда постить(серв)
    scp -P $port $1 $loginOnCluster$clustersUrl:$2
}

function getFromServer() { #$1 - что получаем(сервер), $2 - куда получаем(локалка)
    scp -P $port $loginOnCluster$clustersUrl:$1 $2
}

function connectToNode(){
    if [[ $1 <30 || $1 > 53 ]]
        echo "This is undefined node"
        return
    ssh node$1
}

#pushToServer "./../README.md" "~"
#getFromServer "~/README.md" "./"
#userIntelPhi3