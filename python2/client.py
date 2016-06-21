import math
import socket
import sys
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9999))

s.recv(1024)
s.send('tipi\n')
s.recv(1024)
s.send('d5553209027095297fc550bb2c4cc4ae\n')
s.recv(1024)
s.send('10000\n')
s.recv(1024)

answer = s.recv(1024)
current_guess=10000
prev_prev_guess=0
prev_guess=0

while (answer):

        if (answer == "nope. Try something bigger\n"):
                prev_prev_guess=prev_guess
                prev_guess=current_guess
                current_guess = (prev_guess + abs(prev_prev_guess - prev_guess)/2)

                s.send(str(current_guess)+'\n')
                answer = s.recv(1024)

        elif (answer == "nope. Try something smaller\n"):
                prev_prev_guess=prev_guess
                prev_guess=current_guess
                current_guess = (prev_guess - abs(prev_guess - prev_prev_guess)/2)

                s.send(str(current_guess)+'\n')
                answer = s.recv(1024)

        else:
                print current_guess
                print answer
                break

command = s.recv(1024)
list = []
list2 = []
list = command.split('\n')
list = list[1:9]
print list

f = open("file", "w")
f.write("\n".join(map(lambda x: str(x), list)))
f.close()

pickled_date = open('file', 'r')
date = pickle.load(pickled_date)
pickled_date.close()

print date
s.send(str(date)[-6:]+'\n')

s.recv(1024)
print s.recv(1024)



----------------------------------                


import math
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9999))

s.recv(1024)
s.send('tipi\n')
s.recv(1024)
s.send('d5553209027095297fc550bb2c4cc4ae\n')
s.recv(1024)
s.send('10000\n')
s.recv(1024)

answer = s.recv(1024)
current_guess=10000
prev_guess=0

while (answer):

        if (answer == "nope. Try something bigger\n"):
                prev_guess=current_guess
                current_guess = (prev_guess + abs(10000 - prev_guess)/2)

                s.send(str(current_guess)+'\n')
                answer = s.recv(1024)

        elif (answer == "nope. Try something smaller\n"):
                prev_prev_guess=prev_guess
                prev_guess=current_guess
                current_guess = (prev_guess - abs(prev_guess - prev_prev_guess)/2)

                s.send(str(current_guess)+'\n')
                answer = s.recv(1024)

        else:
                print current_guess
                print answer
                break
        
        
        
        
        
        
        