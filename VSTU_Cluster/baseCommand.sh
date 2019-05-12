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

function checkGetPushArgument() {
    if [[ -z "$1"  ]];then
        echo "First argument is null"
        return -1
    fi
    if [[ -z "$2"  ]];then
        echo "Second argument is null, but will be used current path"
        outputPath = "./"
    fi
    return outputPath
}

function pushToServer() { #$1 - что постить(локалка), $2, куда постить(серв)
    echo $(checkGetPushArgument "$1" "$2")
    outputPath = $(checkGetPushArgument "$1" "$2")

    scp -P $port "$1" "$loginOnCluster""$clustersUrl":"$outputPath"
}

function getFromServer() { #$1 - что получаем(сервер), $2 - куда получаем(локалка)
    outputPath = "$(checkGetPushArgument "$1" "$2")"
    echo $outputPath
    
    scp -P $port "$loginOnCluster""$clustersUrl":"$1" "$outputPath"
}

function connectToNode()  {
    if [[ $1 <30 || $1 > 53 ]]; then
        echo "This is undefined node"
        return
   fi
    ssh node$1
}

#pushToServer "./../README.md" "~"
getFromServer 
#userIntelPhi3