# 1、以下代码的输出是什么？请给出答案并解释。
# def multipliers():
#     return [lambda x:i*x for i in range(4)]
# print([m(2) for m in multipliers()])
# 请修改multipliers的定义来产生期望的结果。
#
# 2、程序从flag a执行到falg b的时间大致是多少秒？
# import threading
# import time
# def _wait():
# 	time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait,daemon = False)
# t.start()
# # flag b
# 3、程序从flag a执行到falg b的时间大致是多少秒？
# import threading
# import time
# def _wait():
# 	time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait,daemon = True)
# t.start()
# # flag b
# 4、程序从flag a执行到falg b的时间大致是多少秒？
# import threading
# import time
# def _wait():
# 	time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait,daemon = True)
# t.start()
# t.join()
# # flag b
# 5、简述 进程、线程、协程的区别 以及应用场景？
def mul():
    return [lambda x:i*x for i in range(4)]  #[lambda x:i*x,lambda x:i*x,lambda x:i*x,lambda x:i*x]  i = 3,for循环里面最后的i是多少，这个表达式里的i就是多少
print(m(2) for m in mul())