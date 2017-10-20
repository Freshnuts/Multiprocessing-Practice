import sys
import os
from multiprocessing import Process
import multiprocessing
import time
import socket



# Demonstrates multirocessing with loop to keep track of initialized
# processes. 

# t1 calls multiprocessing.Process()  p01 (Process Thread 1).
# t2 calls multiprocessing.Process()  p02 (Process Thread 2).

# t1shell Initializes p01. (Process Thread 1 Executes)
# t2shell Initializes p02. (Process Thread 2 Executes)

# c = counter, the variable is used to check whether p01/p02 have been
# called before attempting to initialize p01/p02. If The check isn't
# performed, program crashes.


host = ''
port = 443

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)

q = multiprocessing.Queue()

def looper(q):
    os.system('/bin/bash')

def t3s(q):
    conn.send("id")
    print "command sent"
    time.sleep(1)

def acpt():
    global p03
    global conn
    conn, addr = s.accept()
    p03 = multiprocessing.Process(target=t3s, args=('q', ))
    print "t3shell activated"

def main():
    global c
    c = 0
    while True:
        print "\nt1 for thread 1\nt2 for thread 2\nq to quit"
        read = raw_input("?: ")
        print read
        if read == "t1":
            c += 1
            p01 = multiprocessing.Process(target=looper, args=('q', ))
            print "[+] Type in 't1shell' to activate thread 1."
        elif read == "t2":
            c += 1
            p02 = multiprocessing.Process(target=looper, args=('q', ))
            print "[+] Enter 't2shell' to activate thread 2."
        elif read == "q":
            exit()
        elif read == "t1shell":
            if c > 0:
                p01.start()
                p01.join()
                c -= 1
            else:
                print "p01 not initialized"
        elif read == "t2shell":
            if c > 0:
                p02.start()
                p02.join()
                c -= 1
        elif read == "t3shell":
                p03.start()
        else:
            print "Check your spelling"

acpt()
main()
