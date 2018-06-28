import MySQLdb as m
conn = m.connect(host ='localhost',user = 'Narsi',password = 'Narasimha143@',port =3000)
cursor = conn.cursor()
cursor.execute('use mysql')
