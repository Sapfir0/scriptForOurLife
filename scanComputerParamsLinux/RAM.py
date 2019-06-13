#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import os

class RAM:
    #def __init__(self):


    def getUnusedRAM(self):
        ram = "free -ht | grep \"G\" "
        data = os.popen(ram).read()
        load = data.splitlines()[1][12:].strip()
        #digit=re.findall(r"\d+(G|M)", load)

        #print(digit)

