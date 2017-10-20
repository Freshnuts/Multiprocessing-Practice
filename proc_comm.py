import sys
import os
import time
import multiprocessing
import signal

q1 = multiprocessing.Queue()

def main():
    while 1:
        print "\n1. Create Process\n2. Send Single Command\n3. Shell"
        option = raw_input("#:> ")

        if option == "1":
            print "Creating a Process."
            proc_create()
        elif option == "2":
            print "Send Command to Child process from main()."
            opt = raw_input("Enter Command: ")
            q1.put(opt)
            time.sleep(1)
            continue
        elif option == "3":
            print "Interactive shell."
            while True:
                cmd = raw_input("fresh#> ")
                if cmd == "quit":
                    break
                q1.put(cmd)

        elif option == "q":
            print "Quit"
            break
        else:
            print "Error."
            continue

def proc_create():
    global p
    p = multiprocessing.Pool(1, proc_1,(q1, ))

def proc_1(q1):
    print "[+] PID: " , os.getpid()
    while True:
        item = q1.get(True)
        os.system(item)                


main()
