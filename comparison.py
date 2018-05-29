import re

shakes = open("baseline.dat", "r")
string1 = """ [
                {"""
for line in shakes:
    if re.match(".*" + string1 + "*.", line):
        print(line)

