import fileinput
import sys

file = fileinput.input()

for line in file:
    print line
