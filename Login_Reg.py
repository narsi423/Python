'''
Script_Name:Log_Reg.py
author: Narasimha
Date:06/13/2018
Description: Login and Registration Example
'''


n = int(input("Choose your preference:\n 1. Login\n 2. Register\n 3. Change Password\n"))
def Register():
    pword = input("Create Password: ")
    rpword = input("Re-enter Password: ")
    if pword == rpword:
        with open('Validation.txt', 'a') as f:
            f.write(uname + "," + pword + "\n")
            f.close()
        print("User registered successfully")
    else:
        print("Please enter correct password")
details = {}
if n == 1:
    print("Login details")

    uname = input("Enter username: \n")
    if 'Validation.txt':
        with open('Validation.txt', 'r') as f:
            data = f.readlines()
            print(data)

            for i in data:
                unames = i.split(',')[0]
                pwords = i.split(',')[1].split('\n')[0]
                if details.get(unames) == None:
                    details[unames] = pwords

        print(details)
    else:
        print("Please register before login")
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
    if 'Validation.txt':
        if uname not in details.keys():
            Register()
        else:
            print("The user name is already used, please choose another one")
    else:
        Register()



elif n == 3:
    print("Change password")
    uname = input("Enter Username: ")
    with open('Validation.txt', 'r') as f:
        data = f.readlines()
        print(data)
        details = {}
        for i in data:
            unames = i.split(',')[0]
            pwords = i.split(',')[1].split('\n')[0]
            if details.get(unames) == None:
                details[unames] = pwords

        print(details)
    if uname in details.keys():
        pword = input("Enter Old password: ")
        if pword in details.values():
            pword1 = input("Enter New Password: ")
            pword2 = input("Re-enter New Password: ")
            if pword1 == pword2:

                details[uname] = pword1
                with open('Validation.txt','a') as f:
                    f.write(uname+","+pword1+"\n")
                print("Your Password changed successfully")
            else:
                print("re-entered password is incorrect")
        else:
            print("Your Old password is incorrect")
    else:
        print("Please register before changing the password!")
else:
    print("Please enter either 1 or 2")