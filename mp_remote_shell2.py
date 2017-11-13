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

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except:
    print "Couldn't create socket!"
    exit()

try:
    s.bind((host,port))
except:
    print "Couldn't bind socket!"
    exit()

print "[+] Listening"
s.listen(2)

q = multiprocessing.Queue()



def acpt():
    global i
    global conn
    global addr
    i = 1
    while 1:
        conn, addr = s.accept()
        p = multiprocessing.Process(target=cmd)
        p.start()
        p.join()
        i += 1

def cmd():
    print "====== OPEN CONNECTION ======="
    print "%d: Target Connection: %s" % (i, addr)
    conn.send("9j3b3k8")
    print conn.recv(1024)
    print "[+] Scan Complete"
    print "[*] Closing Connection: %s", addr
    print "====== CLOSED CONNECTION ======\n\n"
    time.sleep(1)

acpt()
