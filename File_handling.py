with open('Info.txt','r') as f:
    f_header = f.readline()
    f_data = f.readlines()
    aggr = {}
    for i in f_data:
        dno = i.split(',')[4].split('\n')[0]  #20
        sal = int(i.split(',')[3]) #4000
        gen = i.split(',')[2] #M
        key = (dno,gen)
        if aggr.get(key) == None:
            aggr[(dno,gen)] = sal

        else:
            aggr[(dno,gen)] += sal
print(aggr)

#104,ddd,M,4000,20
#105,eee,M,5000,20