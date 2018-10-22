# 01 昨日内容回顾
# 02 作业讲解
# 03 while循环
# 04 格式化输入
# 05 运算符
# 06 编码初始
# 07 预习博客
# 08 今日作业
# sam = int(input('猜猜这个数字是什么：'))
# # if sam < 66:
# # 	print('结果小了')
# # elif sam > 66:
# # 	print('结果大了')
# # else:
# # 	print('结果正确')
#
# while 循环结构
# while True:                #判断条件，如果条件为真，进入循环体
# 	print('大悲咒')
# 	print('两只老虎')
# 	print('霸王别姬')
# 	print('老司机带带我')   #返回到条件，继续判断条件
#
# while 条件：
# 	循环体
#
# 如何终止循环？
# 1.改变条件（标志位的概念）
# 2.breack
# flag = True
# while flag:
# 	print('大悲咒')
# 	print('两只老虎')
# 	print('霸王别姬')
# 	print('老司机带带我')
# 	flag = False
#
# flag = True
# while flag:
# 	print('大悲咒')
# 	print('两只老虎')
# 	flag = False
# 	print('霸王别姬')
# # 	print('老司机带带我')
# flag = True
# while flag:
# 	print('love story')
# 	flag = False
# 	print('有一个姑娘')
# 练习
# num = 0
# while num < 100:
# 	num += 1
# 	print(num)
# flag = True
# count = 1
# while flag:
# 	print(count)
# 	count = count + 1
# 	if count == 101:
# 		flag = False
# while True:
# 	print(111)
# 	print(222)
# 	break
# 	print(333)
# 	print(444)
# count = 0
# num = 0
# while count < 100:
# 	count += 1
# 	num = count + num
# print(num)
# count = 1
# sum = 0
# while True:
# 	sum = sum + count
# 	count = count + 1
# 	if count == 101:
# 		break
# print(sum)
# continue:结束本次循环，继续下一次循环
# while True:
# 	print(111)
# 	print(222)
# 	continue
# 	print(333)
# while else 结构
# 如果while循环被break打断，则不执行else代码
# count = 1
# while count < 5:
# 	print(count)
# 	count = count + 1
# 	if count == 3 : break
# else:
# 	print(666)
# print(222)
# 应用场景：
# 	验证用户名密码，重新输入这个功能需要while循环
# 无限次的显示页面，无限次的输入
# 格式化输出：
# 	制作一个模板，某些位置的参数是动态的，像这样，就需要用格式化输出
# 字符串的动态替换
# name = input('请输入你的姓名：')
# age = int( input('请输入你的年龄：'))
# sex = input('请输入性别：')
# # %占位符   s 数据类型为字符串   d  数字
# # msg = '你的名字是%s,你的年龄是%s，你的性别是%s' %(name,age,sex)
# # msg = '你的名字是%s,你的年龄是%d,你的性别是%s' % (name,age,sex)
# #如果占位符是数字%d，那么相应位置上需要加上int 例：age = int(input('请输入你的年龄'))
# msg = '你的名字是%(name1)s,你的年龄是%(age1)d,你的性别是%(sex1)s' % {'name1':name,'age1':age,'sex1':sex}
# #运用字典{}时，要注意前面的名称是一个字符串{'name1':name}
# print(msg)
# bug 点 在格式化输出中，只想单纯的表示一个 % 时，应该用 %% 表示
# msg = '我叫%s,年龄%d.我的学习进度现在是1%%' % ('beriuta',23)
# print(msg)
# num = 0
# while num < 10:
# 	num = num + 1
# 	if num == 7:
# 		continue
# 	print(num)
# sam = 0
# while True :
# 	sam = sam + 1
# 	if sam == 101:
# 		break
# 	print(sam)
# flag = True
# sam = 0
# while flag:
# 	sam += 1
# 	if sam == 100:
# 		print(sam)
# 	flag = False
# 应用：
# 1.if while 等条件判断（数据库，Django orm Q查询）
# 运算符
# == 比较的两边的值是否相等
# = 赋值运算
# ！= 不等于
# += count = count + 1   简写 count += 1
# -=
# *= count = count * 5   简写 count *= 5
# /=
# **=
# //=
# 逻辑运算符
# and  or  not
# 优先级：（）> not > and >or
# 第一种情况，前后条件为比较运算
# print(1 > 2 and 3 > 4 or 7 < 9 and 4 > 0 or 3 > 4)
# 第二种情况，前后两边的条件为数值
# 数字只有0为false
# x or y 如果x为真，则返回x的值
# print(1 or 2)
# print(1 and 2)
# 补充
# int <--->bool
# 0对应的bool值为False,非0都是True
# True       1 ,False   0
# print(bool(100))
# print(bool(0))
# print(bool(-1))
# print(int(True))
# print(int(False))
# print(1 or 2)
# print(1 and 2)
# print(5 or 2)
# print(5 and 2)
# print(0 or 2)
# print(0 and 2)
# print(0 or 3 and 5 or 4)
# ASSCII:最初版本的密码本：所有的英文字母，数字，特殊字符
#
# UTF-8：最少用8位表示一个字符
#     A：01000010  一个字节
#     欧洲文字：01000111 01000111   两个字节
#     中：01000111 01000111 0010011   三个字节
#     ’old 男孩‘：9个字节
#
# gbk: 国标，只包含中文，英文（英文字母，数字，特殊字符）
#     A：01000010   一个字节
#     中：01000111 01000111   两个字节
# print(6 or 2 > 1)
# print(0 or 5 < 4)
# print(2 > 1 or 6)
# print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 >2)
# msg = True
# while  True:
#     num = int(input('请输入你心中所猜的数字：'))
#     if num == 66:
#         print('结果正确')
#         break
#     elif num < 66:
#         print('结果小了')
#     else:
#         print('结果大了')
# num = 0
# while num < 3:
#     name = int(input('请猜一下正确数字：'))
#     num += 1
#     if name == 66:
#         print('结果正确')
#         break
#     elif name < 66:
#         print('结果小了')
#     elif name > 66:
#         print('结果大了')
# print('太笨了你....')
# num = 0
# while num < 10:
#     num += 1
#     if num == 7:
#         continue
#     print(num)
# num = 0
# sam = 0
# while num <100:
#     num += 1
#     sam += num
# print(sam)
# num = 0
# sam = 0
# while True:
#     num += 1
#     sam += num
#     if num == 100:
#         break
# print(sam)
# flag = True
# num = 0
# sam = 0
# while flag:
#     num += 1
#     sam += num
#     if num == 100:
#         flag = False
# print(sam)
# num = 0
# sam = 0
# while num < 100:
#     num += 1
#     if num %2 ==1:
#         sam += num
#     else:
#         continue
# # print(sam)
# for i in range(1,101):
#     if i %2 == 1:
#         print(i)
# n = 0
# while n < 100:
#     n += 1
#     if n %2 ==1:
#         print(n)
# n = 0
# while n < 100:
#     n += 1
#     if n %2 ==0 :
#         print(n)
# n = 1
# while n < 101:
#     n += 1
#     temp = n %2
#     if temp ==0:
#         print(n)
# start = 1
# sum = 0
# while start < 100:
#     temp = start % 2
#     if temp == 1:
#         sum = sum + start
#     else:
#         sum = sum - start
#     # print(start)
#     start += 1
# print(sum)
# start = 1
# sum = 0
# while start <100:
#     temp = start % 2
#     if temp ==1:
#         sum = sum + start
#     else:
#         sum = sum - start
#     #print(start)
#     #sum = sum + 1
#     start += 1
# print(sum)
# n = 1
# while True:
#     name = input('请输入用户名：')
#     if name != 'xiaogui':
#         print('用户名输入错误')
#         if n >= 3:
#             print('三次用户名输入错误')
#             break
#         else:
#             n += 1
#             while True:
#                 ass = int(input('请输入密码：'))
#                 if psw != '172839':
#                     print('用户密码错误，请重新输入')
#                     if n >= 3:
#                         print('三次密码输入有误')
#                         break
#                     else:
#                         n += 1
#                 else:
#                     print('登陆成功')
#                     break
#         break
#     print(msg)

print('hello')











