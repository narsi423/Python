'''
Script Name: Create_File_daily.py
Author: Narasimha
date: 30/06/2017
description: This created a file with a required format write the today's date in the file.
Additional comments: Don't change the directory/path or never modify this file this is a schedule task to create a file daily at 00:00:05AM
'''

import os
import datetime

pattern = 'Info-'
ext = '.txt'
path = "F:/Projects/Python/src/"

date = str(datetime.date.today())
file_name = pattern+date+ext
os.chdir(path)
with open(file_name,'w+') as f:
    f.write(date)
f.close()
