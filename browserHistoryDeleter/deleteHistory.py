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

    print("DELETE FROM moz_places WHERE " + urlOrTitle + " LIKE " + object + ";")
    sql = "DELETE FROM moz_places WHERE " + urlOrTitle + " LIKE " + object + ";"
    cursor.execute(sql)
    conn.commit

def checkBadSites():
    data = [ urls, titles ] 
    i=0
    while (i < len(data) ):
        for j in data[i]:
            urlOrTitle = isCountOfIteration(i)
            sql = "SELECT url FROM moz_places WHERE " + urlOrTitle + " LIKE " + j + ";"
            print("SELECT url FROM moz_places WHERE " + urlOrTitle + " LIKE " + j + ";")
            print("Searching bad item... " + j)
            cursor.execute(sql)
            print(cursor.fetchone())
            if (cursor.fetchall() != [] ):
                print("Удаляем " + j)
                deleteRecords(j, i)
            else:
                print("History is clear")
        i+=1
        #print("Итерация закончена")


checkBadSites()
# i=0
# data = [ urls, titles ] 

# while (i < len(data) ):
#     for j in data[i]:
#         print(j)
#     i+=1
#     print(i)
#     print("Итерация закончена")



            # if (i==0 and bool): #ебать я пишу мусорный код
            #     bool=False
            #     if (cursor.fetchall() != [] ):
            #         print("Удаляем " + item[i])
            #         deleteRecords(i, "url" )
            #     else:
            #         print("History is clear")
            # elif (i==0):
            #     if (cursor.fetchall() != [] ):
            #         print("Удаляем " + item[i])
            #         deleteRecords(i, "title" )
            #     else:
            #         print("History is clear")

