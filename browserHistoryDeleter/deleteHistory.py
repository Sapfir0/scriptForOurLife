#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sqlite3

def configs():
    basicConfig = [ "urls = [ \"badUrl1\", \"badUrl2\", \"badUrln\" ] \n", "titles = [ \"badTitle1\", \"badTitle2\", \"badTitlen\" ]"  ]
    basicHelper = "\n#Specify the keywords for which the history will be deleted "
    if (not os.path.exists("config.py")):
        print("Configs file was not found")
        with open('config.py', 'w') as f:
            for i in basicConfig:
                f.write(i)
            f.write(basicHelper)
            f.close()
            print("Open config.py for further instructions")
  
configs()
from config import urls, titles

userName = os.getlogin() 
path = os.path.join("C:",os.sep,"Users", userName , "AppData", "Roaming","Mozilla","Firefox","Profiles")
profile = os.listdir(path) 

if ( len(profile) > 1): #не уверен, что сработает
    print("A lots of profile, will be selected first")

firefox_places = os.path.join("C:",os.sep,"Users", userName , "AppData", "Roaming","Mozilla","Firefox","Profiles", str(profile[0]) ,"places.sqlite")
#print(firefox_places)

#блок конфигов окончен
print("I hope you use firefox")

conn = sqlite3.connect(firefox_places)
cursor = conn.cursor()

def isCountOfIteration(i):
    if (i == 0):
        urlOrTitle="url"
    elif (i == 1):
        urlOrTitle="title"
    else:
        urlOrTitle=None
    return urlOrTitle

def deleteRecords(object, typeOfDeleter ):
    urlOrTitle = isCountOfIteration(typeOfDeleter)

    sql = "DELETE FROM moz_places WHERE " + urlOrTitle + " LIKE " + object + ";"
    cursor.execute(sql)
    conn.commit()

def checkBadSites():
    data = [ urls, titles ] 
    i=0
    while (i < len(data) ):
        for j in data[i]:
            urlOrTitle = isCountOfIteration(i)
            sqlItemJ = "'%"+j+"%'"
            sql = "SELECT url FROM moz_places WHERE " + urlOrTitle + " LIKE " + sqlItemJ  + ";"
            print("Searching bad item... " + j )
            cursor.execute(sql)
            if (cursor.fetchall() != [] ):
                print("Deleting bad history " + j)
                deleteRecords(sqlItemJ, i)
            else:
                print("History is clear")
        i+=1


checkBadSites()
