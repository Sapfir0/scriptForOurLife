#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

class Discs:

    def getTempOfDiscs(self): 
        TempOfHDD = "sudo hddtemp /dev/sda" #надо понять как поступать с правами админа
        data = os.popen(TempOfHDD).read()
        
        print("Temperature of HDD:" + data[-6:-4]) #предположим что температура будет выглядтеть таким образом 00.0


