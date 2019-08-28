from abc import ABC, abstractmethod
import sqlite3

class Browser(ABC):
    profilesPath = None

    @abstractmethod
    def findDatabaseFile(self):
        pass

    def __init__(self):
        self.profilesPath = self.findDatabaseFile()
        print(self.profilesPath)
        self.connection = sqlite3.connect(self.profilesPath)
        self.cursor = self.connection.cursor()
        self.checkBadSites()

    def deleteQuery(self,  whereParam, likeParam):
        return self.sql('delete', whereParam, likeParam)

    def selectQuery(self,  whereParam, likeParam):
        return self.sql('select',  whereParam, likeParam)

    def sql(self, mode, whereParam, likeParam):
        regexp = "'%" + likeParam + "%'"
        if mode == 'select':
            print("Searching bad item... " + likeParam)
            sql = "SELECT url FROM {} WHERE {} LIKE {};".format(self.tableName, whereParam, regexp)
            try:
                self.cursor.execute(sql)
            except sqlite3.OperationalError:  # задумка отловить исключение database is locked
                print("Close browser")
                exit(-1)
            result = self.cursor.fetchall()
            return result
        if mode == 'delete':
            print("Deleting bad history " + likeParam)
            sql = "DELETE FROM {} WHERE {} LIKE {};".format(self.tableName, whereParam, regexp)
            self.cursor.execute(sql)
            self.connection.commit()
