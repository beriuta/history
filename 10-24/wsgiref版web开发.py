import time
from wsgiref.simple_server import make_server


# 定义处理用户请求的函数
def index(url):
    with open('index.html', 'r', encoding='utf-8') as f:
        html_s = f.read()
        now = str(time.time())
        msg = html_s.replace('@@xx@@', now)
        return bytes(msg, encoding='utf-8')


def home(url):
    s = '你访问的是主页！'
    return bytes(s, encoding='utf-8')


def dabs(url):
    return bytes('来跳舞！', encoding='utf-8')


def login(url):
    with open('login.html', 'rb') as f:
        return f.read()


url_lst = [
    ('/index/', index),
    ('/home/', home),
    ('/dabs/', dabs),
    ('/login/', login),
]


def run_server(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8'), ])
    url = environ['PATH_INFO']  # 取到用户输入的URL
    func = None
    for i in url_lst:
        if i[0] == url:
            func = i[1]
            break
    if func:
        msg = func(url)
    else:
        msg = b'404 Not Found!'
    return [msg, ]


if __name__ == '__main__':
    httpd = make_server('127.0.0.1', 8080, run_server)
    print('我在8080等你哦...')
    httpd.sever_forever()
