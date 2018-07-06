import json

with open("ex_file.json") as f:
    data = json.load(f)

for value in data:
    #print(value)
    #print(type(value['physicalTableName']))
    #print(value['logicalColumns'][0])
    #logicalColumns = value['logicalColumns'][0]
    physicalTableName = value['physicalTableName']
    length = len(value['logicalColumns'])
    for i in range(length):
        logicalColumnName = value['logicalColumns'][i]['logicalColumnName']
        physicalColumnName = value['logicalColumns'][i]['physicalColumnName']
        isProfilable = value['logicalColumns'][i]['isProfilable']
        columnDataType = value['logicalColumns'][i]['columnDataType']
        isKeyColumn = value['logicalColumns'][i]['isKeyColumn']
        #print(physicalTableName)
        print("logicalColumnName : ",logicalColumnName,"--","physicalColumnName : ",physicalColumnName,"--","isProfilable : ",isProfilable,"--","columnDataType : ",columnDataType,"--","isKeyColumn : ",isKeyColumn)

with open("ex_file.json") as f:
    data1 = json.load(f)

for value in data1:
    #print(value)
    #print(type(value['physicalTableName']))
    #print(type((value['logicalColumns'])))
    length = len(value['logicalColumns'])
    #logicalColumns = value['logicalColumns'][0]
    physicalTableName1 = value['physicalTableName']
    for i in range(length):
        logicalColumnName1 = value['logicalColumns'][i]['logicalColumnName']
        physicalColumnName1 = value['logicalColumns'][i]['physicalColumnName']
        isProfilable1 = value['logicalColumns'][i]['isProfilable']
        columnDataType1 = value['logicalColumns'][i]['columnDataType']
        isKeyColumn1 = value['logicalColumns'][i]['isKeyColumn']
        #print(physicalTableName1)
        #print("logicalColumnName : ",logicalColumnName1,"--","physicalColumnName : ",physicalColumnName1,"--","isProfilable : ",isProfilable1,"--","columnDataType : ",columnDataType1,"--","isKeyColumn : ",isKeyColumn1)

