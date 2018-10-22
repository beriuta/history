# import socketserver
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         while True:
#             conn.send(b'hello')
#             print(conn.recv(1024))
# server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
# server.serve_forever()
# import socketserver
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         while True:
#             conn.send(b'hello')
#             print(conn.recv(1024))
# server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
# server.serve_forever()
# import socketserver
# class Myserver(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         while True:
#             conn.send(b'hello')
#             print(conn.recv(1024))
# server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
# server.serve_forever()
'''
局域网中两台机器的通信原理：
交换机
ip地址
ip地址-arp协议->mac地址
mac地址：全球唯一
arp协议：广播 和 单播
    通过ip地址获取mac地址
    一台机器a发起一个arp请求（只包含ip地址），发送给交换机
    交换机接受到请求，广播这条消息
    所有的机器都会接受到这个请求，只有和要寻找ip地址吻合的机器b
    才会回应交换机的广播，（带着自己的mac地址）
    交换机通过单薄的形式将回复的B的mac地址发送给a


'''









