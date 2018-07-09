import json
import sys

with open(sys.argv[1]) as f1:
    data1 = json.load(f1)

with open(sys.argv[2]) as f2:
    data2 = json.load(f2)

length1 = len(data1)
length2 = len(data2)
#print((data1[0]['logicalColumns']))
if length1 == length2:
    for i in range(length1):
        if data1[i]['physicalTableName'] == data2[i]['physicalTableName']:
            if data1[i]['logicalColumns'] != data2[i]['logicalColumns']:
                length3 = len(data1[i]['logicalColumns'])
                for j in range(length3):
                    if data1[i]['logicalColumns'][j] == data2[i]['logicalColumns'][j]:
                        pass
                    else:
                        #print(data1[i]['logicalColumns'][j],data2[i]['logicalColumns'][j],"are not same")
                        if data1[i]['logicalColumns'][j]['logicalColumnName'] == data2[i]['logicalColumns'][j]['logicalColumnName']:
                            if data1[i]['logicalColumns'][j]['physicalColumnName'] == data2[i]['logicalColumns'][j]['physicalColumnName']:
                                if data1[i]['logicalColumns'][j]['isProfilable'] == data2[i]['logicalColumns'][j]['isProfilable']:
                                    if data1[i]['logicalColumns'][j]['columnDataType'] == data2[i]['logicalColumns'][j]['columnDataType']:
                                        if data1[i]['logicalColumns'][j]['isKeyColumn'] == data2[i]['logicalColumns'][j]['isKeyColumn']:
                                            pass
                                        else:
                                            print("***************Difference************")
                                            print("physicalTableName: File1:", data1[i]['physicalTableName'], "FIle2:",data2[i]['physicalTableName'])
                                            print("logicalColumnName: File1:", data1[i]['logicalColumns'][j]['logicalColumnName'], "FIle2:",data2[i]['logicalColumns'][j]['logicalColumnName'])
                                            print("isKeyColumn: File1:",data1[i]['logicalColumns'][j]['isKeyColumn'],"File2:",data2[i]['logicalColumns'][j]['isKeyColumn'])
                                            #print(data1[i]['logicalColumns'][j]['isKeyColumn'],data2[i]['logicalColumns'][j]['isKeyColumn'],"are not same in",data1[i]['logicalColumns'][j])
                                    else:
                                        print("***************Difference************")
                                        print("physicalTableName: File1:", data1[i]['physicalTableName'],"FIle2:",data2[i]['physicalTableName'])
                                        print("logicalColumnName: File1:",data1[i]['logicalColumns'][j]['logicalColumnName'],"FIle2:",data2[i]['logicalColumns'][j]['logicalColumnName'])
                                        print("columnDataType: File1:",data1[i]['logicalColumns'][j]['columnDataType'],"FIle2:",data2[i]['logicalColumns'][j]['columnDataType'])
                                        #print(data1[i]['logicalColumns'][j]['columnDataType'],data2[i]['logicalColumns'][j]['columnDataType'],"are not same in",data1[i]['logicalColumns'][j])
                                else:
                                    print("***************Difference************")
                                    print("physicalTableName: File1:", data1[i]['physicalTableName'], "FIle2:",data2[i]['physicalTableName'])
                                    print("logicalColumnName: File1:",data1[i]['logicalColumns'][j]['logicalColumnName'], "FIle2:",data2[i]['logicalColumns'][j]['logicalColumnName'])
                                    print("isProfilable: File1:",data1[i]['logicalColumns'][j]['isProfilable'],"File2:",data2[i]['logicalColumns'][j]['isProfilable'])
                                    #print(data1[i]['logicalColumns'][j]['isProfilable'],data2[i]['logicalColumns'][j]['isProfilable'],"are not same")
                            else:
                                print("***************Difference************")
                                print("physicalTableName: File1:", data1[i]['physicalTableName'], "FIle2:",data2[i]['physicalTableName'])
                                print("logicalColumnName: File1:", data1[i]['logicalColumns'][j]['logicalColumnName'],"FIle2:", data2[i]['logicalColumns'][j]['logicalColumnName'])
                                print("physicalColumnName: File1:",data1[i]['logicalColumns'][j]['physicalColumnName'],"File2:",data2[i]['logicalColumns'][j]['physicalColumnName'])
                                #print(data1[i]['logicalColumns'][j]['physicalColumnName'],data2[i]['logicalColumns'][j]['physicalColumnName'],"are not same")
                        else:
                            print("***************Difference************")
                            print("physicalTableName: File1:", data1[i]['physicalTableName'], "FIle2:",data2[i]['physicalTableName'])
                            print("logicalColumnName: File1:", data1[i]['logicalColumns'][j]['logicalColumnName'],"FIle2:", data2[i]['logicalColumns'][j]['logicalColumnName'])
                            #print(data1[i]['logicalColumns'][j]['logicalColumnName'],data2[i]['logicalColumns'][j]['logicalColumnName'],"are not same")


            else:
                pass
                #print(data1[i]['logicalColumns'],data2[i]['logicalColumns'],"are not same")
        else:
            print("***************Difference************")
            print("physicalTableName: File1:", data1[i]['physicalTableName'], "FIle2:", data2[i]['physicalTableName'])
            #print(data1[i]['physicalTableName'],data2[i]['physicalTableName'],"are not same")
else:
    print("Length is not same")