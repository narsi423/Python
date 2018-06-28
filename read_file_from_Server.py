import paramiko as p


ssh = p.SSHClient()
ssh.set_missing_host_key_policy(p.AutoAddPolicy())
ssh.connect(hostname='192.168.209.128',username='narsi',password='Narasimha143@',port=22)
stdin, stdout, stderr = ssh.exec_command('cat Info.txt')
header = stdout.readline()
data = stdout.readlines()
for i in data:
    names = i.split(',')[1]
    sals = i.split(',')[3]
    print(names,sals)




