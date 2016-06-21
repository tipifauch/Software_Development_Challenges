import fileinput

file = fileinput.input()

myList = []

for line in file:
    myList.append(line)


for line in file:
	var1,var2 = line.split(' <-- ')
	print var2

print(myList[1])
print var2
