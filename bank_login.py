'''
script name : bank_login.py
author : Narasimha
Date : 23/05/2018
Description : This script is about netbanking login
 
'''

#python bank_login.py HDFC

import sys

bank_name = sys.argv[1]

print("welcome to ",bank_name)

user_name = input("Enter username\n")

#print("the user name is ",user_name)

pwd = input("Enter password\n")

#print("the pwd is \n",pwd)

print("Hello Mr.",user_name)
print("Thanks for visiting",bank_name)