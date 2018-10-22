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















