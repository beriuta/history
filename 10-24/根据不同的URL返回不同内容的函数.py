import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8090))
sk.listen()

def index(url):
    return bytes('你访问的是index页面',encoding='utf-8')

def home(url):
    s = '你访问的是{}页面!'.format(url)
    return bytes(s,encoding='utf-8')


while 1:
    conn, addr = sk.accept()
    ret = conn.recv(9000)
    ret_str = str(ret,encoding='utf-8')  # 转换成字符串
    # 按照\r\n分割字符串
    list1 = ret_str.split('\r\n')
    url = list1[0].split()[1]
    print(url)
    if url == '/index/':
        msg = index(url)
    elif url == '/home/':
        msg = home(url)
    else:
       msg = b'404 Not Found!'
    conn.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n')
    # 先发送响应行
    conn.send(msg)  #发送相应数据
    conn.close()