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















