#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import pwd
import sqlite3
from sys import platform
from browsers.browser import Browser

if os.path.exists("config.py"):
    from config import urls, titles


class Mozilla(Browser):
    profilesPath = None
    # как называются в текущем браузере посещенные урлы и ключевые слова
    labelingUrl = "url"
    labelingKeywords = "title"

    tableName = "moz_places" # название таблицы с данными

    def checkBadSites(self):
        for url in urls:
            if self.selectQuery(self.labelingUrl, url):
                self.deleteQuery(self.tableName, self.labelingUrl, url)
            else:
                print("History is clear")

        for title in titles:
            if self.selectQuery(self.labelingKeywords, title):
                self.deleteQuery(self.tableName, self.labelingKeywords, title)
            else:
                print("History is clear")

    def findDatabaseFile(self):
        os.getlogin = lambda: pwd.getpwuid(os.getuid())[0]
        userName = os.getlogin()
        if platform == "win32":
            path = os.path.join("C:", os.sep, "Users", userName, "AppData", "Roaming", "Mozilla", "Firefox", "Profiles")
            profiles = os.listdir(path)

            if len(profiles) > 1:
                print("A lots of profile, will be selected first")

            firefox_places = os.path.join("C:", os.sep, "Users", userName, "AppData", "Roaming", "Mozilla",
                                          "Firefox", "Profiles", str(profiles[0]), "places.sqlite")
            return firefox_places
        elif platform == "linux" or platform == "linux2":
            path = os.path.join(os.path.expanduser("~"), ".mozilla", "firefox", 'profiles.ini')
            cmd = "cat " + path + " | grep Default | head -1 "
            profileDir = os.popen(cmd).read()[8:]
            profileDir = profileDir.strip()
            firefox_places = os.path.join("/", "home", userName, ".mozilla", "firefox", profileDir, "places.sqlite")
            return firefox_places
        else:
            print("Unknown platform")
            exit()

