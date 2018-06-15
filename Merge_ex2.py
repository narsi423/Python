'''
Script_Name:Merge_ex2.py
author: Narasimha
Date:06/13/2018
Description: Merging of two files which are having different formats
'''
with open('Info3.txt','r') as f3:
    f3_header = f3.readline()
    f3_data = f3.readlines()
    for i in f3_data:
        Id = i.split(',')[0]
        Name = i.split(',')[1]
        Sal = i.split(',')[2]
        Deptno = i.split(',')[3]
        Gen = i.split(',')[4].split('\n')[0]
        with open('Info1.txt', 'a') as f1:
            f1.write("\n"+Id+","+Name+","+Gen+","+Sal+","+Deptno)
            f1.close()
f3.close()