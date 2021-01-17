tables = {
    'city': 
    {
        'id': {
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        'name': {
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        'country': {
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
    },
    'train': 
    {
        'id':{
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        'number':{
            'type': 'INTEGER',
            'info': {'notNull'},
        },
        'model': {
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        'type': {
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        'capacity':{
            'type': 'INTEGER',
            'info': {'notNull'},
        },
        'companyId': {
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'},
            'ref': 'company'
        },
    },
    'company': 
    {
        'id':{
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        'number':{
            'type': 'INTEGER',
            'info': {'notNull'},
        },
    },
    'employee': 
    {
        'id':{
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        'firstName':{
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        'lastName':{
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        'position':{
            'type': 'INTEGER',
            'info': {'notNull'}
        },
        'workExperience':{
            'type': 'DOUBLE',
            'info': {'notNull'}
        },
        'companyId':{
            'type': 'INTEGER',
            'info': {'notNull'}
        },
        'crewId':{
            'type': 'INTEGER',
            'info': {'notNull'}
        },
    },
    'company': 
    {
        'id':{
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        'countOfEmployees':{
            'type': 'INTEGER',
            'info': {'notNull'},
        },
    },
    'cruise': 
    {
        'id':{
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        'number':{
            'type': 'INTEGER',
            'info': {'notNull'},
        },
        'departureTime':{
            'type': 'DATETIME',
            'info': {'notNull'}
        },
        'arrivingTime':{
            'type': 'DATETIME',
            'info': {'notNull'}
        },
        'distance':{
            'type': 'DOUBLE',
            'info': {'notNull'},
        },
        'trainId':{
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': ''
        },
        'crewId':{
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': ''
        },
        'trainstationSorceId':{
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': ''
        },
        'transtationDestinationId':{
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': ''
        },
    },
    'trainstationDestination': 
    {
        'id':{
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        'code':{
            'type': 'INTEGER',
            'info': {'notNull'},
        },
        'name':{
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        'cityId':{
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': ''
        },
    },
    'trainstationSource': 
    {
        'id':{
            'type': 'INTEGER',
            'info': {'key', 'autoInc', 'notNull'}
        },
        'code':{
            'type': 'INTEGER',
            'info': {'notNull'},
        },
        'name':{
            'type': 'VARCHAR',
            'len': '45',
            'info': {'notNull'}
        },
        'cityId':{
            'type': 'INTEGER',
            'info': {'notNull'},
            'ref': ''
        },
    },
}