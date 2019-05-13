#!/bin/bash
#user3@cluster.vstu.ru

loginOnCluster="user3"
clustersUrl="@cluster.vstu.ru"
port="57322"
# ssh -p 57322 user3@cluster.vstu.ru

function connect() {
    ssh -p $port $loginOnCluster$clustersUrl
    expect "user3@cluster.vstu.ru's password: "
    send -- "userIntelPhi3\r"
}

function disconnect() {
    exit
}

# function firstArgumentIsNull() {
    
# }

function pushToServer() { #$1 - что постить(локалка), $2, куда постить(серв)
    scp -P $port $1 $loginOnCluster$clustersUrl:$2
}

function getFromServer() { #$1 - что получаем(сервер), $2 - куда получаем(локалка)
    scp -P $port $loginOnCluster$clustersUrl:$1 $2
}

function connectToNode(){
    if [[ $1 <30 || $1 > 53 ]]; then
        echo "This is undefined node"
        return
    fi
    ssh node$1
}

function pushMyProjectToCluster() {
    if ! [ -d ~/projectsFromAlexander ]; then
        mkdir ~/projectsFromAlexander
    fi
    pushToServer $1 ~/projectsFromAlexander
}

# function runProjectOnCluster() {

# }
connect
#pushToServer "./../README.md" "~"
#getFromServer "~/README.md" "./"
#userIntelPhi3