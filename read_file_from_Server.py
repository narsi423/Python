import paramiko as p
import MySQLdb as m
conn = m.connect(host ='localhost',database = 'mysql',user = 'Narsi',password = 'Narasimha143@',port =3000)
cursor = conn.cursor()

ssh = p.SSHClient()
ssh.set_missing_host_key_policy(p.AutoAddPolicy())
ssh.connect(hostname='192.168.209.128',username='narsi',password='Narasimha143@',port=22)
stdin, stdout, stderr = ssh.exec_command('cat Info.txt')
header = stdout.readline()
data = stdout.readlines()

c = 0
for i in data:

    names = i.split(',')[1]
    sals = float(i.split(',')[3])
    Query = "insert into Info(name,sal) values('%s',%f)"%(names,sals)
    cursor.execute(Query)
    conn.commit()
    c += 1
    if c == 1:
        print(str(c)+'st Record inserted successfully')
    elif c == 2:
        print(str(c)+'nd Record inserted successfully')
    elif c == 3:
        print(str(c)+'rd Record inserted successfully')
    else:
        print(str(c)+'th Record inserted successfully')

conn.close()
ssh.close()






