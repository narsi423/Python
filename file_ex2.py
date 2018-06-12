f = open('Info.txt','r')
header = f.readline()
data = f.readlines()
aggr = {}
for i in data:
    gen = i.split(',')[2]
    sal = int(i.split(',')[3])
    if aggr.get(gen) == None:
        aggr[gen]= sal
    else:
        aggr[gen]+=sal
print(aggr)
