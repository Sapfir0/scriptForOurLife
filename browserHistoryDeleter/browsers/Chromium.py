import os
import sqlite3
if os.path.exists("config.py"):
    from config import urls, titles
from browsers.browser import Browser


class ChromiumSnap(Browser):
    profilePath = None



    def checkBadSites(self):
        for url in urls:
            if self.selectQuery("url", url):
                self.deleteQuery("url", url)
            else:
                print("History is clear")

        for title in titles:
            if self.selectQuery("title", title):
                self.deleteQuery("title", title)
            else:
                print("History is clear")

    def findDatabaseFile(self):
        databasePath = os.path.join(os.path.expanduser("~"), "snap", "chromium",
                            "821", ".config", "chromium", "Default", "History")  # TODO жесткое определение профиля 821

        return databasePath