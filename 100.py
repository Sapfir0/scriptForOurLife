import random

tables = {
    'table1': ['column11', 'column21'],
    'table2': ['column12', 'column22'] # table: columns
}

for array in tables.values():
    array.append("*")

def abstractComand(command, table='', selectStatement=''):
    if not table:
        table = random.choice(list(tables.keys()))
        operationsColumn = random.choice(tables[table]) # пока допустим что только один оператор
    return f"{command}{operationsColumn} from {table}{selectStatement};"


def updateTemplate():
    return abstractComand("UPDATE ")


def deleteTemplate():
    return abstractComand("DELETE ")


def insertTemplate():
    return abstractComand("INSERT ")


def selectTemplate():
    return abstractComand("SELECT ")


print(selectTemplate())