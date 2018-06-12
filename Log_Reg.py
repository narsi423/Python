'''
Script_Name:Log_Reg.py
author: Narasimha
Date:06/12/2018
Description: Login and Registration Example

'''

n = int(input("Choose your preference:\n 1. Login\n 2.Register\n"))
if n == 1:
    print("Login details")
    with open('Validation.txt','r') as f:
        data = f.readlines()
        #print(data)
        details = {}
        for i in data:
            unames = i.split(',')[0]
            pwords = i.split(',')[1].split('\n')[0]
            if details.get(unames)== None:
                details[unames] = pwords
            else:
                print("Please Enter Correct User name")
        #print(details)
        uname = input("Enter username: \n")
        if uname in details.keys():
            pword = input("Enter password: \n")
            #value =details[uname]
            #print(value)
            if pword == details[uname]:
                print("Login successfully")
            else:
                print("Incorrect password for ",uname,"Please Enter a correct passowrd")
        else:
            print("You are not a registered number, please go ahead and press 2")
        f.close()
elif n == 2:
    print("Registartion details")
    uname = input("Create Username: ")
    pword = input("Create Password: ")
    rpword = input("Re-enter Password: ")
    if pword == rpword:

        with open('Validation.txt','a') as f:
            f.write(uname+","+pword+"\n")
            print("User registered successfully")
    else:
        print("Please enter correct password")

else:
    print("Please enter either 1 or 2")