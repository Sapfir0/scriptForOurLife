#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import RAM
from CPU import CPU
from RAM import RAM
from Discs import Discs



#getUnusedRAM()
scanCpu = CPU(); ScanRam = RAM(); scanHdd = Discs()

while True:
    scanHdd.getTempOfDiscs()
    scanCpu.getTempOfCPU()
    scanCpu.getLoadOfCpuByUptime()
    scanCpu.getLoadOfCpuByIostat()
    print("---")
    time.sleep(5)


howManyCoreIHave = "cat /proc/cpuinfo | grep \"cpu cores\" " #есть еще лулзный варик в начале 



