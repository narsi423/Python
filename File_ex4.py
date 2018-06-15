with open('Info.txt','r') as f:
    header = f.readline()
    data = f.readlines()
    aggr = {}
    '''for i in data:
        deptno = i.split(',')[4].split('\n')[0]
        gen = i.split(',')[2]
        sal = int(i.split(',')[3])
    '''


for i in data:
    deptno = i.split(',')[4].split('\n')[0]
    gen = i.split(',')[2]
    sal = int(i.split(',')[3])
