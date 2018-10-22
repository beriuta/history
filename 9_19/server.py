import socket
from multiprocessing import Process
def communicate(conn):
    while True:
        conn.send(b'hello')
        print(conn.recv(1024))
if __name__ == '__main__':
        sk = socket.socket()
        sk.bind(('192.168.16.108',9001))
        sk.listen()
        while True:
            conn,addr = sk.accept()
            Process(target=communicate,args=(conn,)).start()