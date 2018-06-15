import fileinput
text = 'aaa'
new_text = 'aaa'+','+'ccC'
x = fileinput.input(files='Validation.txt',inplace=1)
for line in x:
    if text in line:
        line = new_text
    print(line)
x.close()