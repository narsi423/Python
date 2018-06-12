f = open('Info.txt','r')
header = f.readline()
data = f.readlines()
aggr = {}
for i in data:
    deptno = int(i.split(',')[4].split('\n')[0])
    sal = int(i.split(',')[3])
    if aggr.get(deptno) == None:
        aggr[deptno]= sal
    else:
        aggr[deptno]+=sal
print(aggr)
