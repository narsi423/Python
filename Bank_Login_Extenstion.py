class User:

    num_bal = {123456:10000,789012:20000}
    def __init__(self):
        print("Welcome to Internet Banking:\n")

    def bal_enq(self,ac,uname):
        self.ac = ac
        self.uname = uname
        print("Available Balance of",uname," is",self.num_bal[ac])

    def deposit(self,ac,uname):
        self.ac = ac
        self.uname =uname
        amt = int(input("Enter amount you want to deposit:\n"))
        print("Balance of",uname," after deposit of",amt,"is:",self.num_bal[ac]+amt)

    def withdraw(self,ac,uname):
        self.ac = ac
        self.uname = uname
        amt = int(input("Enter amount you want to withdraw:\n"))
        if amt <= self.num_bal[ac]:
            print("Balance of",uname,"after withdrwal of",amt,"is",self.num_bal[ac] - amt)
        else:
            print("your account",uname," has only",self.num_bal[ac])

    def online_transfer(self,ac1,ac2,uname,uname2):
        self.ac1 = ac1
        self.ac2 = ac2
        self.uname2 = uname2

        amt = int(input("Enter the amount you want to transfer:\n"))
        if amt <= self.num_bal[ac1]:
            t1 = self.num_bal[ac1] - amt
            t2 = self.num_bal[ac2] + amt
            print("The balance of",uname," after transfer of",amt," is",t1,"and the balance of user:",uname2," after the credit of",amt,"is",t2)

details = {'aaa':'aaa', 'bbb':'bbb'}
uname_num = {'aaa':123456,'bbb':789012}


u1 = User()
uname = input("Enter Username:\n")
if uname in details.keys():
    pword = input("Enter passcode:\n")
    if details[uname] == pword:
        n = int(input(
            "Choose your preference:\n 1. Balance Enquiry\n 2. Deposit\n 3. Withdraw\n 4. Online Transfer\n"))
    else:
        print("Incorrect Passcode")
else:
    print("The username",uname,"is not registered with us as per our records")

if n == 1:
    #print("Balance enqiury Page under construction")
    ac = uname_num[uname]
    u1.bal_enq(ac,uname)

elif n == 2:
    #print("Deposite Page under construction")
    ac = uname_num[uname]
    u1.deposit(ac,uname)

elif n == 3:
    #print("Withdraw Page under construction")
    ac = uname_num[uname]
    u1.withdraw(ac,uname)

elif n == 4:
    #print("Online Transfer Page under construction")
    uname2 = input("Enter the user name you want to transfer:\n")
    if uname2 in details.keys():
        ac1 = uname_num[uname]
        ac2 = uname_num[uname2]
        u1.online_transfer(ac1,ac2,uname,uname2)
    else:
        print("Username",uname2,"is not a registered member")
else:
    print('Please choose any number between 1 to 4')