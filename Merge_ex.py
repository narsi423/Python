'''
Script_Name:Merge.py
author: Narasimha
Date:06/13/2018
Description: Merge two files which are having same format
'''

with open('Info2.txt','r') as f2:
    f2_header = f2.readline()
    f2_data = f2.readlines()
with open('Info1.txt','a') as f1:
    f1.write('\n')
    for i in f2_data:
        f1.write(i)