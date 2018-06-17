'''
Script_Name:Log_Reg.py
author: Narasimha
Date:06/14/2018
Description: Login and Registration Example
'''

import os.path
import parameter as p

n = int(input("Choose your preference:\n 1.Login\n 2.Register\n 3.Change Password\n"))

def Read_Data():
    details = {}
    with open('Validation.txt', 'r') as f:
        f_data = f.readlines()
        # print(f_data)
        for i in f_data:
            unames = i.split(',')[0]
            pwords = i.split(',')[1].split('\n')[0]
            # print(i)
            if details.get(unames) == None:
                details[unames] = pwords
            else:
                details[unames] = pwords
        # print(details)
        # print((details[uname]))

def Login():
    print("Login Screen".title())
    uname = input("Enter Username: \n")
    if os.path.isfile(p.file_loc):

        if uname in Read_Data().details.keys():
            pword = input("Enter Password: \n")
            if Read_Data().details[uname] == pword:
                print("Login successful")
            else:
                print("You entered Incorrect Password, please check once.")
    else:
        print("Please register before login.")

def Register():
    print("Registration Details:\n".title())
    uname = input("Create Username: \n")
    pword = input("Create Password: \n")
    rpword = input("Re-Enter Password: \n")
    if(pword == rpword):
        #print("User Registered successfully")
        with open('Validation.txt','a') as f:
            f.write(uname+','+pword+'\n')
            print("User Registered successfully")
    else:
        print("Please check password and re-entered password, both should be same")

def Change_Password():
    print("Change Password screen:".title())
    uname = input("Enter Username: ")
    if os.path.isfile(p.file_loc):

        if uname in Read_Data().details.keys():
            pword = input("Enter Old Password")
            if Read_Data().details[uname] == pword:
                npword = input("Enter New Password")
                rnpword = input("Re Enter New Password")
                if npword == rnpword:
                    with open('Validation.txt','a') as f:
                        f.write(uname+','+npword+'\n')
                        print("Your password has been changed successfully")
                else:
                    print("New password and reentered new password should be same")
            else:
                print("Old password is incorrect")
        else:
            print(uname+" is not registered with us, please go ahead and press 2")
    else:
        print(uname+" is not registered. Please go ahead and register before changing the password")


if n == 1:
    Login()
elif n == 2:
    Register()
elif n == 3:
    Change_Password()
else:
    print("Please select any of the above 3 options as 1/2/3.")