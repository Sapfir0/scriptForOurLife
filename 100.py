import enum
import random
import datetime

tables = {
    'Canteen': {
        'id': int,
        'title': str,
        'workingHours': int,
        "description": str,
        "phoneNumber": int
        },
    'CanteenWorker': {
        'id': int,
        'fullName': str,
        'canteenId': int
        },
    'Courier': {
        'id': int,
        'title': str,
        'workingHours': int,
        "description": str,
        "phoneNumber": int
        },
    'Order': {
        'id': int,
        'orderNumber': int,
        'orderTime': int,
        "quantityDishes": int,
        "status": str,
        "amountPayable": int,
        "canteenWorkerId": int,
        "courierId": int,
        "clientId": int
        },
}

insertUpdateData = ["Александроус", "Андреев", "Леха", "Колян"]


# def nekitFunc(setsLength, columntsCount):  #k,n
#     def incr(listok, max):
#         if not listok:
#             return False
#         elif 
#     listok = []
    


def generateWhereStatements():
    whereArrays = []
    for table in tables.values():
        for column in table:
            if column != "*":
                columnType = table[column]
                if columnType == str:
                    whereElements = f"{random.choice(insertUpdateData)}"
                elif columnType == int:
                    whereElements = random.randint(0, 1000)
                elif columnType == float:
                    whereElements = random.random()
                else:
                    whereElements = None
                whereArrays.append(f"{column}={whereElements}")
    return random.choice(whereArrays)


def abstractComand(command, table='', selectStatement='') -> str:
    stringCommand = random.choice(command.value)
    if not table:
        table = random.choice(list(tables.keys()))
        # пока допустим что только один оператор
        operationsColumn = random.choice(list(tables[table].values()))
    where = generateWhereStatements()

    if command == sql.DELETE:
        return f"{stringCommand} from {table}{selectStatement} WHERE {where};"
    elif command == sql.INSERT:
        return f"{stringCommand} INTO {table} VALUES ({where});"
    elif command == sql.SELECT:
        return f"{stringCommand} from {table}{selectStatement} WHERE {where};"
    elif command == sql.UPDATE:
        return f"{stringCommand} {table} SET {{ }};"


def updateTemplate():
    return abstractComand(sql.UPDATE)


def deleteTemplate():
    return abstractComand(sql.DELETE)


def insertTemplate():
    return abstractComand(sql.INSERT)


def selectTemplate():
    return abstractComand(sql.SELECT)


class sql(enum.Enum):
    SELECT = "SELECT",
    UPDATE = "UPDATE",
    DELETE = "DELETE",
    INSERT = "INSERT",
    ZATICHKA = ""


funarray = [updateTemplate(), selectTemplate(),
            deleteTemplate(), insertTemplate()]

for i in range(50):
    print(random.choice(funarray))
