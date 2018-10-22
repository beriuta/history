# import socket
# sk = socket.socket()
# sk.bind(('192.168.16.108',9001))
# sk.settimeout()
# sk.listen()
# while True:
#     try:
#         conn,addr = sk.accept()   #如果没人连也不会等待
#     except BlockingIOError:
#         conn.recv()     #也不阻塞     但是会比较浪费CPU资源，会一直占用cup
# import socket
# sk = socket.socket()
# sk.bind(('192.168.16.108',9001))
# sk.settimeout()
# sk.listen()
# while True:
#     try:
#         conn,addr = sk.accept()
#     except BlockingIOError:
#         conn.recv()
# import os
# import time
# from multiprocessing import Process
# def func():
#     for i in range(10):
#         time.sleep(0.5)
#         print('子进程:',os.getpid(),os.getppid())
# if __name__ == '__main__':
#     print('主进程:',os.getpid(),os.getppid())
#     p = Process(target=func)
#     p.start()
#     for i in range(10):
#         time.sleep(0.3)
#         print('*' * i)
# def func(arg):
#     for i in range(10):
#         time.sleep(0.3)
#         print('子进程%s:'% arg,os.getpid(),os.getppid())
# if __name__ == '__main__':
#     print('主进程',os.getpid(),os.getppid())
#     p = Process(target=func,args= (1,))
#     p.start()
#     for i in range(10):
#         time.sleep(0.3)
#         print('*' * i)
# import os
# import time
# from multiprocessing import Process
# count = 100
# def func():
#     global count
#     count -= 1
#     print('子进程:',count)                 #子进程: 99
# if __name__ == '__main__':
#     print('主进程:',os.getpid(),os.getppid())            #主进程: 16387 2953
#     p = Process(target=func)
#     p.start()
#     time.sleep(2)
#     print('主进程:',count)                 #主进程: 100
# def func(arg):
#     print('子进程%s:'%arg,os.getpid(),os.getppid())
#     time.sleep(5)
#     print('子进程end')
# if __name__ == '__main__':
#     for i in range(10):
#         Process(target=func,args=(i,)).start()
#     print('父进程***********')         #父进程先启动,启动之后就不管了,子进程爱咋地咋地
# import os
# import hmac
# secret_key = b'blabla'
# msg = os.urandom(32)  #os.urandom(n)的作用：随即产生n个字节的字符串，可以作为随机加密key使用~
# result = hmac.new(secret_key,msg)
# print(result)       #<hmac.HMAC object at 0x000001F6285EE5C0>
# print(result.hexdigest())  #09f3d859d949b19470f6a2d8f3401e9c
# import os
# import hmac
# import socket
# def auth(conn):
#     msg = os.urandom(32) #随机生成一个字符串
#     conn.send(msg)     #发送到silent端
#     result = hmac.new(secret_key,msg)  #处理这个随机字符串，得到一个结果 key两边都是一样的，发送的随机字符串是每次都不一样的
#     client_digest = conn.recv(1024)   #接收client端处理的结果
#     if result.hexdigest() == client_digest.decode('utf-8'):
#         print('合法连接')    #对比成功可以继续通信
#         return True
#     else:
#         print('不合法的连接')   #不成功，close
#         return False
# secret_key = b'blabla'
# sk = socket.socket()
# sk.bind(('192.168.16.108',9001))
# sk.listen()
# conn,addr = sk.accept()
# if auth(conn):
#     print(conn.recv(1024))   #正常的和client端进行沟通了
#     conn.close()
# else:
#     conn.close()
# sk.close()
# import hmac
# import os
# import socket
# def auth(conn):
#     msg = os.urandom(32)
#     conn.send(msg)
#     result = hmac.new(secret_key,msg)
#     client_digest = conn.recv(1024)
#     if result.hexdigest() == client_digest.decode('utf-8'):
#         print('是合法链接')
#         return True
#     else:
#         print('不合法链接')
#         return False
# secret_key = b'hello'
# sk = socket.socket()
# sk.bind(('192.168.16.108',9001))
# sk.listen()
# conn,addr = sk.accept()
# if auth(conn):
#     print(conn.recv(1024))
#     conn.close()
# else:
#     conn.close()
# sk.close()
# import os
# import hmac
# import socket
# def auth(conn):
#     msg = os.urandom(32)
#     conn.send(msg)
#     result = hmac.new(secret_key,msg)
#     client_digest = conn.recv(1024)
#     if result.hexdigest() == client_digest.decode('utf-8'):
#         print('是合法链接')
#         return True
#     else:
#         print('不合法链接')
#         return False
# secret_key = b'hello'
# sk = socket.socket()
# sk.bind(('192.168.16.108',9001))
# sk.listen()
# conn,addr = sk.accept()
# if auth(conn):
#     print((conn.recv(1024)).decode('utf-8'))
#     conn.close()
# else:
#     conn.close()
# sk.close()
# import socket
# sk = socket.socket()
# sk.bind(('192.168.16.108',9001))
# sk.listen()
# while True:
#     conn,addr = sk.accept()
#     while True:
#         conn.send(b'hello')
#         print(conn.recv(1024))
# import socketserver   #tcp协议就不需要导入socket
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         while True:
#             conn.send(b'hello')
#             print(conn.recv(1024))
# server = socketserver.ThreadingTCPServer(('192.168.16.108',9001),Myserver)
# server.serve_forever()
# import hmac   #实现一个简单的客户端链接认证功能，利用hmac加盐的方式
# import socket
# def auth(sk):
#     msg = sk.recv(32)
#     result = hmac.new(key,msg)   #key就是盐
#     res = result.hexdigest()
#     sk.send(res.encode('utf-8'))
# key = b'blabla'
# sk = socket.socket()
# sk.connect(('192.168.16.108',9001))
# auth(sk)
# sk.send(b'upload')
# sk.close()
# import hmac
# import socket
# def auth(sk):
#     msg = sk.recv(32)
#     result = hmac.new(key,msg)
#     res = result.hexdigest()
#     sk.send(res.encode('utf-8'))
# key = b'hello'
# sk = socket.socket()
# sk.connect(('192.168.16.108',9001))
# auth(sk)
# sk.send(b'hellode')
# sk.close()
# import hmac
# import socket
# def auth(sk):
#     msg = sk.recv(32)
#     result = hmac.new(key,msg)
#     res = result.hexdigest()
#     sk.send(res.encode('utf-8'))
# key = b'hello'
# sk = socket.socket()
# sk.connect(('192.168.16.108',9001))
# auth(sk)
# sk.send('可以执行其他的沟通了'.encode('utf-8'))
# import socket
# sk = socket.socket()
# sk.connect(('192.168.16.108',9001))
# while True:
#     ret = sk.recv(1024)
#     print(ret)
#     sk.send(b'byebye')
# sk.close()