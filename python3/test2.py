import sys


def define_block(block):
    
    file = open(block,"r")
    
    list = []
    colums_list = []
    lines_list = []

    for line in file:
        list.append(line)
    
    for i in range(len(list)):
        list[i] = str(list[i]).replace(' ', '0')
        list[i] = str(list[i]).replace('\n', '')
    
        list[i] = str(list[i]).replace('A', '1')
        list[i] = str(list[i]).replace('B', '1')
        list[i] = str(list[i]).replace('C', '1')
        list[i] = str(list[i]).replace('D', '1')
        list[i] = str(list[i]).replace('E', '1')
        list[i] = str(list[i]).replace('F', '1')
        list[i] = str(list[i]).replace('G', '1')
    
    list = filter(None, list)

    for i in range(len(list)-1):
        if (len(list[i]) < len(list[i+1])):
            list[i]=list[i]+'0'

    for i in range(len(list)-1):
        if (len(list[i]) > len(list[i+1])):
            list[i+1]=list[i+1]+'0'

    colums_to_add = 5-len(list[0])
    lines_to_add = 5-len(list)
    
    for c in range(colums_to_add+1):
        new_item = ''
        for i in range(len(list)):
            new_item=new_item+c*'0'+list[i]+(colums_to_add - c)*'0'
        colums_list.append(new_item)
    print colums_list

    for i in range(len(colums_list)):
        for l in range(lines_to_add+1):
            new_item = '1'+l*5*'0'+colums_list[i]+(lines_to_add - l)*5*'0'
            lines_list.append(int(new_item))

    return lines_list       

listA = define_block(sys.argv[1])
listB = define_block(sys.argv[2])
listC = define_block(sys.argv[3])
listD = define_block(sys.argv[4])
listE = define_block(sys.argv[5])
listF = define_block(sys.argv[6])
listG = define_block(sys.argv[7])

print 'listA'
print listA

# print 'listB'
# print listB
#
# print 'listC'
# print listC
#
# print 'listD'
# print listD
#
# print 'listE'
# print listE
#
# print 'listF'
# print listF
#
# print 'listG'
# print listG


