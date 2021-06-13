def inInterval(mark, interval):
    return mark >= interval[0] and mark <= interval[1]

m3 = (61, 75)
m4 = (76, 89)
m5 = (77, 90)


first = [85, 90, 70, 76,76, 92, 85, 81, 76, ]

second = [64, 52, 64, 86, 76,  100, 90, 88, 85]

third = [76, 96, 90,  76, 76, 84, 93, 76, 93]

thouth = [61, 98, 72,61, 90,68,90,85,96,95]

thith = [100, 91, 88, 95,  78, 90, 80]

sixs = [85, 99, 95,  100, 100, 100, 100, 90]

sevens = [94, 96, 100, 90, 92, 100, 100, 96, 96]

eiths = [90, 83, 90, 95, 100, ]

allSemesters = [first, second, third, thouth, thith, sixs, sevens]

def getAvgIn5Marks():
    marks5 = []
    for sem in allSemesters:
        for mark in sem:
            if inInterval(mark, m3):
                marks5.append(3)
            elif inInterval(mark, m4):
                marks5.append(4)
            elif inInterval(mark, m5):
                marks5.append(5)
    return sum(marks5) / len(marks5)


def getAvg():
    def avg(lst): 
        return sum(lst) / len(lst) 

    avgInEachSem = list(map(lambda sem: avg(sem), allSemesters))

    # print(avgInEachSem)

    return avg(avgInEachSem)


print("Приведение к 5 балльной системе", getAvgIn5Marks())
print("Среднее 5 балльное", getAvg() /100*5)
print("Среднее 4 балльное", getAvg() /100*4)
print("Средний балл", getAvg())

