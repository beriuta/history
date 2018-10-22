# import socket
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
# while 1:
#     conn,addr = sk.accept()
#     ret = conn.recv(9000)
#     print(ret)
#     conn.send(b'HTTP/1.1 200 OK\r\ncontent-type:text/html;charset=utf-8\r\n\r\n')
#     with open('s1.text','rb') as f:
#         msg = f.read()
#     conn.send(msg)
#     conn.close()
# import socket
#
#
# sk = socket.socket()
# sk.bind(('127.0.0.1',9000))
# sk.listen()
#
# while 1:
#     conn,addr = sk.accept()
#     ret = conn.recv(9000)
#     print(ret)
#     conn.send(b'HTTP/1.1 200 OK\r\ncontent-type:text/html;charset=utf-8\r\n\r\n')
#     with open('s1.text','rb') as f:
#         msg = f.read()
#     conn.send(msg)
#     conn.close()
# class Course:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
# class Student:
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course = course
# python = Course('python',19800)
# ming = Student('小明',22,python)
# ming2 = Student('小红',23,python)
# python.price = 23453
# print(ming.course.price)  # 23453
# class Foo:
#     count = 0
#     def __init__(self):
#         self.count += 1
# f1 = Foo()
# f2 = Foo()
# print(Foo.count)  # 0
# print(f1.count)  # 1
# print(f2.count)  # 1
# class Foo:
#     count = 0
#     def __init__(self):
#         Foo.count += 1
# f1 = Foo()
# print(f1.count)  # 1
# f2 = Foo()
# print(f2.count)  # 2
# f3 = Foo()
# f4 = Foo()
# f5 = Foo()
# print(f1.count)  # 5
# print(f5.count)  # 5
# print(Foo.count)  # 5
# class Foo:
#     count =[0]
# f1 = Foo()
# print(Foo.count[0])  # 0
# f1.count[0] += 1
# print(f1.count[0])  # 1
# print(Foo.count[0])  # 1
# f1.count = [2]
# print(f1.count)  # [2]
# print(Foo.count)  # [1]
# class Animal:
#     def __init__(self,name,kind,food,language):
#         self.name = name
#         self.kind = kind
#         self.food = food
#         self.language = language
#     def yell(self):
#         print('%s叫'%self.language)
#     def eat(self):
#         print('吃%s'%self.food)
#     def drink(self):
#         print('喝水')
# class Cat(Animal):  # 继承Animal类
#     def catch_mouse(self):  # 抓老鼠，是猫自己独有的功能
#         print('抓老鼠')
# class Dog(Animal):
#     def look_after_house(self):  # 看家，是狗自己独有的功能
#         print('看家')

