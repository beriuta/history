# # def a(func):
# #     def func2():
# #         print('xyh')
# #         func()
# #         print('ycm')
# #
# #     return func2
# #
# #
# # @a
# # def people():
# #     print('永远不要高估自己！')
# #
# #
# # people()
# # def func1():
# #     name = '深圳'
# #
# #     def func():
# #         print(name)  # 内层函数的作用域里没有name,会自动往外层函数的作用域去找
# #
# #     func()
# #
# #
# # func1()
# #
# #
# # def func1():
# #     name = '张三'
# #
# #     def func2(arg):
# #         print(arg)
# #
# #     func2(name)
# #
# #
# # func1()
# #
# #
# # def func(name):
# #     def func2():
# #         print(name)  # 形参相当于函数的 内部变量
# #
# #     func2()
# #
# #
# # func('零食铺子')
# # num = 1000
# #
# #
# # def func_1():
# #     print(num)
# #
# #
# # func1()
# # def func1(name):
# #     def func2():
# #         print(name)
# #     return func2
# # ret = func1('吃的')
# # ret()  # 吃的
# # def func1():
# #     def func2():
# #         def func3():
# #             def func4():
# #                 print('开心笑')
# #             return func4
# #         return func3
# #     return func2
# # ret1 = func1()  # func2
# # ret2 = ret1()  # func3
# # ret3 = ret2()  # func4
# # ret3()  # 开心笑
# # def create_people():
# #     print('我想吃脆皮烤猪')
# create_people()
# def create_people():
#     print('我想吃烤鸭')
# def create_people_duck():
#     print('炸鸡也不错')
#     create_people()
# 既不想直接修改原来的函数，也不想修改函数的调用方式，还要加新功能
# def create_duck():
#     print('这边是脆皮烤鸭')
# def food(func):
#     def food_flavour():
#         print('加上荷叶饼，酱料，黄瓜丝，葱丝')
#         func()
#     return food_flavour
# create_duck = food(create_duck)  # 重新赋值
# create_duck()
# def food(func):
#     def food_flavour():
#         print('荷叶饼，酱料，黄瓜丝，葱丝')
#         func()
#
#     return food_flavour
#
#
# @food  # 相当于被装饰的函数当成参数传给food，然后返回值再赋值给被装饰的函数名
# def create_duck():
#     print('这里是脆皮烤鸭')
#
#
# @food
# def create_pig():
#     print('这里是卤猪蹄')
#
#
# create_duck()
# create_pig()
# def food(func):
#     def food_duck():
#         print('这里是脆皮烤鸭')
#         func()
#         print('这里是酱猪蹄')
#     return food_duck
# @food
# def create_pig():
#     print('这里是脆皮烤猪')
# create_pig()
# """
# 最终输出结果：
# 这里是脆皮烤鸭
# 这里是脆皮烤猪
# 这里是酱猪蹄
# """
# def food(func):
#     def duck():
#         print('这只是只烤鸭')
#         func()  # 函数现在是create_food
#     return duck
# @food
# def create_food():
#     print('这是一只脆皮烤猪')
# create_food()
# """
# 输出结果：
# 这只是只烤鸭
# 这是一只脆皮烤猪
# """
# def food(func):
#     def duck():
#         print('这只是只烤鸭')
#         func()  # 函数现在是create_food
#     return duck
# @food
# def create_food():
#     print('这是一只脆皮烤猪')
# create_food()
# """
# 输出结果：
# 这只是只烤鸭
# 这是一只脆皮烤猪
# """
# 装饰带返回值的函数
# def food(func):
#     def food_duck():
#         print('这是一只脆皮烤鸭')
#         price = func()
#         print(price)
#         return 23
#     return food_duck
# @food
# def create_food():
#     print('这是一只烤猪')
#     return 100
# ret = create_food()
# print(ret)
# """
# 打印结果：
# 这是一只脆皮烤鸭
# 这是一只烤猪
# 100
# 23
# """
# 装饰带参数的函数
# def food(func):
#     def food_duck(*args,**kwargs):
#         print('脆皮猪的价钱和脆皮鸭的价钱')
#         r = func(*args,**kwargs)
#         print(r)
#         print('价格很便宜，欢迎购买')
#         return r
#     return food_duck
# @food
# def my_price(x,y):
#     print('这是明码标价的')
#     return x + y
# ret = my_price(10,23)
# print(ret)
# """
# 脆皮猪的价钱和脆皮鸭的价钱
# 这是明码标价的
# 33
# 价格很便宜，欢迎购买
# 33
# """
# 装饰器本身带参数
# def food_all(arg):  # 这是装饰器所带的参数
#     def food(func):  # 这是传进去的函数
#         def food_food(*args,**kwargs):  # 这是传进去的函数的参数
#             print('欢迎进入{}'.format(arg))
#             func(*args,**kwargs)
#         return food_food
#     return food
# @food_all('烤猪店')
# def food_pig():
#     print('这是一只烤猪')
# @food_all('烤鸭店')
# def food_duck():
#     print('这是一只烤鸭')
# food_pig()
# food_duck()
# """
# 欢迎进入烤猪店
# 这是一只烤猪
# 欢迎进入烤鸭店
# 这是一只烤鸭
# """
# 按照闭包的格式写一个函数
# def food_all(need=None):
#     def food(func):
#         def food_duck():
#             if need:
#                 print('我是一个油锅')
#             func()
#         return food_duck
#     return food
# @food_all('need_oil')
# def create_food():
#     print('我是需要油炸的一只猪')
# @food_all()
# def create_duck():
#     print('我是一只已经炸过了鸭子了')
# create_food()
# create_duck()
# '''
# 我是一个油锅
# 我是需要油炸的一只猪
#
# 我是一只已经炸过了鸭子了
# '''
# 装饰器修复技术
# from functools import wraps
# def food_all(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         print('这是新功能')
#         func(*args,**kwargs)
#     return inner
# @food_all
# def food(arg1, arg2):
#     """
#     这里写函数是做什么的
#     :param arg1: 这个参数是什么类型
#     :param arg2: 这个参数是什么类型
#     :return: None
#     """
#     print('这是一只烤乳猪')
# print(food.__doc__)
# print(food.__name__)
# '''
# 加上@wraps(func)这个模块，打印：
#
#     这里写函数是做什么的
#     :param arg1: 这个参数是什么类型
#     :param arg2: 这个参数是什么类型
#     :return: None
#
# food
# 不加@wraps(func)，打印：
# None
# inner
# 避免日志出现全部都是inner，便于看
# '''
# 多个装饰器装饰同一个函数
# def food(func):
#     print('烤鸭')
#
#     def inner1():
#         print('烤猪1')
#         return "<i>{}</i>".format(func())
#
#     return inner1
#
#
# def food_all(func):
#     print('烤全羊')
#
#     def inner2():
#         print('烤猪2')
#         return '<b>{}</b>'.format(func())
#
#     return inner2
#
#
# @food
# @food_all
# def food_duck():
#     print('这是一只烤鸭')
#     return '炸鸡'
#
#
# ret = food_duck()
# print(ret)
# food_duck = food_all(food_duck)  打印烤全羊 return inner2 此时food_duck = inner2
# food_duck = food(inner2)   打印烤鸭 return inner1  此时food_duck = inner1
# 然后最终调用的food_duck是inner1 打印烤猪1 return <i> func() </i> ,
# 因为此时func()是inner2,所以要到inner2里面去找，此时的inner1函数没有return，所以没有结束，
# 到inner2 中，然后打印inner2，打印 烤猪2 ，返回一个<b> func() </b> ,此时的func是原来的food_duck，
# 所以调用food_duck这个函数，打印‘这是一只炸鸡’，并拿到返回值‘炸鸡’
# 然后回到inner1，此时的func()的值是<b> 炸鸡 </b>，再加上<i> func() </i> = <i> <b> 炸鸡 </b> </i>
