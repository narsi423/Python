'''
Script_name = Logon_Extentions.py
Author = Narasimha
Date = 5/29/2018
Description = Etenstion of login script
Version = 0.1

'''
import sys
print("Welcome to somewebsite.com")
user_name = input("Enter User name : \n")
dict = {'abcd':'abcd','abc':'abc',1234:1234}
user_list = dict.keys()
if user_name in user_list:
    #print("Valid user")
    password = input("Enter Password: \n")
    if dict[user_name] == password:
        #print("valid password")
        print("login successfully")
    else:
        print("Invalid password, please check for CAPS lock and NUM lock for case sensitivity")
        sys.exit(1)
else:
    print("Inavlid User, please enter correct user name")
    sys.exit(1)
print("Thanks for visting somewebsite.com, have a good day!")