from multiprocessing import Process, Manager


# Append elements in global list from multiprocesses
def f(l):
    l.append(str(1))
    l.append(str(2))

l = Manager().list()

p = Process(target=f, args=(l, ))
p.start()
p.join()

print l
