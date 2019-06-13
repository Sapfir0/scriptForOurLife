#!/usr/bin/python3
# -*- coding: utf-8 -*-

# тут маленькая линукс вики

import os
import subprocess
from subprocess import PIPE
import re

    

def getTempOfCPU():
    TempofCPU = "sensors | egrep \"Core\" "
    data = os.popen(TempofCPU).read()
    sum=0.
    counter = int(os.popen("sensors | egrep 'Core' -o | wc -l").read()) #вернет количество ядер
    for i in range(0, counter): #второе число - количество совпадений с шаблоном
        tempOfCore=data.splitlines()[i][16:20].strip()
        sum+=float(tempOfCore)
    result = sum / counter
    print("Average temperature of CPU: " + str(result))
    return result

def getTempOfDiscs(): 
    TempOfHDD = "sudo hddtemp /dev/sda" #надо понять как поступать с правами админа
    data = os.popen(TempOfHDD).read()
    
    print("Temperature of HDD:" + data[-6:-4]) #предположим что температура будет выглядтеть таким образом 00.0


def getLoadOfCpuByUptime():
    # Загрузка проца, нужно как-то определить, пока я не сдал физику #АХАХАХ
    #пример выдаваемой строки
    # user(время на процессы юзера), system(системные процессы), niced(не приоритетные процессы юзера), idle(вроемя на простой ядра), 
    uptime="uptime"
    data = os.popen(uptime).read() # 23:10:39 up  6:19,  1 user,  load average: 1,05, 0,89, 0,79
    digit=re.findall(r"\d+", data)[-6:]
    print( "Current load: " + digit[0] + "." + digit[1] )
    print( "5-mintute load: " + digit[2] + "." + digit[3] )
    print( "15-mintute load: " + digit[4] + "." + digit[5] )
    return digit
    # (инфа с хабра https://habr.com/ru/post/216827/)
    # если нагрузка больше 1 для одноядерного проца, то все пиздец, ты упал
    # 1 на каждое ядро


def getLoadOfCpuByIostat():
    #также можно юзнуть это
    cpuLoad = "iostat -c | grep \"avg\" -A 1"
    data = os.popen(cpuLoad).read()
    load = data.splitlines()[1]
    digit=re.findall(r"\d+", load)
    list=[]
    for i in range(0, len(digit), 2):
        list.append( digit[i] + "."  + digit[i+1] ) #avg-cpu:  %user   %nice %system %iowait  %steal   %idle
    # первые 3 пункта - загруженность проца, остальные - свободные % проца
    usedResources= float(list[0]) + float(list[1]) + float(list[2])
        
    print("CPU load on " + str(usedResources) + "%")
    return usedResources



getTempOfDiscs()
getTempOfCPU()
getLoadOfCpuByUptime()
getLoadOfCpuByIostat()



howManyCoreIHave = "cat /proc/cpuinfo | grep \"cpu cores\" " #есть еще лулзный варик в начале 



