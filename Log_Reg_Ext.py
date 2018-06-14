import os.path
import parameter as p

n = int(input("Choose your preference:\n 1.Login\n 2.Register\n 3.Change Password\n"))
details = {}
def Login():
    print("Login Screen: \n")
    uname = input("Enter Username: \n")
    if os.path.isfile(p.file_loc):
        with open('Validation.txt','r') as f:
            f_data = f.readlines()
            #print(f_data)
            for i in f_data:

                unames = i.split(',')[0]
                pwords = i.split(',')[1].split('\n')[0]
                print(i)
                if details.get(unames) == None:
                    details[unames] = pwords
            #print(details)
            #print((details[uname]))
        if uname in details.keys():
            pword = input("Enter Passord: \n")
            if details[uname] == pword:
                print("Login successful")
            else:
                print("You entered Incorrect Password, please check once.")
    else:
        print("Please register before login.")

def Register():
    print("Registration Details:\n")
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
    print("Change Password screen:")

if n == 1:
    Login()
elif n == 2:
    Register()
elif n == 3:
    Change_Password()
else:
    print("Please select any of the above 3 options as 1/2/3.")