import random
import enum
class sql(enum.Enum):
    SELECT = "SELECT",
    UPDATE = "UPDATE",
    DELETE = "DELETE",
    INSERT = "INSERT",
    ZATICHKA = ""

tables = {
    'table1': ['column11', 'column21'],
    'table2': ['column12', 'column22'] # table: columns
}

insertUpdateData = [1, "foo", 2.4] # можно сделать тупо проверку по типу

for array in tables.values():
    array.append("*")

def abstractComand(command, table='', selectStatement='') -> str:
    if not table:
        table = random.choice(list(tables.keys()))
        operationsColumn = random.choice(tables[table]) # пока допустим что только один оператор
    if command == sql.DELETE:
        return f"{command.value[0]} from {table}{selectStatement};"
    elif command == sql.INSERT:
        #values = 
        return f"{command.value[0]} INTO {table} VALUES ();"
    elif command == sql.SELECT:
        return f"{command.value[0]} {operationsColumn} from {table}{selectStatement};"
    elif command == sql.UPDATE:
        return f"{command.value[0]} {table} SET {{ }};"



def updateTemplate():
    return abstractComand(sql.UPDATE)


def deleteTemplate():
    return abstractComand(sql.DELETE)


def insertTemplate():
    return abstractComand(sql.INSERT)


def selectTemplate():
    return abstractComand(sql.SELECT)


funarray = [updateTemplate(), selectTemplate(), deleteTemplate(), insertTemplate()]
print(random.choice(funarray))