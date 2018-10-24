import time
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()


# 定义处理用户请求的函数
def index(url):
    with open('index.html', 'r') as f:
        html_s = f.read()
        now = str(time.time())
        msg = html_s.replace('@@xx@@', now)
        return bytes(msg, encoding='utf-8')


def home(url):
    s = '你访问的是{}页面'.format(url)
    return bytes(s, encoding='utf-8')


def seite(url):
    return bytes('我实在想不出广告词了！', encoding='utf-8')


def Not_Found(url):
    return bytes('404 Not Found!', encoding='utf-8')


def login(url):
    with open('login2.html', 'rb') as f:
        return f.read()


# 定义一个用户访问的URL和将要执行的 函数的对应关系
url_lst = [
    ('/index/', index),
    ('/home/', home),
    ('/seite/', seite),
    ('/login/', login)
]

while 1:
    conn, addr = sk.accept()
    ret = conn.recv(8900)
    ret_str = str(ret, encoding='utf-8')
    lst = ret_str.split('\r\n')
    url = lst[0].split()[1]
    func = dict([i for i in url_lst]).get(url, Not_Found)
    msg = func(url)
    conn.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n')
    conn.send(msg)
    conn.close()
