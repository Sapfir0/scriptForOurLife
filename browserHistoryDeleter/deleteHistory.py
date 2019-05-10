import os
import sqlite3
from config import urls, titles
from threading import Thread


userName = os.getlogin() 
path = os.path.join("C:",os.sep,"Users", userName , "AppData", "Roaming","Mozilla","Firefox","Profiles")
profile = os.listdir(path) 

if ( len(profile) > 1): #не уверен, что сработает
    print("Профилей много, будет выбран первый")

firefox_places = os.path.join("C:",os.sep,"Users", userName , "AppData", "Roaming","Mozilla","Firefox","Profiles", str(profile[0]) ,"places.sqlite")
print(firefox_places)

#блок конфигов окончен

conn = sqlite3.connect(firefox_places)
cursor = conn.cursor()


def deleteRecords(i, typeOfDeleter ):
    #str=str(titles[i]) if typeOfDeleter == "title" else str=str(urls[i])
    if (typeOfDeleter == "title"):
        str=titles[i]
    else:
        str=urls[i]

    sql = "DELETE FROM moz_places WHERE" + typeOfDeleter + "LIKE " + str + ";"
    cursor.execute(sql)
    conn.commiturls

def checkBadSites():
    data = [ urls, titles ]
    for item in data:
        for i in range(0, len(item)):
            sql = "SELECT url FROM moz_places WHERE url LIKE " + item[i] + ";"
            print("Searching bad item... " + item[i])
            cursor.execute(sql)
            if (cursor.fetchall() != [] ):
                print("Удаляем " + item[i])
                deleteRecords(i, "url")
            else:
                print("History is clear")


checkBadSites()