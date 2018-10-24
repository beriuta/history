import socket
sk = socket.socket()
sk.bind(('127.0.0.1', 8090))
sk.listen()

while 1:
    conn, addr = sk.accept()
    ret = conn.recv(9000)
    # print(ret)  # 用户发送的请求消息
    # 从请求的消息中拿到请求的URL是什么
    # data_str = str(ret,encoding='utf-8')  # 转换成字符串类型
    ret_str = ret.decode(encoding='utf-8',errors='ignore')
    # 按照\r\n分割
    list1 = ret_str.split('\r\n')
    url = list1[0].split()[1]
    print(url)
    if url == '/index/':
        msg = 'this is index page!'
    elif url == '/home/':
        msg = 'this is home page!'
    else:
        msg = '404 NOT Found!'
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')  # 先发送响应行
    conn.send(bytes(msg, encoding='utf-8'))  # 发送响应数据
    conn.close()