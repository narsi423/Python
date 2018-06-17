import os
import sys

def file_availability(file_name,mode):
    try:
        f = open(file_name,mode)
    except IOError as e:
        print("Unable to open file: ",file_name,e)
        input("Please press enter to exit")
        sys.exit(1)
    except FileNotFoundError as e1:
        print("There is no file with the ",file_name,e1)
    else:
        return file_name

def Read_Data(file_name):
    data = file_name.readlines()
    details = {}
    for i in data:
        uname = i.split(',')[0]
        pword = i.split(',')[1].split('\n')[0]
        if details.get(uname) == None:
            details[uname] = pword
        else:
            details[uname] = pword

    return details


file_name = 'Validation.txt'
mode = 'r'
username = input("Please Enter your user name:\n")
file_availability(file_name,mode)
print(Read_Data(file_name))





