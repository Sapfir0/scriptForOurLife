#!/bin/sh

logsDirectory=$(env|grep HOME|cut -c 6-) ;
cd logsDirectory ;

while (true)
do
    bash ./ci.bash;
    sleep 3600;
done;
