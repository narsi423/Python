import sys
n = int(input("Enter the numbers of students you want to register here:\n".title()))
ID = []
NAME = []
MOBILE_NUMBER = []
for i in range(n):
    ID_LIST = input("Enter your id{}:\n".format(i).title())
    if(ID_LIST.isdigit()):
        ID.append(ID_LIST)
    else:
        print("Please Enter only digits".title())
        sys.exit(1)
    NAME_LIST = input("Enter your name:\n".title())
    if(NAME_LIST.isalpha()):
        NAME.append(NAME_LIST)
    else:
        print("Please Enter only alphabets from [A-Z] or [a-z]")
        sys.exit(1)
    MOBILE_NUMBER_LIST = input("Enter mobile number:\n".title())
    if(MOBILE_NUMBER_LIST.isdigit()):
        if(len(MOBILE_NUMBER_LIST) == 10):
            MOBILE_NUMBER.append(MOBILE_NUMBER_LIST)
        else:
            print("Please Enter a valid mobile number with only 10 digits".title())
            sys.exit(1)
    else:
        print("Please Enter only digits".capitalize())
        sys.exit(1)

print("Entered Details:\n".title())
for ids,names,mobile_numbers in zip(ID,NAME,MOBILE_NUMBER):
    print("%s %-6s %-6s" %(ids,names,mobile_numbers))

m = input("Please enter id/name/mobile_number to search:\n".title())
if(m.isdigit()):
    if m in ID:
        print("Entered ID is found".capitalize())
    elif m in MOBILE_NUMBER:
        print("Entered MOBILE_NUMBER is found".capitalize())
    else:
        print("Entered ID/MOBILE_NUMBER is not found".capitalize())

elif m in NAME:
    print("Entered Name is found".capitalize())
else:
    print("Entered Name is Not found".capitalize())
