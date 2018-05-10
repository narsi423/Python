n = int(input('Enter Number to check for palindrome : '))
m = n
c = 0
while (m > 0):
   b = m % 10
   c = m % 10 + c*10
   m = m//10
if (n == c):
    print(n, 'is a palindrome number')
else:
    print(n,'is not a palindrome number')