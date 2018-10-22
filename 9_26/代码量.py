# from urllib.request import urlopen
# import re
# import json
# def getPage(url):
#     response = urlopen(url)
#     content = response.read().decode('utf-8')
#     return content
# def parsePage(s):
#     ret = com.finditer(s)
#     for i in ret:
#         yield {
#             "id": i.group("id"),
#             "title": i.group("title"),
#             "rating_num": i.group("rating_num"),
#             "comment_num": i.group("comment_num"),
#         }
# def main(num):
#     url = 'https://movie.douban.com/top250?start=%s&filter=' %num
#     response_html = getPage(url)
#     ret = parsePage(response_html)
#     print(ret)
#     f = open("move_info7",'a',encoding='utf-8')
#     for obj in ret:
#         print(obj)
#         data = json.dump(obj,ensure_ascii=False)
#         f.write(data + '\n')
#     f.close()
# if __name__ == '__main__':
#     com = re.compile(
#         '<div class="item">.*?<div class="pic">.*?<em .*?>(?P<id>\d+).*?<span class="title">(?P<title>.*?)</span>'
#         '.*?<span class="rating_num" .*?>(?P<rating_num>.*?)</span>.*?<span>(?P<comment_num>.*?)评价</span>',re.S
#     )
#     count = 0
#     for i in range(10):
#         main(count)
#         count += 25
# from urllib.request import urlopen
# ret = urlopen('https://movie.douban.com/top250?start=225&filter=')
# content = ret.read().decode('utf-8')
# print(type(content))
# import time
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# def func(i):
#     print('thread',i)
#     time.sleep(1)
#     print('thread %s end'%i)
# if __name__ == '__main__':
#     tp = ProcessPoolExecutor(5)  #开启五个进程
#     tp.submit(func,1)  #按位置传参
#     tp.shutdown()
#     print('主进程')
# import time
# from concurrent.futures import ThreadPoolExecutor
# from threading import current_thread as cthread
# def func(i):
#     print('thread %s'%i)
#     time.sleep(1)
#     print('thread %s end'%i)
# tp = ThreadPoolExecutor(5)   #开启5个线程
# for i in range(20):           #开启20个任务
#     tp.submit(func,i)
# tp.shutdown()  #阻塞直到任务完成
# print('主线程')
#获取返回值
# import time
# from concurrent.futures import ThreadPoolExecutor
# from threading import current_thread as cthread
# def func(i):
#     print('thread',i,cthread().ident)
#     time.sleep(1)
#     print('thread %s end'%i)
#     return i * '*'
# tp = ThreadPoolExecutor(5)
# ret_l = []
# for i in range(20):
#     ret = tp.submit(func,i)
#     ret_l.append(ret)
# for ret in ret_l:
#     print(ret.result())
# print('主线程')
#回调函数
# import time
# from concurrent.futures import ThreadPoolExecutor
# from threading import current_thread as cthread
# #线程池的回调函数，是由子线程完成的，而进程则是由主进程完成的
# def func(i):
#     print('thread',i,cthread().ident)
#     time.sleep(1)
#     print('thread %s end'%i)
#     return i * '*'
# def call_back(arg):
#     print('call back:',cthread().ident)
#     print('ret:',arg.result())
# tp = ThreadPoolExecutor(5)
# det_l = []
# for i in range(20):
#     tp.submit(func,i).add_done_callback(call_back)  #加上回调函数
# print('主线程',cthread().ident)
# import os
# import time
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# def func(i):
#     print('thread',i,os.getpid())
#     time.sleep(1)
#     print('thread %s end'%i)
# if __name__ == '__main__':
#     tp = ProcessPoolExecutor(5)   #起了五个进程
#     tp.submit(func,1)
#     tp.shutdown()
#     print('主进程',os.getpid())
# '''
# thread 1 23455
# thread 1 end
# 主进程 23454   #主进程跟子进程的id不一样
# '''
# import os
# import time
# from concurrent.futures import ThreadPoolExecutor
# def func(i):
#     print('thread',i,os.getpid())
#     time.sleep(1)
#     print('thread %s end'%i)
# tp = ThreadPoolExecutor(5)
# tp.submit(func,1)
# tp.shutdown()
# print('主线程',os.getpid())
# '''
# thread 1 23824
# thread 1 end
# 主线程 23824  #主线程跟子线程的id一样
# '''
# import os
# import time
# from concurrent.futures import ProcessPoolExecutor
# from threading import current_thread as cthread
# def func(i):
#     print('thread',i,os.getpid())
#     time.sleep(1)
#     print('thread %s end'%i)
#     return i*'*'
# def call_back(arg):
#     print('call back:',os.getpid())
#     print('ret:',arg.result())
# if __name__ == '__main__':
#     tp = ProcessPoolExecutor(5)
#     ret_l = []
#     for i in range(20):
#         tp.submit(func,i).add_done_callback(call_back)
#     print('主进程',os.getpid())
# '''
# thread 0 24582
# 主进程 24581
# ...
# thread 5 24582
# call back: 24581
# ret:
# thread 1 end
# thread 6 24584
# call back: 24581
# ret: *    call back 的ip跟主进程的一样
# '''
# def my_generator():
#     for i in range(10):
#         yield i   #保存当前程序的状态
# for num in my_generator():
#     print(num)
# def consumer():
#     g = producer()
#     for num in g:
#         print(num)
# def producer():
#     for i in range(1000):
#         yield i
# consumer()
# import time
# from greenlet import greenlet
# def eat():
#     print('eating 1')
#     g2.switch()
#     time.sleep(1)
#     print('eating 2')
# def play():
#     print('playing 1')
#     time.sleep(1)
#     print('playing 2')
#     g1.switch()
# g1 = greenlet(eat)
# g2 = greenlet(play)
# g1.switch()
# '''
# eating 1
# playing 1   #跟eating一起出现
# playing 2
# eating 2
# '''
# import time
# import gevent
# def eat():
#     print('eating 1')
#     time.sleep(1)
#     print('eating 2')
# def play():
#     print('playing 1')
#     time.sleep(1)
#     print('playing 2')
# g1 = gevent.spawn(eat)            #自动检测阻塞事件，遇见阻塞了就会进行切换，有些阻塞它不认识
# g2 = gevent.spawn(play)
# g1.join()   #阻塞直到g1结束
# g2.join()   #阻塞直到g2结束
# '''
# eating 1
# eating 2
# playing 1
# playing 2         #依旧按照顺序执行，并没有切换，是因为time模块它不认识
# '''
# from gevent import monkey;monkey.patch_thread()
# import time
# import gevent
# def eat():
#     print('eating 1')
#     time.sleep(1)
#     print('eating 2')
# def play():
#     print('playing 1')
#     time.sleep(1)
#     print('playing 2')
# g1 = gevent.spawn(eat)
# g2 = gevent.spawn(play)
# g1.join()
# g2.join()
# from gevent import monkey;monkey.patch_all()
# import time
# import gevent
# import requests
# url_lst = [
#     'http://www.baidu.com',
#     'http://www.4399.com',
#     'http://www.7k7k.com',
#     'http://www.sogou.com',
#     'http://www.sohu.com',
#     'http://www.sina.com',
#     'http://www.jd.com',
#     'https://www.douban.com',
#     'http://www.baidu.com',
#     'http://www.4399.com',
#     'http://www.7k7k.com',
#     'http://www.sogou.com',
#     'http://www.sohu.com',
#     'http://www.sina.com',
#     'http://www.jd.com',
#     'https://www.douban.com',
#     'http://www.baidu.com',
#     'http://www.4399.com',
#     'http://www.7k7k.com',
#     'http://www.sogou.com',
#     'http://www.sohu.com',
#     'http://www.sina.com',
#     'http://www.jd.com',
#     'https://www.douban.com',
#     'http://www.baidu.com',
#     'http://www.4399.com',
#     'http://www.7k7k.com',
#     'http://www.sogou.com',
#     'http://www.sohu.com',
#     'http://www.sina.com',
#     'http://www.jd.com',
#     'https://www.douban.com',
# ]
# def get_url(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         print(url,len(response.text))
# # start = time.time()
# # for url in url_lst:
# #     get_url(url)
# # print(time.time() - start)           #4.075298070907593
# start = time.time()
# g_lst = []
# for url in url_lst:
#     g = gevent.spawn(get_url,url)
#     g_lst.append(g)
# gevent.joinall(g_lst)
# print(time.time() - start)           #0.715653657913208
# import time
# import random
# from multiprocessing import Process,Queue
# def consumer(q,name):
#     while True:
#         food = q.get()
#         if food is None:break
#         time.sleep(random.uniform(0.5,1))
#         print('%s吃了一个%s'%(name,food))
# def producer(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(0.3,0.8))
#         print('%s生产了%s %s'%(name,food,i))
#         q.put(food + str(i))
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=consumer,args=(q,'ake'))
#     c2 = Process(target=consumer,args=(q,'bebe'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=producer,args=(q,'hha','hehe'))
#     p2 = Process(target=producer,args=(q,'hehe','xixi'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
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
# import socket
# sk = socket.socket()
# sk.connect(('127.0.0.1',9000))
# while True:
#     print(sk.recv(1024))
#     sk.send(b'byebye')
# from gevent import monkey;monkey.patch_all()
# import socket
# import gevent
# from threading import current_thread
# def talk(conn):
#     print('--->',current_thread())
#     while True:
#         conn.send(b'hello')
#         print(conn.recv(1024))
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# while True:
#     conn,addr = sk.accept()
#     gevent.spawn(talk,conn)
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
#             conn.send(b'hellr')
#             print(conn.recv(1024))
# server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),Myserver)
# server.serve_forever()
import time
import random
# from multiprocessing import Process,Queue
# def consumer(q,name):
#     while True:
#         food = q.get()
#         if food is None:break
#         time.sleep(random.uniform(0.5,1))
#         print('%s吃了%s'%(name,food))
# def producer(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(0.3,0.5))
#         print('%s生产了%s %s'%(name,food,i))
#         q.put(food + str(i))
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=consumer,args=(q,'ake'))
#     c2 = Process(target=consumer,args=(q,'wusr'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=producer,args=(q,'haha','hehe'))
#     p2 = Process(target=producer,args=(q,'xixi','lala'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
# import time
# import random
# from multiprocessing import Process,Queue
# def consumer(q,name):
#     while True:
#         food = q.get()
#         if food is None:break
#         time.sleep(random.uniform(0.5,1))
#         print('%s吃了%s'%(name,food))
# def producer(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(0.3,0.5))
#         print('%s生产了%s %s'%(name,food,i))
#         q.put(food + str(i))
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=consumer,args=(q,'ake'))
#     c2 = Process(target=consumer,args=(q,'wusr'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=producer,args=(q,'haha','hehe'))
#     p2 = Process(target=producer,args=(q,'xixi','lala'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)







