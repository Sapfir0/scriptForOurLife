import random

from bunch import generateRandomBunch

from tables import tables

insertUpdateData = ["Александроус", "Андреев", "Леха", "Колян"]


def generateColumns(tableName: str) -> list:
    table_keys = list(tables[tableName].keys())
    bunch_of_keys: list = generateRandomBunch(table_keys)
    return bunch_of_keys


def singleQuote(word: str):
    return f"'{word}'"


def randomBoolean() -> bool:
    return bool(random.getrandbits(1))


def toStr(listok: list, table=None):
    columns_str = ""
    for field in listok:
        if table:
            columns_str += f"{table}."
        columns_str += field
        if field != listok[-1]:
            columns_str += ', '
    return columns_str


def generateWhereStatements(table, joinTableName=False):
    whereArrays = []
    columns = generateColumns(table)
    for column in columns:
        columnType = tables[table][column]['type']
        if columnType == "VARCHAR":
            whereElements = f"{random.choice(insertUpdateData)}"
            whereElements = singleQuote(whereElements)
        elif columnType == "INTEGER":
            whereElements = random.randint(0, 1000)
        elif columnType == "FLOAT":
            whereElements = random.random()
        else:
            whereElements = None

        if joinTableName:
            whereArrays.append(f"{table}.{column}={whereElements}")
        else:
            whereArrays.append(f"{column}={whereElements}")
    return toStr(whereArrays)


def generateCreatingTable(table_name):
    res = "CREATE TABLE "
    foo = []
    if randomBoolean():
        res += "IF NOT EXISTS "
    res += f"{table_name} ("
    table = tables[table_name]
    for column_name in table:
        column_type = table[column_name]["type"]
        if (table[column_name].get("len")!=None):
            column_type += "(" + table[column_name]["len"] + ")"
            
        name_and_type = f"{column_name} {column_type}"
        foo.append(name_and_type)
    res += toStr(foo) + ');'
    
    return res


def generateDropTable(table_name):
    res = "DROP TABLE "
    if randomBoolean():
        res += "IF EXISTS "
    res += f"{table_name};"
    return res


def generateDatabase(database_name):
    return f"CREATE DATABASE {database_name}"


def updateTemplate(table, where):
    return f"UPDATE {table} SET {{{where}}};"


def deleteTemplate(table, where):
    return f"DELETE FROM {table} WHERE {where};"


def insertTemplate(table, where):
    return f"INSERT INTO {table} VALUES ({where});"


def selectTemplate(table, where, join=False):
    columns = toStr(generateColumns(table))
    distinct = ""
    if not bool(random.randint(0, 5)):
        distinct = "DISTINCT "
    return f"SELECT {distinct}{columns} FROM {table} WHERE {where};"


def generateAlter():
    pass


def generateSelectWithJoin():
    if randomBoolean():
        typeOfJoin = 'INNER'
    else:
        typeOfJoin = "OUTTER"


    randomNum = random.randint(0, 2)
    if randomNum == 0:
        mod = "LEFT"
    elif randomNum == 1:
        mod = "RIGHT"
    elif randomNum == 2:
        mod = "FULL"

    table = random.choice(list(tables.keys()))
    columns = generateColumns(table)

    table2 = random.choice(list(tables.keys()))
    columns2 = generateColumns(table2)

    print(f"SELECT {toStr(columns, table=table)}, "
          f"{toStr(columns2, table=table2)} FROM {table} {typeOfJoin} {mod} {table2} "
          f"WHERE {generateWhereStatements(table, joinTableName=True)}, "
          f"{generateWhereStatements(table2, joinTableName=True)};")


def generate_sql_requests():
    for table_name in tables:
        yield generateCreatingTable(table_name)

    for table_name in tables:
        yield generateDropTable(table_name)

    for i in range(10):
        table = random.choice(list(tables.keys()))
        where = generateWhereStatements(table)
        yield selectTemplate(table, where)

    generateSelectWithJoin()