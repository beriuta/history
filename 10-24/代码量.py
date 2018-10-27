< !DOCTYPE
html >
< html
lang = "en" >
< head >
< meta
charset = "UTF-8" >
< title > 登录页面 < / title >
< link
rel = "stylesheet"
href = "bootstrap-3.3.7/css/bootstrap.css" >
< style >
body
{
    background - color:  # eeeeee;
}
< / style >
< / head >
< body >

< div


class ="container" >

< div


class ="row" >

< div


class ="col-md-4 col-md-offset-4" style="margin-top: 70px" >

< h2


class ="text-center" > 欢迎登陆 < / h2 >

< form >
< div


class ="form-group" >

< label
for ="exampleInputEmail1" > 邮箱 < / label >
< input
type = "email"


class ="form-control" id="exampleInputEmail1" placeholder="Email" >

< span


class ="help-block" > < / span >

< / div >
< div


class ="form-group" >

< label
for ="exampleInputPassword1" > 密码 < / label >
< input
type = "password"


class ="form-control" id="exampleInputPassword1" placeholder="Password" >

< span


class ="help-block" > < / span >

< / div >
< div


class ="checkbox" >

< label >
< input
type = "checkbox" > 记住
< / label >
< / div >
< button
type = "submit"
id = "login-btn"


class ="btn btn-success btn-block" > 登录 < / button >

< / form >
< / div >
< / div >
< / div >

< script
src = "jquery.js" > < / script >
< script >
// 给登录绑定事件
$('#login-btn').click(function()
{
// 定义一个允许提交的标志位
var
flag = true;
// 找到登录框所有的input框，判断是否为空
$('form input').each(function()
{ // each是遍历每一个DOM对象
var
value = $(this).val();
if (value.length === 0)
{
// 为空就显示提示信息
// 提示信息出现在下框中
var
errMsg = $(this).prev().text() + '不能为空';
$(this).next().text(errMsg);
// 给父标签设置has - error的样式
$(this).parent().addClass('has-error');
// 阻止表单提交
flag = false;
return false;
}
});
return flag;
});
// 给input框绑定focus事件
$('form input').focus(function()
{ // 当失去焦点时就会触发
// 取到当前input框后面的span标签的文本
$(this).next().text('');
// 去掉父标签的额has - error样式
$(this).parent().removeClass('has-error');
})

< / script >
    < / body >
        < / html >
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="x-ua-compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>用户列表</title>
</head>
<body>
    <table border="1">
        <thead>
            <tr>
                <th>id值</th>
                <th>姓名</th>
                <th>密码</th>
            </tr>
        </thead>
        <tbody>
            {% for user in user_list %}
                <tr>
                    <td>{{user.id}}</td>
                    <td>{{user.username}}</td>
                    <td>{{user.password}}</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>

</body>
</html>
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
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()


def index(url):
    s = '您访问的是{}网页！'.format(url)
    return bytes(s, encoding='utf-8')


def home(url):
    return bytes('您现在在首页！', encoding='utf-8')


def seite(url):
    return bytes('我实在想不出广告词了！', encoding='utf-8')

def Not_Found(url):
    return bytes('404 Not Found!',encoding='utf-8')

url_lst = [
    ('/index/', index),
    ('/home/', home),
    ('/seite/', seite)
]

while 1:
    conn, addr = sk.accept()
    ret = conn.recv(9000)
    ret_str = str(ret, encoding='utf-8')
    list1 = ret_str.split('\r\n')
    url = list1[0].split()[1]
    print(url)
    # func = None
    func = dict([i for i in url_lst]).get(url, Not_Found)
    msg = func(url)
    print(msg)
    conn.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n')
    conn.send(msg)
    conn.close()
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
    import socket

    sk = socket.socket()
    sk.bind(('127.0.0.1', 8090))
    sk.listen()


    def index(url):
        return bytes('你访问的是index页面', encoding='utf-8')


    def home(url):
        s = '你访问的是{}页面!'.format(url)
        return bytes(s, encoding='utf-8')


    while 1:
        conn, addr = sk.accept()
        ret = conn.recv(9000)
        ret_str = str(ret, encoding='utf-8')  # 转换成字符串
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
        conn.send(msg)  # 发送相应数据
        conn.close()
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
import time
import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8080))
sk.listen()
# 定义处理用户请求的函数
def index(url):
    with open('index.html','r') as f:
        html_s = f.read()
        now = str(time.time())
        msg = html_s.replace('@@xx@@',now)
        return bytes(msg,encoding='utf-8')

def home(url):
    s = '你访问的是{}页面'.format(url)
    return bytes(s,encoding='utf-8')

def seite(url):
    return bytes('我实在想不出广告词了！', encoding='utf-8')

def Not_Found(url):
    return bytes('404 Not Found!',encoding='utf-8')
url_lst = [
    ('/index/', index),
    ('/home/', home),
    ('/seite/', seite)
]