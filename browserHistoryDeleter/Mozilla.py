import os
import sqlite3

if (os.path.exists("config.py")):
    from config import urls, titles
else:
    exit

class Mozilla:
    def __init__(self):
        userName = os.getlogin() 
        path = os.path.join("C:",os.sep,"Users", userName , "AppData", "Roaming","Mozilla","Firefox","Profiles")
        profile = os.listdir(path) 

        if ( len(profile) > 1): #не уверен, что сработает
            print("A lots of profile, will be selected first")

        firefox_places = os.path.join("C:",os.sep,"Users", userName , "AppData", "Roaming","Mozilla","Firefox","Profiles", str(profile[0]) ,"places.sqlite")
        #блок конфигов окончен

        self.connection = sqlite3.connect(firefox_places)
        self.cursor = self.connection.cursor()

        self.checkBadSites()


    def deleteRecords(self, object, typeOfDeleter ):
        urlOrTitle = self.isCountOfIteration(typeOfDeleter)

        sql = "DELETE FROM moz_places WHERE " + urlOrTitle + " LIKE " + object + ";"
        self.cursor.execute(sql)
        self.connection.commit()

    def checkBadSites(self):
        data = [ urls, titles ] 
        i=0
        while (i < len(data) ):
            for j in data[i]:
                urlOrTitle = self.isCountOfIteration(i)
                sqlItemJ = "'%"+j+"%'"
                sql = "SELECT url FROM moz_places WHERE " + urlOrTitle + " LIKE " + sqlItemJ  + ";"
                print("Searching bad item... " + j )
                self.cursor.execute(sql)
                if (self.cursor.fetchall() != [] ):
                    print("Deleting bad history " + j)
                    self.deleteRecords(sqlItemJ, i)
                else:
                    print("History is clear")
            i+=1

    def isCountOfIteration(self,i):
        if (i == 0):
            urlOrTitle="url"
        elif (i == 1):
            urlOrTitle="title"
        else:
            urlOrTitle=None
        return urlOrTitle

    
