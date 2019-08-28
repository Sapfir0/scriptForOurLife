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

    def deleteQuery(self, table, whereParam, likeParam):
        return self.sql('delete', table, whereParam, likeParam)

    def selectQuery(self, selectParam, table, whereParam, likeParam):
        return self.sql('select', table, whereParam, likeParam, selectParam=selectParam)

    def sql(self, mode, table, whereParam, likeParam, selectParam=None):
        regexp = "'%" + likeParam + "%'"
        if mode == 'select':
            print("Searching bad item... " + likeParam)
            sql = "SELECT {} FROM {} WHERE {} LIKE {};".format(selectParam, table, whereParam, regexp)
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        if mode == 'delete':
            print("Deleting bad history " + likeParam)
            sql = "DELETE FROM {} WHERE {} LIKE {};".format(table, whereParam, regexp)
            self.cursor.execute(sql)
            self.connection.commit()
