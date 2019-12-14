from math import factorial

morti1 = [100000,120000]
morti2 = [3,7]
morti3 = [3,6]

mortiList = [morti1, morti2, morti3]

for morti in mortiList:
    galacticus = [i for i in range(1, morti[0]+1)]
    x = factorial(morti[0])
    print(x%morti[1])
