import MySQLdb as m
import re

conn = m.connect(host ='*******',database = '******',user = '******',password = '*****',port =3306)
cursor = conn.cursor()

cursor.execute("SELECT * FROM CNV_CONVERSATION where conversationid in (3156,4555,5008,4809,3579,5103,5018,5176,6421,6427 ,5233,5219,4445,5258,4294,3693,5000,5380,3899,3964,3414,5426,5440,6124,5457,5886,6139,6794,6945,6993,6946,7089,7108,7098,7249,7582,7202,8126,8224,8328,7198,8687)")
#cursor.execute("SELECT * FROM CNV_CONVERSATION where conversationid in (3156)")
rows = cursor.fetchall()
for row in rows:
    with open("ZH_Data.txt", 'a') as f:
        f.write("Campaign_id :"+str(row[0])+"\n")
    #print("Campaign_id :",row[0])
    #print(type(row[9]))
    #print(row[9].partition('physicalTableName'))
    p = re.compile('SAVE_SEGMENT_CHANNELED_\d[0-9]*_\d[0-9]*')
    m = p.findall(row[9])
    if m:
        for i in m:
            with open("ZH_Data.txt",'a') as f:
                f.write(i+"\n")
    else:
        with open("ZH_Data.txt", 'a') as f:
            f.write("No Segemnts \n")

print("Data has written into ZH_Data file successfully.")

'''
    data = row[9]
    #seg = data['nodes']
    print(data)
    '''