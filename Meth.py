import os.path
import sys
import random
class Online_Banking:
    def file_availability(self):
        file_name = 'Validation.txt'
        if os.path.isfile(file_name):
            return file_name
        else:
            return None

    def user_pass(self):
        details = {}
        with open(Online_Banking.file_availability(self),'r') as f:
            f_data = f.readlines()
            for i in f_data:
                uname = i.split(',')[0]
                pword = i.split(',')[1]
                if details.get(uname) == None:
                    details[uname] = pword
                else:
                    details[uname] = pword
        return details

    def user_acc_num(self):
        details = {}
        with open(Online_Banking.file_availability(self),'r') as f:
            f_data = f.readlines()
            for i in f_data:
                uname = i.split(',')[0]
                acc_num = i.split(',')[2]
                if details.get(uname) == None:
                    details[uname] = acc_num
        return details

    def acc_num_bal(self):
        details = {}
        with open(Online_Banking.file_availability(self), 'r') as f:
            f_data = f.readlines()
            for i in f_data:
                acc_num = i.split(',')[2]
                bal = i.split(',')[3].split('\n')[0]
                if details.get(acc_num) == None:
                    details[acc_num] = bal
                else:
                    details[acc_num] = bal
        return details


    def login(self):
        uname = input("Enter username:\n")
        #print("Login")
        if uname in Online_Banking.user_pass(self).keys():
            pword = input("Please enter pword:\n")
            if pword == Online_Banking.user_pass(self)[uname]:
                print("Login successful")
                n = int(input("Choose your preference:\n 1. Deposit\n 2. Withdraw\n 3. Online Transfer\n"))
                if n == 1:
                    Online_Banking.deposit(self,uname)

                elif n == 2:
                    Online_Banking.withdraw(self,uname)

                elif n == 3:
                    Online_Banking.online_transfer(self,uname)

                else:
                    print("Choose a number that you want between the above options")
            else:
                print("Incorrect password")
        else:
            print("Not registered")

    def deposit(self,uname):
        self.uname = uname
        print("Deposit")
        m = int(input("Choose your preference:\n 1. Current Account 2. Other account"))
        if m == 1:
            acct_num = Online_Banking.user_acc_num(self)[uname]
            bal = int(Online_Banking.acc_num_bal(self)[acct_num])
            amt = int(input("Please enter the amount you want to deposit:\n"))

            if Online_Banking.acc_num_bal(self)[acct_num] != None:
                #print(int(Online_Banking.acc_num_bal(self)[acct_num]) + amt)
                ob.write_data(uname,Online_Banking.user_pass(self)[uname],acct_num,bal+amt)
            print("Money",amt,"deposited successfully, available balance is :",Online_Banking.acc_num_bal(self)[acct_num])



    def withdraw(self,uname):
        print("Withdraw")
        self.uname = uname

    def online_transfer(self,uname):
        print("Online Transfer")
        self.uname = uname

    def register(self):
        uname = input("Create username:\n")
        if uname not in Online_Banking.user_pass(self).keys():
            pword = input("Create password:\n")
            rpword = input("Re-enter password:\n")
            if pword == rpword:
                ac_num = random.randint(999999, 99999999)
                bal = 10000
                while ac_num not in Online_Banking.acc_num_bal(self):
                    ob.write_data(uname,pword,ac_num,bal)
                    print("user registered successfully")
                    break
                    #return uname+','+pword+'\n'


            else:
                print("Incorrect passcode")
        else:
            print("Username is already registered with us, please select another.")

    def write_data(self,uname,pword,acc_num,bal):
        self.uname = uname
        self.pword = pword
        self.acc_num = acc_num
        self.bal = bal
        with open('Validation.txt','a') as f:
            f.write(self.uname+','+self.pword+','+str(self.acc_num)+','+str(bal)+'\n')



ob = Online_Banking()
n = int(input("Choose ur pref:\n 1. Login\n 2.Register\n"))
if n == 1:
    if ob.file_availability() != None:
        ob.login()
    else:
        print("No file")
if n == 2:
    ob.register()




