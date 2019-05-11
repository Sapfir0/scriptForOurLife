#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

from Mozilla import Mozilla


def configs():
    basicConfig = [ "urls = [ \"badUrl1\", \"badUrl2\", \"badUrln\" ] \n", "titles = [ \"badTitle1\", \"badTitle2\", \"badTitlen\" ]"  ]
    basicHelper = "\n#Specify the keywords for which the history will be deleted "
    if (not os.path.exists("config.py")):
        print("Configs file was not found")
        with open('config.py', 'w') as f:
            for i in basicConfig:
                f.write(i)
            f.write(basicHelper)
            f.close()
            print("Open config.py for further instructions")
  
configs()


m = Mozilla()
