import os
if os.path.exists("config.py"):
    from config import urls, titles
from browsers.browser import Browser


class ChromiumSnap(Browser):
    profilePath = None

    columnWithUrl = "url"
    columnWithKeywords = "term"

    tableWithUrls = "urls"  # тут 2 таблицы, в которых
    tableWithKeywords = 'keyword_search_terms'

    # Shortcuts / select text from omni_box_shortcuts ;

    def checkBadSites(self):
        for url in urls:
            if self.selectQuery(self.columnWithUrl, self.tableWithUrls, self.columnWithUrl, url):
                self.deleteQuery(self.tableWithUrls, self.columnWithUrl, url)
            else:
                print("History is clear")

        for title in titles:
            if self.selectQuery(self.columnWithKeywords, self.tableWithKeywords, self.columnWithKeywords, title):
                self.deleteQuery(self.tableWithKeywords, self.columnWithKeywords, title)
            else:
                print("History is clear")

    def findDatabaseFile(self):
        databasePath = os.path.join(os.path.expanduser("~"), "snap", "chromium",
                            "821", ".config", "chromium", "Default", "Shortcuts")  # TODO жесткое определение профиля 821

        return databasePath
