#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import pwd
import sqlite3
from sys import platform

if os.path.exists("config.py"):
    from config import urls, titles


def config():
    os.getlogin = lambda: pwd.getpwuid(os.getuid())[0]
    userName = os.getlogin()
    if platform == "win32":
        path = os.path.join("C:", os.sep, "Users", userName, "AppData", "Roaming", "Mozilla", "Firefox", "Profiles")
        profile = os.listdir(path)

        if len(profile) > 1:  # не уверен, что сработает
            print("A lots of profile, will be selected first")

        firefox_places = os.path.join("C:", os.sep, "Users", userName, "AppData", "Roaming", "Mozilla",
                                      "Firefox", "Profiles", str(profile[0]), "places.sqlite")
        return firefox_places
    elif platform == "linux" or platform == "linux2":
        path = os.path.join("/", "home", userName, ".mozilla", "firefox", 'profiles.ini')
        cmd = "cat " + path + " | grep Default | head -1 "
        profileDir = os.popen(cmd).read()[8:]
        profileDir = profileDir.strip()
        firefox_places = os.path.join("/", "home", userName, ".mozilla", "firefox", profileDir, "places.sqlite")
        return firefox_places
    else:
        print("Unknown platform")
        exit()


class Mozilla:
    def __init__(self):
        firefox_places = config()
        print(firefox_places)
        self.connection = sqlite3.connect(firefox_places)
        self.cursor = self.connection.cursor()

        self.checkBadSites()

    def deleteRecords(self, sqlItemJ, typeOfDeleter):
        urlOrTitle = isCountOfIteration(typeOfDeleter)

        sql = "DELETE FROM moz_places WHERE " + urlOrTitle + " LIKE " + sqlItemJ + ";"
        self.cursor.execute(sql)
        self.connection.commit()

    def checkBadSites(self):
        data = [urls, titles]
        for i, item in enumerate(data):
            for j in data[i]:
                urlOrTitle = isCountOfIteration(i)
                sqlItemJ = "'%" + j + "%'"
                sql = "SELECT url FROM moz_places WHERE " + urlOrTitle + " LIKE " + sqlItemJ + ";"
                print("Searching bad item... " + j)
                self.cursor.execute(sql)
                if self.cursor.fetchall():
                    print("Deleting bad history " + j)
                    self.deleteRecords(sqlItemJ, i)
                else:
                    print("History is clear")


def isCountOfIteration(i):
    if i == 0:
        urlOrTitle = "url"
    elif i == 1:
        urlOrTitle = "title"
    else:
        urlOrTitle = None
    return urlOrTitle
