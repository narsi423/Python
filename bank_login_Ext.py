class User:

    num_bal = {123456:10000,789012:20000}
    def __init__(self):
        print("Welcome to Internet Banking:\n")

    def bal_enq(self,ac):
        self.ac = ac
        print("Available Balance is",self.num_bal[ac])

    def deposit(self,ac):
        self.ac = ac
        amt = int(input("Enter amount you want to deposit:\n"))
        print("Balance after deposit of",amt,"is:",self.num_bal[ac]+amt)

    def withdraw(self,ac):
        self.ac = ac
        amt = int(input("Enter amount you want to withdraw:\n"))
        if amt <= self.num_bal[ac]:
            print("Balance after withdrwal of",amt,"is",self.num_bal[ac] - amt)
        else:
            print("your account has only",self.num_bal[ac])

    def online_transfer(self,ac1,ac2,uname2):
        self.ac1 = ac1
        self.ac2 = ac2
        self.uname2 = uname2

        amt = int(input("Enter the amount you want to transfer:\n"))
        if amt <= self.num_bal[ac1]:
            t1 = self.num_bal[ac1] - amt
            t2 = self.num_bal[ac2] + amt
            print("The balance after transfer of",amt," in your accunt is",t1,"and the balance of user:",uname2," after the credit of",amt,"is",t2)

details = {'aaa':'aaa', 'bbb':'bbb'}
uname_num = {'aaa':123456,'bbb':789012}

n = int(input("Choose your preference:\n 1. Login\n 2. Register\n 3. Balance Enquiry\n 4. Deposit\n 5. Withdraw\n 6. Online Transfer\n"))
u1 = User()
if n == 1:
    print("Login Page under construction")
    #Login()
elif n == 2:
    print("Regstartion Page under construction")
elif n == 3:
    #print("Balance enqiury Page under construction")
    uname = input('Enter username:\n')
    if uname in details.keys():
        pword = input("Enter passcode:\n")
        if details[uname] == pword:
            ac = uname_num[uname]
            u1.bal_enq(ac)
        else:
            print("Incorrect passcode")
    else:
        print("Username",uname,"is not registered with us as per records")

elif n == 4:
    #print("Deposite Page under construction")
    uname = input("Enter username:\n")
    if uname in details.keys():
        pword = input("Enter passcode:\n")
        if details[uname] == pword:
            ac = uname_num[uname]
            u1.deposit(ac)
        else:
            print("Incorrect passcode")
    else:
        print("Username",uname,"is not registered with us as per records")
elif n == 5:
    #print("Withdraw Page under construction")
    uname = input("Enter username:\n")
    if uname in details.keys():
        pword = input("Enter passcode:\n")
        if details[uname] == pword:
            ac = uname_num[uname]
            u1.withdraw(ac)
        else:
            print("Incorrect passcode")
    else:
        print("Username",uname,"is not registered with us as per records")

elif n == 6:
    #print("Online Transfer Page under construction")
    uname = input("Enter username:\n")
    if uname in details.keys():
        pword = input("Enter passcode:\n")
        if details[uname] == pword:
            uname2 = input("Enter the user name you wnat to transfer")
            if uname2 in details.keys():
                ac1 = uname_num[uname]
                ac2 = uname_num[uname2]
                u1.online_transfer(ac1,ac2,uname2)
            else:
                print("Username",uname2,"is not registered ")
        else:
            print("Incorrect passcode")
    else:
        print("Username", uname, "is not registered with us as per records")
else:
    print('Please choose any number between 1 to 6')