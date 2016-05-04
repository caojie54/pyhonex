# -*- coding:utf-8 -*-
import time,threading
balance=0
def change_it(n):
    global balance
    balance=balance+n
    balance=balance-n
    #balance赋值有两个过程：1，新建临时变量x=balance+n，将临时变量的值赋给balance
lock=threading.Lock()
def thread_run(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t1=threading.Thread(target=thread_run,args=(5,))
t2=threading.Thread(target=thread_run,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()

print(balance)


