import os
import sqlite3

userName = os.getlogin() 
path = os.path.join("C:",os.sep,"Users", userName , "AppData", "Roaming","Mozilla","Firefox","Profiles")
profile = os.listdir(path) 

if ( len(profile) > 1): #не уверен, что сработает
    print("Профилей много, будет выбран первый")

firefox_places = os.path.join("C:",os.sep,"Users", userName , "AppData", "Roaming","Mozilla","Firefox","Profiles", str(profile[0]) ,"places.sqlite")
print(firefox_places)

badSites = [ "'%pornhub.com/%'" ]

#блок конфигов окончен

conn = sqlite3.connect(firefox_places)
cursor = conn.cursor()


def deleteRecords(i):
    sql = "DELETE FROM moz_places WHERE url LIKE " + badSites[i] + ";"
    cursor.execute(sql)
    conn.commit()

def checkBadSites():
    for i in range(0, len(badSites)):
        sql = "SELECT url FROM moz_places WHERE url LIKE " + badSites[i] + ";"
        print("Ищем на " + badSites[i])
        cursor.execute(sql)
        if (cursor.fetchall() != [] ):
            print("Удаляем " + badSites[i])
            deleteRecords(i)
        else:
            print("Ты превосходен")

checkBadSites()