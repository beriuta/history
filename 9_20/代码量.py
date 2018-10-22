# import time
# import random
# from multiprocessing import Process,Queue,JoinableQueue
# def consumer(q,name):
#     while True:
#         food = q.get()
#         # if food is None:break
#         print('%s吃了一个%s'%(name,food))
#         time.sleep(random.uniform(0.3,0.5))
#         q.task_done()
# def procucer(q,name,food):
#     for i  in range(10):
#         time.sleep(random.uniform(0.3,0.8))
#         print('%s生产了%s%s'%(name,food,i))
#         q.put(food+str(i))
# # if __name__ == '__main__':
# #     q = JoinableQueue()
# #     c1 = Process(target=consumer,args=(q,'bebe'))
# #     # c1.daemon = True
# #     c1.start()
# #     p1 = Process(target=procucer,args=(q,'byby','泔水'))
# #     p1.start()
# #     p1.join()
# #     q.put(None)   #有几个consumer就需要放几个None
# if __name__ == '__main__':
#     jq = JoinableQueue()
#     c1 = Process(target=consumer,args=(jq,'alex'))
#     c2 = Process(target=consumer,args=(jq,'wusir'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=procucer,args=(jq,'杨宗河','泔水'))
#     p2 = Process(target=procucer,args=(jq,'何思浩','鱼刺和骨头'))
#     p1.start()
#     p2.start()
# from multiprocessing import Queue
# import queue
# q = Queue(2)        #括号里面可以限制队列放的元素的个数
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# print(q.get())
# print(q.get())
# q.get()
# q.get()
# q.get()
# try:
#     print(q.get_nowait())    #如果get不了就用这个异常处理queue。Empty
# except queue.Empty:
#     print('empty')
# q.put_nowait(3)  #一般情况下不用put_nowait(),因为数据会丢   这是不能放进去就会堵塞  get_nowait()不能取会阻塞
# q.empty():判断当前这个队列是否为空
# print(q.empty())      #True
# q.full():判断是否是满  但是q.empty跟q.full在多进程下不准
# from multiprocessing import Process,Queue
# def cons(q):
#     print('son-->',q.get())
#     q.put('abc')
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=cons,args=(q,))
#     p.start()
#     q.put({'123':123})
#     # p.join()        #如果不用join会只显示  Foo--> {'123': 123}   主进程会直接get主进程的put
#     print('Foo-->',q.get())
# from multiprocessing import Queue
# q = Queue(3)
# q.put(2)
# q.put(3)
# q.put(5)
# # q.put(6)  #当给Queue设置队列长度，而如果队列已满，程序就会停在这里，等待数据被别人取走，再将数据放入队列，而如果队列中的数据一直不被取走，程序就会永远停在这里
# try:
#     q.put_nowait(3)  #可以使用put_mowait(),如果队列满了不会阻塞，但是会因为队列满了而报错
# except:      #因此我们可以用一个try语句来处理这个错误，这样程序不会一直阻塞下去，但是会丢掉这个消息
#     print('队列已经满了')
# print(q.get())
# print(q.get())
# print(q.get())
# import time
# from multiprocessing import  Process,Queue
# def f(q):
#     q.put([time.asctime(),'from Beriuta','hello'])  #调用主函数中p进程参数，put函数为队列中添加一条数据
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f,args=(q,))
#     p.start()
#     print(q.get())
#     p.join()       #['Thu Sep 20 16:23:21 2018', 'from Beriuta', 'hello']
# import os
# import time
# import multiprocessing
# def inputQ(queue):   #向queue中输入数据的函数
#     info = str(os.getpid()) + '(put):' + str(time.asctime())
#     queue.put(info)
# def outputQ(queue):          #向queue中输出数据的函数
#     info = queue.get()
#     print('{}{}{}'.format(str(os.getpid()),'(get):',info))
# if __name__ == '__main__':
#     multiprocessing.freeze_support()
#     recoed1 = []
#     recoed2 = []
#     queue = multiprocessing.Queue(3)
#     for i in range(10):
#         process = multiprocessing.Process(target=inputQ,args=(queue,))
#         process.start()
#         recoed1.append(process)
#     for i in range(10):
#         process = multiprocessing.Process(target=outputQ,args=(queue,))
#         process.start()
#         recoed2.append(process)
#     for p in recoed1:
#         p.join()
#     for p in recoed2:
#         p.join()
# 生产者消费者模型：基于庞大的数据之下使用
# import time
# import random
# from multiprocessing import Process,Queue
# def cons(q,name):
#     while True:
#         food = q.get()
#         if food is None:break
#         time.sleep(random.uniform(0.5,1))
#         print('{}吃了一只{}'.format(name,food))
# def prodon(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(0.3,0.8))
#         print('{}生产了{}只{}'.format(name,i,food))
#         q.put(food+str(i))
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=cons,args=(q,'Ali'))
#     c2 = Process(target=cons,args=(q,'Ali2'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=prodon,args=(q,'Beriuta','猪'))
#     p2 = Process(target=prodon,args=(q,'Beriuta2','鸡'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     q.put(None)      #有几个cons就需要放几个None
#     q.put(None)
# import time
# import random
# from multiprocessing import Process,Queue
# def cins(q,name):
#     while True:
#         food = q.get()
#         if food is None:break
#         time.sleep(random.uniform(0.5,1))
#         print('{}吃了一只{}'.format(name,food))
# def prodon(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(0.3,0.8))
#         print('{}生产了一只{}{}'.format(name,food,i))
#         q.put(food+str(i))
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=cins,args=(q,'Ali'))
#     c2 = Process(target=cins,args=(q,'Ali2'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=prodon,args=(q,'Beriuta','猪'))
#     p2 = Process(target=prodon,args=(q,'Beriuta','鸡'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p1.join()
#     q.put(None)
#     q.put(None)
# import time
# import random
# from multiprocessing import Process,Queue
# def cons(q,name):
#     while True:
#         food = q.get()
#         if food is None:break
#         time.sleep(random.uniform(0.5,1))
#         print('{}吃了一只{}'.format(name,food))
# def person(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(0.3,0.5))
#         print('{}生产了一只{}{}'.format(name,food,i))
#         q.put(food+str(i))
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=cons,args=(q,'Ali'))
#     c2 = Process(target=cons,args=(q,'Ali2'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=person,args=(q,'Beriuta','猪'))
#     p2 = Process(target=person,args=(q,'Beriuta','鸡'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
# import time
# import random
# from multiprocessing import Process,Queue
# def eat(q,name):
#     while True:
#         food = q.get()
#         if food is None:break
#         time.sleep(random.uniform(0.5,1))
#         print('{}吃了一只{}'.format(name,food))
# def cons(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(0.3,0.8))
#         print('{}生产了一只{}{}'.format(name,food,i))
#         q.put(food+str(i))
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=eat,args=(q,'Ali'))
#     c2 = Process(target=eat,args=(q,'QQ'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=cons,args=(q,'Beriuta','猪'))
#     p2 = Process(target=cons,args=(q,'Beriuta','鸡'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.start()
#     q.put(None)
#     q.put(None)
from multiprocessing import JoinableQueue
# import time
# import random
# from multiprocessing import Process,JoinableQueue
# def cons(q,name):
#     while True:
#         food = q.get()
#         time.sleep(random.uniform(0.5,1))
#         print('{}吃了一个{}'.format(name,food))
#         q.task_done()  #通知队列已经有一个数据被处理了
# def producerr(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(1.3,0.8))
#         print('{}生产了{}{}'.format(name,food,i))
# if __name__ == '__main__':
#     jq = JoinableQueue()
#     c1 = Process(target=cons,args=(jq,'Ali'))
#     c2 = Process(target=cons,args=(jq,'Ali2'))
#     c1.daemon = True
#     c2.daemon = True
#     c1.start()
#     c2.start()
#     p1 = Process(target=producerr,args=(jq,'Beriuta','猪'))
#     p2 = Process(target=producerr,args=(jq,'Beriuta','鸡'))
#     p1.start()
#     p2.start()
#     p1.join()        #生产者要先把所有的数据都放到队列中
#     p2.join()
#     jq.join()
# from multiprocessing import Pipe   #管道就是 队列+锁 简便的ICP机制
# left,right = Pipe()
# left.send(12345)
# print(right.recv())
# import time
# import os
# from multiprocessing import Process,Pipe
# def cons(left,right):
#     time.sleep(1)
#     print(right.recv())
# if __name__ == '__main__':
#     left,right = Pipe()
#     Process(target=cons,args=(left,right)).start()
#     left.send(1234)        #但是上述代码cons的left参数并没有用上
# def cons(left,right):
#     left.close()
#     # time.sleep(1)
#     while True:
#         try:
#             print(right.recv())
#         except EOFError:
#             break
# if __name__ == '__main__':
#     left,right = Pipe()
#     Process(target=cons,args=(left,right)).start()
#     right.close()
#     for i in range(10):
#         left.send('糖果{}'.format(i))
#     left.close()
# def cons(left,right):
#     left.close()
#     while True:
#         try:
#             print(right.recv())
#         except EOFError:         #手动关闭所有的端口来触发报错
#             break
# if __name__ == '__main__':
#     left,right = Pipe()
#     Process(target=cons,args=(left,right)).start()
#     right.close()
#     for i in range(10):
#         left.send('糖水{}'.format(i))
#     left.close()       #pipe的端口管理不会随着某一个进程的关闭就关闭   在主进程里关了，在子进程里能用 2.操作系统来管理进程对这些端口的使用
import time
from multiprocessing import Pool,Process
# def func(num):
#     print('做了第{}件衣服'.format(num))
# if __name__ == '__main__':
#     start = time.time()
#     p = Pool(4)             #os.cpu_count()+1  #比CPU多一个就会多分到一个时间片
#     for i in range(100):
#         p.apply_async(func,args=(i,))        #异步提交func到一个子进程中执行
#     p.close()   #关闭进程池，用户不能再向这个池中提交任务
#     p.join()   #阻塞，直到进程池中所有的任务都被执行完
#     print(time.time() - start)
# if __name__ == '__main__':
#     start = time.time()
#     p_lst = []
#     for i in range(100):
#         p = Process(target=func,args=(i,))
#         p.start()
#         p_lst.append(p)
#     for p in p_lst:
#         p.join()
#     print(time.time() - start)
import os
import time
from multiprocessing import Pool
# def task(num):
#     time.sleep(1)
#     print('{}:{}'.format(num,os.getpid()))
#     return num **2
# if __name__ == '__main__':
#     p =Pool()
#     for i in range(20):
#         res = p.apply(task,args=(i,))         #提交任务的方法，同步提交
#         print('-->',res)
# def task(num):
#     time.sleep(1)
#     print('{}:{}'.format(num,os.getpid()))
#     return num**2
# if __name__ == '__main__':
#     p = Pool()
#     for i in range(20):
#         p.apply_async(task,args=(i,))              #提交任务的方法，异步提交
#     p.close()
#     p.join()
# def task(num):
#     time.sleep(1)
#     print('{}:{}'.format(num,os.getpid()))
#     return num**2
# if __name__ == '__main__':
#     p = Pool()
#     res_lst = []
#     for i in range(20):
#         res = p.apply_async(task,args=(i,))          #提交任务的方法，异步提交
#         res_lst.append(res)
#     for res in res_lst:
#         print(res.get())
# def task(num):
#     time.sleep(1)
#     print('{}:{}'.format(num,os.getpid()))
#     return num**2
# if __name__ == '__main__':
#     p = Pool()
#     p.map(task,range(20))       #map  异步提交的简化版本  ，自带close和join方法
# import time
# import random
# from multiprocessing import Process,Queue
# def cons(q,name):
#     while True:
#         food = q.get()
#         if food is None:break
#         time.sleep(random.uniform(0.5,1))
#         print('{}吃了一个{}'.format(name,food))
# def produce(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(0.3,0.5))
#         print('{}生产了一只{}{}'.format(name,food,i))
#         q.put(food + str(i))
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=cons,args=(q,'Ali'))
#     c2 = Process(target=cons,args=(q,'Ali'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=produce,args=(q,'Beriuta','糖水'))
#     p2 = Process(target=produce,args=(q,'Beriuta','辣椒'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
import os
import time
from multiprocessing import  Pool
# def rask(num):
#     time.sleep(1)
#     print('{}:{}'.format(num,os.getpid()))
#     return num**2
# if __name__ == '__main__':
#     p = Pool()
#     for i in range(20):
#         res = p.apply(rask,args=(i,))           #同步提交
#     p.close()
#     p.join()
# def task(num):
#     time.sleep(1)
#     print('{}；:{}'.format(num,os.getpid()))
#     return num**2
# if __name__ == '__main__':
#     p = Pool()
#     for i in range(10):
#         res = p.apply_async(task,args=(i,))        #异步提交 但是没有返回值
#     p.close()
#     p.join()
# def task(num):
#     time.sleep(1)
#     print('{}:{}'.format(num,os.getpid()))
#     return num**2
# if __name__ == '__main__':
#     p = Pool()
#     res_lst = []
#     for i in range(10):
#         res = p.apply_async(task,args=(i,))
#         res_lst.append(res)
#     for res in res_lst:
#         print(res.get())             ##异步提交 但是有返回值
# def task(num):
#     time.sleep(1)
#     print('{}:{}'.format(num,os.getpid()))
#     return num**2
# if __name__ == '__main__':
#     p = Pool()
#     p.map(task,range(20))         #异步提交，自带close和join方法
# import re
# def cal_atom(exp):
#     if '*' in exp:
#         a,b = exp.split('*')
#         return str(float(a) * float(b))
#     if '/' in exp:
#         a,b= exp.split('/')
#         return str(float(a) / float(b))
# def exp_format(exp):
#     exp = exp.replace('--','+')
#     exp = exp.replace('+-','-')
#     exp = exp.replace('++','+')
#     exp = exp.replace('-+','-')
# def inner_bracket(s):
#     while True:
#         parttern = r'\d+(\.\d+)?[*/]-?\d+(\.\d+)?'
#         ret = re.search(parttern,s)
#         if ret:
#             exp = ret.group()
#             res = cal_atom(exp)
#             s = s.replace(exp,res)
#         else:break
#     s = exp_format(s)
#     ret = re.findall('[-+]?\d+(?:\.\d+)?', s)
#     count = 0
#     for i in ret:
#         count += float(i)
#     return count
# def remove_bracket(s):
#     while True:
#         ret = re.search('\([^()]+\)',s)
#         if ret:
#             no_bracket = ret.group()
#             res = inner_bracket(no_bracket)
#             s = s.replace(no_bracket,str(res))
#             s = exp_format(s)
#         else:return s
# def main(s):
#     s = s.replace(' ','')
#     s = remove_bracket(s)
#     return inner_bracket(s)
# s = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# ret = main(s)
# print(ret)
# import time
# import random
# from multiprocessing import Process,Queue
# def cons(q,name):
#     while True:
#         food = q.get()
#         if food is None:break
#         time.sleep(random.uniform(0.5,1))
#         print('{}吃了一个{}'.format(name,food))
# def producer(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(0.3,0.5))
#         print('{}生产了{}{}'.format(name,food,i))
#         q.put(food+str(i))
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=cons,args= (q,'Ali'))
#     c2 = Process(target=cons,args=(q,'Ali'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=producer,args=(q,'Beriuta','鱼头'))
#     p2 = Process(target=producer,args=(q,'Beriuta','芋头'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
# import time
# import random
# from multiprocessing import Process,Queue
# def cons(q,name):
#     while True:
#         food = q.get()
#         if food is None:break
#         time.sleep(random.uniform(0.5,1))
#         print('{}吃了一个{}'.format(name,food))
# def producer(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(0.3,0.8))
#         print('{}生产了一个{}{}'.format(name,food,i))
#         q.put(food+str(i))
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=cons,args=(q,'Ali'))
#     c2 = Process(target=cons,args=(q,'Ali'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=producer,args=(q,'Beriuta','鱼头'))
#     p2 = Process(target=producer,args = (q,'Beriuta','yutou'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
# import time
# import random
# from multiprocessing import Process,Queue
# def cons(q,name):
#     while True:
#         food = q.get()
#         if food is None:break
#         time.sleep(random.uniform(0.5,1))
#         print('{}吃了一只{}'.format(name,food))
# def peodure(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(0.3,0.5))
#         print('{}生产了一只{}{}'.format(name,food,i))
#         q.put(food+str(i))
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=cons,args=(q,'Ali'))
#     c2 = Process(target=cons,args=(q,'Ali'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=peodure,args=(q,'Beriuta','鱼头'))
#     p2 = Process(target=peodure,args=(q,'Beriuta','与头'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
# import time
# import random
# from multiprocessing import Process,Queue
# def cons(q,name):
#     while True:
#         food = q.get()
#         if food is None:break
#         time.sleep(random.uniform(0.5,1))
#         print('{}吃了一个{}'.format(name,food))
# def produce(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(0.3,0.8))
#         print('{}生产了一只{}{}'.format(name,food,i))
#         q.put(food+str(i))
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=cons,args=(q,'Ali'))
#     c2 = Process(target=cons,args=(q,'ali1'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=produce,args=(q,'Beruta','鱼头'))
#     p2 = Process(target=produce,args=(q,'Beruta','玉兔'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
# import time
# import random
# from multiprocessing import Process,Queue
# def cons(q,name):
#     while True:
#         food = q.get()
#         if food is None:break
#         time.sleep(random.uniform(0.5,1))
#         print('{}吃了一只{}'.format(name,food))
# def producer(q,name,food):
#     for i in range(10):
#         time.sleep(random.uniform(0.3,0.8))
#         print('{}生产了一只{}{}'.format(name,food,i))
#         q.put(food+str(i))
# if __name__ == '__main__':
#     q = Queue()
#     c1 = Process(target=cons,args=(q,'Ali'))
#     c2 = Process(target=cons,args=(q,'Ali2'))
#     c1.start()
#     c2.start()
#     p1 = Process(target=producer,args=(q,'Beriuta','鱼头'))
#     p2 = Process(target=producer,args=(q,'Beriuta','yuyu'))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
# from socket import *
# from multiprocessing import Pool
# import os
# sk = socket(AF_INET,SOCK_STREAM)
# sk.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
# sk.bind(('192.168.16.108',9001))
# sk.listen(5)
# def tail(conn):
#     print('进程pid:{}'.format(os.getpid()))
#     while True:
#         try:
#             msg = conn.recv(1024)
#             if not msg:break
#             conn.send(msg.upper())
#         except Exception:
#             break
# if __name__ == '__main__':
#     p = Pool()
#     while True:
#         conn,_ = sk.accept()
#         p.apply_async(tail,args=(conn,))
# from socket import *
# client = socket(AF_INET,SOCK_STREAM)
# client.connect(('192.168.16.108',9001))
# while True:
#     msg = input('>>>')
#     if not msg:continue
#     client.send(msg.encode('utf-8'))
#     msg = client.recv(1024)
#     print(msg.decode('utf-8'))













