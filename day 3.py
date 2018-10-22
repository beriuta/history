# nam = 'Beriuta'
# pw = '23333'
# count =3
# while True:
#     count -= 1
#     if count < 0:
#         break
#     input_nam = input('请输入用户名：')
#     input_pw = input('请输入密码：')
#     if input_nam == nam and input_pw == pw:
#             print('登陆成功')
#             break
#     else:
#         print('输入错误，请重新输入，还有%d次机会' % count)
# print(1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# print(not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6)
# print(8 or 3 and 4 or 2 and 0 or 9 and 7)
# print(0 or 2 and 3 and 4 or 6 and 0 or 3)
# print(6 or 2 > 1)
# print(3 or 2 > 1)
# print(0 or 5 < 4)
# print(5 < 4 or 3)
# print(2 > 1 or 6)
# print(3 and 2 > 1)
# print(0 and 3 > 1)
# print(2 > 1 and 3)
# print(3 > 1 and 0)
# print(3 > 1 and 2 or 2 < 3 and 4 or 3 > 2)
# -------info of Beriuta -------
# Name    :   Beriuta
# Age     :   23
# job     :   student
# Hobbie  :   girl
# -------end-------
# name = input('Name:')
# age = input('Age:')
# job = input('job:')
# hobbie = input('Hobbie:')
# info = '''
# Name   : %s
# Age    : %s
# job    : %s
# Hobbie : %s
# ''' % (name , age , job , hobbie)  #z这行的%号就是把前面的字符串与括号后面的变量关联起来'''
# print(info)
# -------info of CLASS-------
# name    :   Beriuta
# hobbie  :   girl
# CLASS   :   s1py
# 学习进度  ： 1 %
# input_name = input('Name:')
# input_age = input('Age:')
# input_class = input('CLASS:')
# input_process = input('学习进度:')
# info = '''
# Name : %s
# Age  : %s
# class : %s
# 学习进度：%s %%''' % (input_name , input_age , input_class , input_process)
# print(info)
# s1 = 72
# s2 = 85
# r = s2 / s1
# print('%d %%' % r)
# '{0} love {1}'.format('I', 'you')
# q = True
# while q:
#     num = input('请输入一个整数（输入q结束程序）：')
#     if num != 'q':
#         num = int(num)
#         print('十进制-> 十六进制：%d -> 0x%x' % (num,num))
#     else:
#          q = False
# a = 'sjdkeleeckvvjvjjsllls'
# print('j' in a)
# v = 11
# data = v.bit_length()
# print(data)
# a = 'whsiejelcocod'
# print(a[0])
# print(a[5])
# print(a[9])
# print(a[4])
# a = '1234567890'
# print(a[0:3])
# print(a[2:5])
# print(a[0:])    #默认到最后
# print(a[0:-1])  #-1就是最后一个
# print(a[0:8:3]) #加步长
# print(a[5:0:-2])#反向加步长
# len('abc')
# msg = 'egon say hi'
# print(msg.title())
# name = 'beriuta'
# print(name.upper())
# x = 'hello word ASDF'
# print(x.lower())
# n = '112222373h39494fljks'
# print(n.islower())
# m = '12838383883'
# print(m.islower())
# a1 = '23k'
# ret2 = a1.center(20 , "*")
# print(ret2)
# name = 'BERIUTA'
# print(name.swapcase())
# name ='aBSKKEEaa'
# # print(name.capitalize())
# a2 = 'hqwqreffdgthg\t'
# ret4 = a2.expandtabs()
# print(ret4)
# a4 = 'sdjeenkdukd809'
# ret4= a4.endswith('sje' , 3 , 8)
# print(ret4)
# b4 = 'wksn9234cckkkkkd'
# ret2 = b4.startswith('wks', 0, 4)
# print(ret2)
# b = 'whsjkjhrh'
# tex2 = b.find('sjk', 4 , 6)
# print(tex2)
# tex3 = b.index('kihr', 3 , 8)
# print(tex3)
# ret4 = 'title,Title,atre' .split('t')
# print(ret4)
# ter = 'title,Title,atre' .rsplit('t',2)
# print(ter)
# res = '{} {} {}'.format('egon',18,'male')
# res = '{0} {1} {2}'.format('egon',18,'male')
# print(res)
# res = '{name} {age} {sex}'.format(name='egon',age=22,sex='male')
# print(res)
# name = '*egon**'
# print(name.strip('*'))
# print(name.lstrip('*'))
# print(name.rstrip('*'))
# name ='alex say :my name is alex'
# print(name.replace('alex','SB',)2)
# name ='hanlei123'
# print(name.isalnum())
# print(name.isalpha())
# print(name.isdigit())
# li = [1,333,455,'晕菜','mac','a']
# li.insert(3,50)
# print(li)
# li.append('qqq')
# print(li)
# li.append([1,2,3])
# print(li)
# li.extend(['q,a,w'])
# print(li)
# li.extend(['q,a,w','aaa'])
# print(li)
# li.extend('abc')
# print(li)
# l1=li.pop(1)
# print(l1)
# del li[1:3]
# print(li)
# li.remove('a')
# print(li)
# li.clear()
# print(li)
# li = [1,'a','b',2,3,'a']
# li[1] = 'dfasdfas'
# print(li)
# li[1:3] = ['b','c']
# print(li)
# a =['q','w','q','r','t','y']
# print(a.index('y'))
# print(a.count('y'))
# a =[2,1,3,4,5,]
# a.sort()
# print(a)
# a.reverse()
# print(a)
# dict ={'a':1,'b':2,'b':'3'}
# dict['b']
# dict
# {'a':1,'b':'3'}
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
# print("dict['Name']: ", dict['Name'])
# print("dict['Age']: ", dict['Age'])
# dic['li'] = ["a","b","c"]
# print(dic)
# dic={'2':'f','d':'gd','g':'6'}
# dic_pop1={'4':'6','6':'d','u':'7'}
# dic_num = {'h':'3','wl':'x','f':'2'}
# dic['li'] = ["a","b","c"]
# print(dic)
# dic.setdefault('k','v')
# print(dic)
# dic.setdefault('k','v1')
# print(dic)
# dic_num = dic.popitem()
# print(dic)
# print(dic_num)
# dic_clear = dic.clear()
# print(dic_clear)
# dic = {'name':'jin','age':18,'sex':'male'}
# dic2 ={'name':'niu','weight':75}
# dic2.update(dic)
# print(dic2)
# item = dic.items()
# print(item,type(item))
# name = "牛牛"
# pw = "23333"
# count = 3
# while True:
#     input_name = input('请输入用户名：')
#     input_pw = input('请输入密码：')
#     count -= 1
#     if count < 1:
#         print('三次机会用尽，今日无法登录')
#         break
##     elif input_name == '\r' or input_pw == '\r':
##         count += 1
#     elif input_name == name and input_pw == pw:
#         print('登陆成功')
#         break
#     else:
#         print('输入有误，请重新输入，还有%d次机会' % count)
# name = "牛牛"
# pw = "23333"
# count = 3
# while True:
#     input_name = input('请输入用户名：')
#     input_pw = input('请输入密码：')
#     count -= 1
#     if count < 1:
#         print('三次机会用尽，今日无法登录')
#         break
#     elif input_name == name and input_pw == pw:
#         print('登陆成功')
#         break
#     else:
#         print('输入有误，请重新输入，还有%d次机会' % count)
# count = 0
# num = 0
# while True:
#     num += 1
#     count += 1
#     msg = '%d * %d' % (count,num)
#     print(msg)
#     if count == 9 and num == 9:
#         break
# i=0
# j=0
# while i < 9:
#     i += 1
#     while j < 9:
#         j += 1
#     # print('%d * %d =%d' % (i,j,i*j,))
#     print(j,"x",i,"=",i*j,"\t",end="")
#     if i == j:
#         j = 0
#         print("")
#         break
# i=0
# j=0
# while i < 9:
#     i += 1
#     while j < 9:
#         j += 1
#         print('%d * %d =%d' % (i,j,i*j,))
#     if i == j:
#         j = 0
#         break