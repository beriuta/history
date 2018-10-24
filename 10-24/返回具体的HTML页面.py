import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8000))
sk.listen()

def index(url):
    s = '您访问的是{}网页！'.format(url)
    return bytes(s, encoding='utf-8')


def home(url):
    return bytes('您现在在首页！', encoding='utf-8')


def seite(url):
    return bytes('我实在想不出广告词了！', encoding='utf-8')

def login(url):
    with open('login.html','rb') as f1:
        return f1.read()

def Not_Found(url):
    return bytes('404 Not Found!',encoding='utf-8')


url_lst = [
    ('/index/', index),
    ('/home/', home),
    ('/seite/', seite),
    ('/login/',login),
]

while 1:
    conn, addr = sk.accept()
    ret = conn.recv(9000)
    ret_str = str(ret, encoding='utf-8')
    list1 = ret_str.split('\r\n')
    url = list1[0].split()[1]
    # print(url)
    # func = None
    func = dict([i for i in url_lst]).get(url, Not_Found)
    msg = func(url)
    print(msg)
    conn.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n')
    conn.send(msg)
    conn.close()























