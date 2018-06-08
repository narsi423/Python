str1 = "Hello World!, Welcome to Python"
sub = "o"

i = 0
flag = False

n = len(str1)

while i < n:
 pos = str1.find(sub,i,n)
 if pos != -1:
  print("found at position:", pos + 1)
  i = pos + 1
  flag = True
 else:
  i = i + 1

if flag == False:
 print("sub string not found")