'''
Script Name: Copy_File.py
Author: Narasimha
date: 30/06/2017
description: This created a file with a required format and then check for it's availability and then read and print the data in the file.
'''

import os
import pysftp as sftp
import glob
import datetime
import paramiko as p

hostname='192.168.209.128'
username='narsi'
password='Narasimha143@'
port=22


transport = p.Transport((hostname,port))
transport.connect(username = username, password = password)
sftp = p.SFTPClient.from_transport(transport)
pattern = 'Info-'
ext = '.txt'
localpath = "F:/Projects/Python/src/"
remotepath = "/home/narsi/"

date = str(datetime.date.today())
file_name = pattern+date+ext
location = localpath+file_name

os.chdir(localpath)
files = glob.glob('Info*'+ext)
if file_name in files:
    sftp.put(localpath+file_name,remotepath+file_name)
    sftp.close()
    #ssh.close()

else:
    print("file",file_name," is not available in localpath",localpath)

