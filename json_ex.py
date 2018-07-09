import json

with open('student.json') as f:
    data = json.load(f)

length1 = len(data['student'])

for i in range(length1):
    name = data['student'][i]['name']
    phone = data['student'][i]['phone']
    length2 = len(data['student'][i]['address'])
    for j in range(length2):
        dno = data['student'][i]['address'][j]['dno']
        street = data['student'][i]['address'][j]['street']
        city = data['student'][i]['address'][j]['city']
        state = data['student'][i]['address'][j]['state']
    print("*********** student",str(i+1),"***************")
    print(" Name :",name,"\n","Phone No: ",phone,"\n","Address :-  dno :",dno,"\n\t\t\t","Street :",street,"\n\t\t\t","City :",city,"\n\t\t\t","State: ",state)

