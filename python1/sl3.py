import fileinput
import sys

list = []

for line in sys.stdin:
    list.append(line)
 
for i in range (0, len(list)):   
    print list[i]