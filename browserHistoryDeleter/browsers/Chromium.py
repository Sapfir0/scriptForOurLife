import os
import sqlite3
if os.path.exists("config.py"):
    from config import urls, titles


class ChromiumSnap():
    profilePath = None

    def __init__(self):
        self.profilePath = os.path.join(os.path.expanduser("~"), "snap", "chromium",
                                        "821", ".config", "chromium", "Default")  # TODO жесткое определение профиля 821

    def query(self):
        databasePath = os.path.join(self.profilePath, "History")
        conn = sqlite3.connect(databasePath)
        cursor = conn.cursor()

    def checkBadSites(self):

