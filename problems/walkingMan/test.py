# Задача: если есть сетка кварталов и человек может идти в любую сторону с вероятностью 0.25. 
# Какая вероятность что он не уйдет дальше 2 перекрестков от начального?

import random
from random import randint

def generateRandomMoving():
    xmoving = 0
    ymoving = 0

    if random.choice([True, False]):
        while ymoving == 0:
            ymoving = randint(-1, 1)
    else:
        while xmoving == 0:
            xmoving = randint(-1, 1)

    return xmoving, ymoving


def faraway(cd: list):
    counter = abs(cd[0]) + abs(cd[1])
    return counter


def experiment(N=10, M=2):
    startCoordinates = [0, 0]

    for i in range(1, N):
        x, y = generateRandomMoving()
        startCoordinates[0] += x
        startCoordinates[1] += y

    currentGeo = faraway(startCoordinates)
    return currentGeo <= M


def getProbability(iterationmax=10000):
    probabilityNearTheHouse = 0
    for i in range(iterationmax):
        if experiment():
            probabilityNearTheHouse += 1
    print(probabilityNearTheHouse / iterationmax)
            
                
getProbability()