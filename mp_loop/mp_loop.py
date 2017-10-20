import sys
import os
from multiprocessing import Process
import multiprocessing
import time


# Demonstrates multiprocessing with number loop to keep track of initialized
# processes. 

# t1 calls multiprocessing.Process()  p01 (Process Thread 1).
# t2 calls multiprocessing.Process()  p02 (Process Thread 2).

# t1loop Initializes p01. (Process Thread 1 Executes)
# t2loop Initializes p02. (Process Thread 2 Executes)

# c = counter, the variable is used to check whether p01/p02 have been
# called before attempting to initialize p01/p02. If The check isn't
# performed, program crashes.


q = multiprocessing.Queue()

def looper(q):
    for i in range(20):
        print "Thread loop: %d" % i
        time.sleep(1)


# t1loop - p01.start() allows user to start thread t2, while t1 is looping.
# t1join  - p01.start(), p01.join() LOCKS user in thread t1 execution until
# it's done.
# After initializing 't1' with 't1loop', use 't1join' to LOCK thread
# in the MIDDLE of 't1' execution.

def main():
    c = 0
    while True:
        print "\n't1' for thread 1"
        print "'t2' for thread 2"
        print "'t1loop' to initialize multiprocess.Process()"
        print "'t1join' lock thread AFTER initiated by 't1loop'."
        print "'t1lock' to lock on thread from beginning"
        print "'q' for quit"
        read = raw_input("?: ")
        print read
        if read == "t1":
            c += 1
            p01 = multiprocessing.Process(target=looper, args=('q', ))
            print "[+] Type in 't1loop' to activate thread 1."
        elif read == "t2":
            c += 1
            p02 = multiprocessing.Process(target=looper, args=('q', ))
            print "[+] Enter 't2loop' to activate thread 2."
        elif read == "q":
            exit()
        elif read == "t1loop":
            if c > 0:
                p01.start()
            else:
                print "p01 not initialized"
        elif read == "t1join":
            if c > 0:
                p01.join()
            else:
                print "p01 not initialized"
                c = 0
        elif read == "t1lock":
            if c > 0:
                p01.start()
                p01.join()
            else:
                print "p01 not initialized"
                c = 0
        elif read == "t2loop":
            if c > 0:
                p02.start()
                p02.join()
                c = 0
        else:
            print "Check your spelling"

main()
