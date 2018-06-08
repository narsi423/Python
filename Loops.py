# While Loop
count = 0
while(count < 9):
    print("count is :", count)
    count +=1

print("End of the code")

#Indefinite while loop

var = 1
while(var == 1):
    num = input("Enter a number:")
    print("you entered ", num)

#Else with loops

count = 0
while(count < 5):
    print(count,"is less than 5")
    count+=1
else:
    print(count, "is not less than 5")

#Single statements suite

flag = 1
while(flag): print("Given flag is really true")
print("Good bye")