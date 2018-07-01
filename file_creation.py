'''
Script Name: file_creation.py
Author: Narasimha
date: 30/06/2017
description: This created a file with a required format and then check for it's availability and then read and print the data in the file.
'''

import os
import datetime
import glob


pattern = 'Info-'
ext = '.txt'
path = "F:/Projects/Python/src/"


date = str(datetime.date.today())
file_name = pattern+date+ext
location = path+file_name
#print(file_name,location)

with open(file_name,'w+') as f:
    f.write(date)
f.close()

os.chdir(path)
files = glob.glob('Info*'+ext)
print(files)

if file_name in files:
    with open(file_name,'r') as f:
        print(f.readlines())
    print('avaialble')
else:
    print("No file")