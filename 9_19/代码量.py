# from multiprocessing import Process
# import os
# import time
# import random
# def func(index):
#     time.sleep(random.random())
#     print('第%s个邮件已经发送完毕'%index)
# if __name__ == '__main__':
#     p_lst=[]
#     for i in range(10):
#         p = Process(target=func,args=(i,))
#         p.start()
#         p_lst.append(p)
#     for p in p_lst:
#         p.join()
#     print('10个邮件已经发送完毕')
# class MyProcess(Process):
#     def __init__(self,arg):
#         super().__init__()
#         self.arg = arg
#     def run(self):
#         print('子进程：',os.getpid(),os.getppid(),self.arg)
# if __name__ == '__main__':
#     for i in range(10):
#         p = MyProcess(i)
#         p.start()
#     print('主进程',os.getpid())
# def func():
#     while True:
#         time.sleep(5*60)
#         print('我还活着')
# def main():
#     print('主程序一直提供服务')
# import time
# import json
# from multiprocessing import Process,Lock,Event
# def search(person):
#     with open('ticket') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     print('%s查询余票：'%person,dic['count'])
# def get_ticket(person):
#     with open('ticket') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     if dic['count'] > 0:
#         print('%s买到票了'%person)
#         dic['count'] -= 1
#         time.sleep(0.2)
#         with open('ticket','w') as f:
#             json.dump(dic,f)
#     else:
#         print('%s没买到票'%person)
# def ticket(person,lock):
#     search(person)
#     lock.acquire()
#     get_ticket(person)
#     lock.release()
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10):
#         p = Process(target=ticket,args=('person%s'%i,lock))
#         p.start()
# def traffic_light(e):
#     # flag = False
#     while True:
#         if e.is_set():
#             print('\033[32m绿灯亮\033[0m')
#             time.sleep(2)
#             flag = False
#         else:
#             print('\033[32m红灯亮\033[0m')
#             flag = True
# def car():
#     for i in range(20):
#         e.wait()
#         print('car%s通过了'%i)
# if __name__ == '__main__':
#     e = Event()
#     p = Process(target=traffic_light)
#     p.start()
#     p = Process(target=car,e)
#     p.start()
# import time
# from multiprocessing import Process
# def f(name):
#     print('hello',name)
#     print('我是子进程')
# if __name__ == '__main__':
#     p = Process(target=f,args=('bob',))
#     p.start()
#     # time.sleep(1)
#     print('执行主进程了呀！')
# #hello bob       #我是子进程    #执行主进程了呀！
# import time
# from multiprocessing import Process
# def b(name):
#     print('hello',name)
#     time.sleep(1)
#     print('我是子进程')
# if __name__ == '__main__':
#     p = Process(target=b,args=('bob',))
#     p.start()
#     p.join()
#     print('主进程执行啦！')
# import os
# import time
# import random
# from multiprocessing import Process
# def func(index):
#     time.sleep(random.randint(1,3))
#     print('邮件已经发完毕')
# if __name__ == '__main__':
#     p = Process(target=func,args=(1,))
#     p.start()
#     p.join()  #阻塞，直到p进程执行完毕就结束阻塞
#     print('10个邮件已经发送完毕')
# def func(index):
#     time.sleep(random.random())
#     print('第%s个邮件已经发送完毕'%index)
# if __name__ == '__main__':
#     p_lst = []
#     for i in range(10):
#         p = Process(target=func,args=(i,))
#         p.start()
#         p_lst.append(p)
#     for p in p_lst:
#         p.join()          # 阻塞 直到p进程执行完毕就结束阻塞
#     print('10个邮件全部发送完毕')
# def func(index):
#     time.sleep(random.random())
#     print('第%s个邮件已经发送完毕'%index)
#
# if __name__ == '__main__':
#     p_lst = []
#     for i in range(10):
#         p = Process(target=func,args=(i,))
#         p.start()
#         p_lst.append(p)
#     for p in p_lst:
#         p.join()
#     print('10个邮件已经发送完毕')
# import time
# from multiprocessing import Process
# def f(name):
#     print('hello',name)
#     time.sleep(1)
# if __name__ == '__main__':
#     p_lst = []
#     for i in range(5):
#         p = Process(target=f,args=('bpb',))
#         p.start()
#         p_lst.append(p)
# import time
# from multiprocessing import Process
# def f(name):
#     print('hello',name)
#     # time.sleep(1)
# if __name__ == '__main__':
#     p_lst = []
#     for i in range(5):
#         p = Process(target=f,args=(i,))
#         p.start()
#         p_lst.append(p)
#         p.join()
#         # [p.join() for p in p_lst]
#     print('父进程在执行')
# import os
# from multiprocessing import Process
# class MyProcess(Process):
#     def run(self):       #必须要写这个方法名
#         print('子进程：',os.getpid(),os.getppid())
# if __name__ == '__main__':
#     p =MyProcess()
#     p.start()        #开启一个子进程，让这个子进程执行run方法
# #     print('主进程：',os.getpid())
# import time
# import os
# from multiprocessing import Process
# class MyProcess(Process):
#     def __init__(self,args):
#         super().__init__()        #把Process里面的__init__方法复制过来
#         self.args = args
#     def run(self):
#         time.sleep(1)
#         print('子进程：',os.getpid(),os.getppid(),self.args)
# if __name__ == '__main__':
#     # p = MyProcess('参数')
#     # p.start()
#     # p.join()
#     # print('主进程:',os.getpid())
#     for i in range(10):
#         p = MyProcess('参数%s'%i)
#         p.start()
#     print('主进程',os.getpid())
# import time
# from multiprocessing import Process
# def func():
#     print('子进程 start')
#     time.sleep(3)
#     print('子进程 end')
# if __name__ == '__main__':
#     p = Process(target=func)
#     p.daemon = True
#     p.start()
#     time.sleep(2)
#     print('主进程')           #守护进程会随着主进程的代码执行完毕而结束
# import time
# from multiprocessing import Process
# def func():
#     count = 1
#     while True:
#         print(count * '*')
#         time.sleep(0.5)
#         count += 1
# def ffn():
#     print('ffn start')
#     time.sleep(5)
#     print('ffn end')
# if __name__ == '__main__':
#     p1 = Process(target=func)
#     p1.daemon = True        #守护进程  主进程的代码执行完毕时，但是子进程还没有执行完，视乎进程也不会 继续执行，是代码结束，而不是程序结束
#     p1.start()
#     Process(target=ffn).start()         #程序是执行五秒以上  主进程要等待子进程执行完毕之后才会结束
#     time.sleep(3)
#     print('主进程')
# def func():
#     while True:
#         time.sleep(5*60)          #每隔五分钟就向一台机器汇报自己的状态
#         print('我还活着')
# def main():
#     print('主进程会7*24个小时的提供服务')       #守护进程的功能就是程序的报活，
# import time
# import json
# from multiprocessing import Process,Lock         #降低了程序的效率，让原来能够同时执行的代码变成顺序执行，异步变同步的过程，但是保证了数据的安全
# def search(person):       #查票
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     print('%s查询余票:'%person,dic['count'])
# def get_ticket(person):       #买票
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     if dic['count'] > 0:
#         print('%s买票成功'%person)
#         dic['count'] -= 1
#         time.sleep(0.2)
#         with open('tick','w') as f:
#             json.dump(dic,f)
#     else:
#         print('%s买票失败'%person)
# def tick(person,lock):
#     search(person)
#     lock.acquire()  #上了锁，给一把钥匙
#     get_ticket(person)             #买票
#     lock.release()   #还钥匙给下一个人
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(20):
#         p = Process(target=tick,args=('person%s'%i,lock))
#         p.start()
        # p.join()   #用join也可以，但是会让所有人都按照顺序先去看，都会消耗0.2秒去查，再去买
