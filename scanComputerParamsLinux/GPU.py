#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import re

class GPU:

    def getTempOfGPU(self):
        TempofGPU = "sensors | egrep \"PCI\" -A 1 "
        data = os.popen(TempofGPU).read()
        result = data.splitlines()[1][15:24].strip()[:-4]
        print("Temperature of GPU: " + str(result))
        return result


