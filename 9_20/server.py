from socket import *
from multiprocessing import Pool
import os
sk = socket(AF_INET,SOCK_STREAM)
sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sk.bind(('192.168.16.108',9001))
sk.listen(5)
def tail(conn):
    print('进程pid:{}'.format(os.getpid()))
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:break
            conn.send(msg.upper())
        except Exception:
            break
if __name__ == '__main__':
    p = Pool()
    while True:
        conn,_ = sk.accept()
        p.apply_async(tail,args=(conn,))

