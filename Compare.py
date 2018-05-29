f1 = open('baseline.dat', 'r')
f2 = open('file.txt', 'r')
FO = open('output.txt', 'w')

for line1 in f1:
    for line2 in f2:
        if line1 == line2:
            FO.write(line2)