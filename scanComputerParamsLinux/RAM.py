#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import os

class RAM:
    #def __init__(self):


    def getUnusedRAM(self):
        ram = "free -ht"
        data = os.popen(ram).read()
        load = data.splitlines()[3]
        #digit=re.findall(r"\d+(G|M)", load)
        allMemory = load[11:27].strip()[:-1]
        loadedMemory = load[27:41].strip()[:-1]
        freeMemory = load[27:41].strip()[:-1]
        print("allMemory: " + allMemory)
        print("loadedMemory: " + loadedMemory)
        print("freeMemory: " + freeMemory)

        return [allMemory, loadedMemory, freeMemory]

