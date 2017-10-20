import os
from multiprocessing import Process, Pipe


def f(conn):
    print "Child #1 PID: %s, Sending  'x'" % os.getpid()
    conn.send("x")
    print "Child #1 PID: %s, Received '%s'" % (os.getpid(), conn.recv())
    conn.close

def f_proc():
    print "Parent   PID: %s" % os.getpid()
    parent_c, child_c = Pipe()
    p = Process(target=f, args=(child_c, ))
    p.start()
    print "Parent   PID: %s, Received '%s'" % (os.getpid(), parent_c.recv())
    parent_c.send("x2")



f_proc()
