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


def generation(arr: list, dlina: int) -> list:
	def generator(sgen: list, prev_index: int = -1):
		if len(sgen) < dlina:
			for i in range(prev_index + 1,len(arr)):
				sgen.append(arr[i])
				yield from generator(sgen, i)
				sgen.pop()
		else:
			yield sgen.copy()
	return [i for i in generator([])]

def generateRandomBunch(arr: list):
    bunch = random.choice(generation(arr, random.randrange(1, len(arr))))
    random.shuffle(bunch)
    return bunch
    
def generateColumns(tableName : str) -> str:
    table_keys = list(tables[tableName].keys())
    bunch_of_keys = generateRandomBunch(table_keys)
    columns_str = ""
    for i in range(len(bunch_of_keys)):
        columns_str += '\'' + bunch_of_keys[i] + '\'' + ('' if i == len(bunch_of_keys)-1 else ',')
    return columns_str


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
        columns = generateColumns(table)
        return f"{stringCommand} {columns} from {table}{selectStatement} WHERE {where};"
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



for i in range(50):
    funarray = [updateTemplate(), selectTemplate(),
            deleteTemplate(), insertTemplate()]
    print(random.choice(funarray))
