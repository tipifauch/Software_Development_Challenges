import sys

list = []
result = []

for line in sys.stdin:
    list.append(line)
 
def sequence(site_adress):
    
    for i in range (0, len(list)):  
        var1,var2 = list[i].split(' <-- ')
        var1,var2 = var1.strip(), var2.strip()

        if var1 == site_adress:
            if var2 != '[none]':
                result.append(var2)
                new_site = var2
                sequence(new_site)
            else:
                break
                        
result.append(sys.argv[1])
sequence(sys.argv[1])

for i in range (0, len(result)):
    print str(i+1) + '. ' + result[len(result)-1-i]