import time
from multiprocessing import Process,Lock
# def func(num,lock):
#     time.sleep(1)
#     print('异步执行',num)
#     lock.acquire()
#     time.sleep(0.5)
#     print('同步执行',num)
#     lock.release()
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10):
#         p = Process(target=func,args=(i,lock))
#         p.start()   #一个acquire对应一个release，如果多一个acquuire,将会变成死锁,如果多一个release，会报错
# lock = Lock()
# lock.acquire()
# print('12345')
# lock.release()
# print('2345')
# lock.release()
# print('sksdj')
# import time
# import random
# from multiprocessing import Process,Semaphore
# def ktv(person,sem):
#     sem.acquire()
#     print('%s走进KTV'%person)
#     time.sleep(random.randint(1,5))
#     print('%s走出了KTV'%person)
#     sem.release()
# if __name__ == '__main__':
#     sem = Semaphore(4)
#     for i in range(10):
#         p = Process(target=ktv,args=('person%s'%i,sem))
#         p.start()
# import time
# import random
# from multiprocessing import Process,Event
# def traffic(e):
#     print('\033[031m红灯亮\033[0m')
#     while True:
#         if e.is_set():        #判断当前属性是否为True
#             time.sleep(2)
#             print('\033[31m红灯亮\033[0m')
#             e.clear()     #将属性的值改为False
#         else:
#             time.sleep(2)
#             print('\033[32m绿灯亮\033[0m')
#             e.set()  #将这个属性的值改为True
# def car(e,i):
#     if not e.is_set():
#         print('car %s 在等待'%i)
#         e.wait()
#     print('car %s 通过了'%i)
# if __name__ == '__main__':
#     e = Event()
#     p = Process(target=traffic,args=(e,))
#     p.start()
#     for i in range(20):
#         time.sleep(random.randrange(0,3,2))
#         p = Process(target=car,args=(e,i))
#         p.start()        #这个程序一直在运行，当车走完了，也会一直打印红灯跟绿灯
# import time
# import random
# from multiprocessing import Process,Event
# def traffic(e):
#     print('红灯亮')
#     while True:
#         if e.is_set():
#             time.sleep(2)
#             print('红灯亮')
#             e.clear()
#         else:
#             time.sleep(2)
#             print('绿灯亮')
#             e.set()
# def car(e,i):
#     if not e.is_set():
#         print('car %s 在等待'%i)
#         e.wait()
#     print('car %s 出发了'%i)
# if __name__ == '__main__':
#     e = Event()
#     p = Process(target=traffic,args=(e,))
#     p.daemon = True       #守护进程
#     p.start()
#     p_lst = []
#     for i in range(20):
#         time.sleep(random.randrange(0,3,2))
#         p = Process(target=car,args=(e,i))
#         p.start()
#         p_lst.append(p)
#     for i in p_lst:p.join()   #阻塞
# import time
# import json
# from multiprocessing import Process,Lock
# def search(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     print('%s查询余票：'%person,dic['count'])
# def get_tick(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     if dic['count'] > 0:
#         print('%s买票成功'%person)
#         dic['count'] -= 1
#         time.sleep(0.2)
#         with open('tick', 'w') as f:
#             json.dump(dic,f)
#     else:
#         print('%s买票失败'%person)
# def tick(person,lock):
#     search(person)
#     lock.acquire()
#     get_tick(person)
#     lock.release()
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(20):
#         p = Process(target=tick,args=('person%s'%i,lock))
#         p.start()
# import time
# import json
# from multiprocessing import Process,Lock
# def search(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     print('%s查询余票：'%person,'剩余%s'%dic['count'])
# def get_tick(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     if dic['count'] > 0:
#        print('%s买到票了'%person)
#        dic['count'] -= 1
#        with open('tick','w') as f:
#            json.dump(dic,f)
#     else:
#         print('%s抢票失败'%person)
# def tick(person,lock):
#     search(person)
#     lock.acquire()
#     get_tick(person)
#     lock.release()
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(20):
#         p = Process(target=tick,args=('person%s'%i,lock))
#         p.start()
# import time
# import json
# from multiprocessing import Process,Lock
# def search(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     print('%s查看余票张'%person,dic['count'])
# def get_tick(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     if dic['count'] > 0:
#         print('%s买票成功'%person)
#         dic['count'] -= 1
#         time.sleep(0.2)
#         with open('tick','w') as f:
#             json.dump(dic,f)
#     else:
#         print('%s抢票失败'%person)
# def tick(person,lock):
#     search(person)
#     lock.acquire()
#     get_tick(person)
#     lock.release()
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(20):
#         p = Process(target=tick,args=('person%s'%i,lock))
#         p.start()
# import time
# import json
# from multiprocessing import Process,Lock
# def seach(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     print('%s查看余票：'%person,dic['count'])
# def get_tick(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     if dic['count'] > 0:
#         print('%s购票成功'%person)
#         dic['count'] -= 1
#         time.sleep(0.2)
#         with open('tick','w') as f:
#             json.dump(dic,f)
#     else:
#         print('%s购票失败'%person)
# def tick(person,lock):
#     seach(person)
#     lock.acquire()
#     get_tick(person)
#     lock.release()
# if __name__ == '__main__':
#     lock =Lock()
#     for i in range(20):
#         p = Process(target=tick,args=('person%s'%i,lock))
#         p.start()
# import json
# import time
# from multiprocessing import Process,Lock
# def seach(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     print('%s查看余票:'%person,dic['count'])
# def get_tick(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     if dic['count'] > 0:
#         print('%s购票成功'%person)
#         dic['count'] -= 1
#         with open('tick','w') as f:
#             json.dump(dic,f)
#     else:
#         print('%s购票失败'%person)
# def tick(person,lock):
#     seach(person)
#     lock.acquire()
#     get_tick(person)
#     lock.release()
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(20):
#         p = Process(target=tick,args=('person%s'%i,lock))
#         p.start()
# import time
# import random
# from multiprocessing import Process,Event
# def light(e):
#     print('红灯亮')
#     while True:
#         if e.is_set():
#             time.sleep(2)
#             print('红灯亮')
#             e.clear()
#         else:
#             time.sleep(2)
#             print('绿灯亮')
#             e.set()
# def car(e,i):
#     if not e.is_set():
#         print('car %s 在等待'% i)
#         e.wait()
#     print('car %s 通过了'%i)
# if __name__ == '__main__':
#     e = Event()
#     p = Process(target=light,args=(e,))
#     p.start()
#     for i in range(5):
#         time.sleep(random.randrange(0,3,2))
#         p = Process(target=car,args=(e,i))
#         p.start()
# import time
# import random
# from multiprocessing import Process,Event
# def light(e):
#     print('红灯亮')
#     while True:
#         if e.is_set():
#             time.sleep(2)
#             print('红灯亮')
#             e.clear()
#         else:
#             time.sleep(2)
#             print('绿灯亮')
#             e.set()
# def car(e,i):
#     if not e.is_set():
#         print('car %s 在等待' % i)
#         e.wait()
#     print('car %s 通过了'%i)
# if __name__ == '__main__':
#     e = Event()
#     p = Process(target=light,args=(e,))
#     p.daemon = True
#     p.start()
#     p_lst = []
#     for i in range(10):
#         time.sleep(random.randrange(0,3,2))
#         p = Process(target=car,args=(e,i))
#         p.start()
#         p_lst.append(p)
#         for p in p_lst:p.join()
# import time
# import random
# from multiprocessing import Process,Event
# def light(e):
#     print('红灯亮')
#     while True:
#         if e.is_set():
#             time.sleep(2)
#             print('红灯亮')
#             e.clear()
#         else:
#             time.sleep(2)
#             print('绿灯亮')
#             e.set()
# def car(e,i):
#     if not e.is_set():
#         print('car %s 在等待'%i)
#         e.wait()
#     print('car %s 通过了'%i)
# if __name__ == '__main__':
#     e = Event()
#     p = Process(target=light,args=(e,))
#     p.daemon = True
#     p.start()
#     p_lst = []
#     for i in range(10):
#         time.sleep(random.randrange(0,3,2))
#         p = Process(target=car,args=(e,i))
#         p.start()
#         p_lst.append(p)
#     for p in p_lst:p.join()
# import time
# import random
# from multiprocessing import Process,Event
# def light(e):
#     print('红灯亮')
#     if e.is_set():
#         time.sleep(2)
#         print('红灯亮')
#         e.clear()
#     else:
#         time.sleep(2)
#         print('绿灯亮')
#         e.set()
# def car(e,i):
#     if not e.is_set():
#         print('car %s 等待中'%i)
#         e.wait()
#     print('car %s 通过了'%i)
# if __name__ == '__main__':
#     e = Event()
#     p = Process(target=light,args=(e,))
#     p.daemon = True
#     p.start()
#     p_lst = []
#     for i in range(10):
#         time.sleep(random.randrange(0,3,2))
#         p = Process(target=car,args=(e,i))
#         p.start()
#         p_lst.append(p)
#     for p in p_lst:p.join()
# import time
# import json
# from multiprocessing import Process,Lock
# def seach(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     print('%s查看余票:'%person,dic['count'])
# def get_tick(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time .sleep(0.2)
#     if dic['count'] > 0:
#         print('%s购票成功'%person)
#         with open('tick','w') as f:
#             json.dump(dic,f)
#     else:
#         print('%s购票失败'%person)
# def tick(person,lock):
#     seach(person)
#     lock.acquire()
#     get_tick(person)
#     lock.release()
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10):
#         p = Process(target=tick,args=('person%s'%i,lock))
#         p.start()
# import socket
# sk = socket.socket()
# sk.connect(('192.168.16.108',9001))
# while True:
#     print(sk.recv(1024))
#     sk.send(b'bye')           #一直循环
# import socket
#    sk = socket.socket()
#         sk.bind(('192.168.16.108',9001))
#         sk.listen()
#         while True:
#             conn,addr = sk.accept()
#             Process(target=communicate,args=(conn,)).start()from multiprocessing import Process
# def communicate(conn):
#     while True:
#         conn.send(b'hello')
#         print(conn.recv(1024))
# if __name__ == '__main__':
#         sk = socket.socket()
#         sk.bind(('192.168.16.108',9001))
#         sk.listen()
#         while True:
#             conn,addr = sk.accept()
#             Process(target=communicate,args=(conn,)).start()
# import time
# import json
# from multiprocessing import Process,Lock
# def seach(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     print('%s查询余票:'%person,dic['count'])
# def get_tick(person):
#     with open('tick') as f:
#         dic = json.load(f)
#     time.sleep(0.2)
#     if dic['count'] > 0:
#         print('%s购票成功'%person)
#         dic['count'] -= 1
#         with open('tick','w') as f:
#             json.dump(dic,f)
#     else:
#         print('%s购票失败'%person)
# def tick(person,lock):
#     seach(person)
#     lock.acquire()
#     get_tick(person)
#     lock.release()
# if __name__ == '__main__':
#     lock =Lock()
#     for i in range(10):
#         p = Process(target=tick,args=('person%s'%i,lock))
#         p.start()













































































































