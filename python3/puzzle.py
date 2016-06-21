#python3
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

    for i in range(len(colums_list)):
        for l in range(lines_to_add+1):
            new_item = '1'+l*5*'0'+colums_list[i]+(lines_to_add - l)*5*'0'
            lines_list.append(int(new_item))

    return lines_list 



def add():
    if '2' in str(sum(done_list)):
        return -1
    else:
        return 1



def puzzle():       
    for a in range(len(listA)):
        done_list[0]=listA[a]
        done_list[-6:]=[10000000000000000000000000, 10000000000000000000000000, 10000000000000000000000000, 10000000000000000000000000, 10000000000000000000000000, 10000000000000000000000000]
        # print 'a = '+str(a)
        # print done_list
        if add()==-1:
            # print 'I try the next position for block A'
            done_list[0]=10000000000000000000000000
        else:

            for b in range(len(listB)):
                done_list[1]=listB[b]
                done_list[-5:]=[10000000000000000000000000, 10000000000000000000000000, 10000000000000000000000000, 10000000000000000000000000, 10000000000000000000000000]
                # print 'a = '+str(a)+', b = '+str(b)
                # print done_list
                if add()==-1:
                        # print "I try the next position for block B"
                        done_list[1]=10000000000000000000000000
                else:
        
                    for c in range(len(listC)):
                        done_list[2]=listC[c]
                        done_list[-4:]=[10000000000000000000000000, 10000000000000000000000000, 10000000000000000000000000, 10000000000000000000000000]
                        # print 'a = '+str(a)+', b = '+str(b)+', c = '+str(c)
                        # print done_list
                        if add()==-1:
                            # print "I try the next position for block C"
                            done_list[2]=10000000000000000000000000
                        else:  
                
                            for d in range(len(listD)):
                                done_list[3]=listD[d]
                                done_list[-3:]=[10000000000000000000000000, 10000000000000000000000000, 10000000000000000000000000]                            
                                # print 'a = '+str(a)+', b = '+str(b)+', c = '+str(c)+', d = '+str(d)
                                # print done_list
                                if add()==-1:
                                    # print "I try the next position for block D"
                                    done_list[3]=10000000000000000000000000
                                else:
                        
                                    for e in range(len(listE)):
                                        done_list[4]=listE[e]
                                        done_list[-2:]=[10000000000000000000000000, 10000000000000000000000000]
                                        # print 'a = '+str(a)+', b = '+str(b)+', c = '+str(c)+', d = '+str(d)+', e = '+str(e)
                                        # print done_list
                                        if add()==-1:
                                            # print "I try the next position for block E"
                                            done_list[4]=10000000000000000000000000
                                        else:
                                
                                            for f in range(len(listF)):
                                                done_list[5]=listF[f]
                                                done_list[6]=10000000000000000000000000
                                                # print 'a = '+str(a)+', b = '+str(b)+', c = '+str(c)+', d = '+str(d)+', e = '+str(e)+', f = '+str(f)
                                                # print done_list
                                                if add()==-1:
                                                    # print "I try the next position for block F"
                                                    done_list[5]=10000000000000000000000000
                                                else:
                                        
                                                    for g in range(len(listG)):
                                                        done_list[6]=listG[g]
                                                        # print 'a = '+str(a)+', b = '+str(b)+', c = '+str(c)+', d = '+str(d)+', e = '+str(e)+', f = '+str(f)+', g = '+str(g)
                                                        # print done_list
                                                        if add()==-1:
                                                            # print "I try the next position for block G"
                                                            done_list[6]=10000000000000000000000000
                                                        else:
                                                            # print "I am done"
                                                            # print done_list
                                                            return done_list



listA = define_block(sys.argv[1])
listB = define_block(sys.argv[2])
listC = define_block(sys.argv[3])
listD = define_block(sys.argv[4])
listE = define_block(sys.argv[5])
listF = define_block(sys.argv[6])
listG = define_block(sys.argv[7])

done_list = [10000000000000000000000000, 10000000000000000000000000, 10000000000000000000000000, 10000000000000000000000000,
10000000000000000000000000, 10000000000000000000000000, 10000000000000000000000000]

puzzle()

done_list[0] = 1*done_list[0]
done_list[1] = 2*done_list[1]
done_list[2] = 3*done_list[2]
done_list[3] = 4*done_list[3]
done_list[4] = 5*done_list[4]
done_list[5] = 6*done_list[5]
done_list[6] = 7*done_list[6]

sum = sum(done_list)
sum = str(sum)[2:]

sum = sum.replace('1', 'A')
sum = sum.replace('2', 'B')
sum = sum.replace('3', 'C')
sum = sum.replace('4', 'D')
sum = sum.replace('5', 'E')
sum = sum.replace('6', 'F')
sum = sum.replace('7', 'G')


square = sum[:5]+'\n'+sum[5:10]+'\n'+sum[10:15]+'\n'+sum[15:20]+'\n'+sum[20:25]

print square


 

