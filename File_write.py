#To Write into a File
f = open('testfile.txt','w')
text = input("Enter a text to write:")
f.write(text)
f.close()

#To read a file
f = open('testfile.txt','r')
print(f.read())
f.close()

#To appened a text toa file
f = open('testfile.txt','a')
text1 = input("Enter a text to appened:")
f.write(text1)
f.close()