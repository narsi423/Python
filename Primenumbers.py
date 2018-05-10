x =  int(input("Enter a number : "))
c = 0
for i in range(1,x):
    if(x%i == 0):
        c+=1

if(c <= 2):
    print( x ,"is a prime number")

else:
    print(x,"is not a prime number")





