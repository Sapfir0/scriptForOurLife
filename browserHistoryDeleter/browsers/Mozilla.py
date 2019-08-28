#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import pwd
import sqlite3
from sys import platform

if os.path.exists("config.py"):
    from config import urls, titles





class Mozilla:
    def __init__(self):
        firefox_places = config()
        print(firefox_places)
        self.connection = sqlite3.connect(firefox_places)
        self.cursor = self.connection.cursor()

        self.checkBadSites()

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

    def deleteQuery(self, whereParam, likeParam):
        return self.sql('delete', whereParam, likeParam)

    def selectQuery(self, whereParam, likeParam):
        return self.sql('select', whereParam, likeParam)

    def sql(self, mode, whereParam, likeParam):
        regexp = "'%" + likeParam + "%'"
        if mode == 'select':
            print("Searching bad item... " + likeParam)
            sql = "SELECT url FROM moz_places WHERE " + whereParam + " LIKE " + regexp + ";"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        if mode == 'delete':
            print("Deleting bad history " + likeParam)
            sql = "DELETE FROM moz_places WHERE " + whereParam + " LIKE " + regexp + ";"
            self.cursor.execute(sql)
            self.connection.commit()

    def findProfilesDir(self):
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

