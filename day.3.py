# count = 1
# while count < 4:
#     prinit(count)
#     count += 1
#     break
# else:
#     print(666)
# print(1 > 2 and 3 < 4 or 5 > 7)
# count = 1
# while count < 11:
#
#     if count == 7:
#         count += 1
#     else:
#         print(count)
#     count += 1
# count = 1
# while count < 11:
#
#     if count == 7:
#         count += 1
#     print(count)
#     count += 1
# count = 0
# while count < 3:
#     username = input('请输入用户名：')
#     pasworld = input('请输入密码：')
#     count += 1
#     if username == 'Beriuta' and pasworld == '1234':
#         print('登陆成功')
#         break
#     else:
#         print('登录失败,您还剩%s次机会' % (3-count))
# i = 4
# print(i.bit_length())   #查询十进制转化成二进制占用的最小位置
# bool
# 数据类型之间的转化
# 数字与字符串之间的转化     int---> str   str(int)    int(str)
# int ----> bool   非零及True,零即为Flase
# bool ---> str    print(bool('beir'))  空字符串对应的bool值是Flaser   s1 = ''  非空即True
# str ---> bool 无意义
# name = input('<<<')
# if name :
#     print(333)
# else:
#     print('无内容')
# 对字符串的下面这两部分操作：形成的都是一个新的字符串，与原来的字符串没有关系
# # 第一部分：索引切片步长
# 按照索引取值，取出来的都是一个字符，形成的字符串
# s1 = 'python1期骑士计划'
# s2 = s1[2]
# print(s2,type(s2))
# s5 = s1[0:6]    # 按切片取值，顾首不顾尾
# s51 = s1[:6]
# print(s5,s51)
# s7 = s1[:5:2]   # 按照切片+步长
# print(s7)
# s8 = s1[-1:-6:-2]  # 如果想倒序取值，加一个反向步长
# s9 = s1[-1:-6:-1]
# print(s9)
# name = 'olDboy'
# print(name.capitalize())   *** #首字母大写
# print(name.center(20,'*'))   **  #字符串居中前后填充自定义的字符
# uppeer  lower *****  大小写  验证码应用广泛
# username = input('请输入用户名：')
# code = 'adfb'
# your_code = input('请输入验证码：').upper()
# if username == 'niu' and your_code == 'adfb'.upper():
#     print('登陆成功')
# else:
#     print('用户名或密码错误')
# print(name.upper())
# # print(name.lower())
# print(name.startswith('o'))
# print(name.swapcase())   #大小写反转  **
# s1 = 'alex wusir*taibai6nvshen'
# print(s1.title())     #title  非字母的每个首字母大写  **
# find index  *****
# print(name.find('D'))    #通过元素找索引,找到第一个就返回，没有此元素返回-1
# print(name.find('lD'))
# print(name.find('ID'))
# print(name.index('Q'))     #通过元素找索引,找到第一个就返回，没有此元素报错
# strip 默认去除字符串前后的空格 ，换行符，制表符  *****
# name = '**n**iu'
# print(name.strip('*'))
# lstrip   去掉左边或者前面的空格
# rstrip   去掉右边或者后面的空格
# username = input('请输入用户名：').strip()
# if username == 'alex':
#     print('登陆成功')
# s1 = 'alex','2222'
# l1 = s1.split()      #将字符串分割成列表（str---> list)  默认按照空格分割
# print(l1)
# s4 = 'alexlwle'
# print(s4.split('l',1))   #可以设置分割的次数  *****
# join  以自定制连接符，将可迭代对象中的元素连接起来      *****
# replace  用新的内容替换之前的内容  可以设置替换的次数（从左往右依次替换）
# 格式化输出format
# s1 = '我叫{0},今年{1},性别{2},我依然叫{0}'.format('taibai','26','nv')
# print(s1)
# is 系列
# name = 'taibai234'
# print(name .isalnum())   #数字或字母组成
# print(name.isdigit())     #判断是否全部都由数字组成
# print(name.isalpha())     #判断是否全部由字母组成
# 公共方法  count  计数  len  长度
# i = 'beriuta,383h,dabai'
# print(i.rsplit())
# count = 0
# while True:
#     name = input('请输入用户名：')
#     pw = input('请输入密码：')
#     count += 1
#     if name == 'niu' and pw == '2388':
#         print('登陆成功')
#         break
#     elif count > 2:
#         sum=input('三次机会用尽，请选择是否继续输入：')
#         if sum == '否':
#             print('您还要脸吗？')
#             break
#         else:
#             count -= 3
#     else:
#         print('请重新输入，您还剩{}次机会'.format(3 - count))
# li = 'sksaljljdjclkn'
# i = 0
# while i < len(li):
#     print(li[i])
#     i += 1
# li = 'skahdiwockc'
# for i in li :
#     print(i)
# dic = {'name':'fhs','age':'23','sex':'nv'}
# for k,v in dic.items():
#     print(k,v)
# 作业：1
# name = 'aleX leNb'
# print(name.strip())
# print(name.strip('al'))
# print(name.strip('Nb'))
# print(name[1:8])
# print(name.strip('ab'))
# print(name.startswith('al'))
# print(name.endswith('Nb'))
# print(name.replace('l','p'))
# print(name.replace('l','p',1))
# print(name.split('l'))
# print(name.split('l',1))
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.count('l'))
# print(name[1])
# print(name[0:5].count('l'))
# print(name.index('N'))
# print(name.find('N'))
# print(name.find('X le'))
# print(name[1])
# print(name[0:3])
# print(name[-2:])
# print(name.find('e'))
# s = '123a4b5c'     #第二题
# s1 = s[0:3]
# print(s1)
# s2 = s[3:-2]
# print(s2)
# s4 = s[1:-1:2]
# print(s4)
# s5 = s[-1]
# print(s5)
# s6 = s[-3::-2]
# print(s6)
# s = 'asdfer'      #第三题 while循环
# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1
# s = 'asdfer'          #for循环
# for i in s:
#     print(i)
# s = 'asdfer'             #第四题
# for i in s:
#     print(s)
# for i in s:             #第五题
#     print(i+'sb')
# s = '321'               #第六题
# for i in s:
#     print('倒计时{}秒'.format(i))
# print('出发！')
# num = 'whrD'
# print(num)
# name = input('请输入验证码：').upper()
# if num =='whrD':
#     print('验证码正确')
# find  index
# s = 'shGTh780fjkbxz'
# print(s.find('f'))
# print(s.index('f'))
# m = ('bsbs,mama,femme,fille,man')
# print(m.find('man'))
# str1 = 'this is string example.....wow!!!'
# str2 = 'exam'
# print(str1.find(str2))
# print(str1.find(str2,10))
# print(str1.find(str2,40))
# info = 'abcd'
# print(info.find('a'))
# print(info.find('a',1))
# print(info.find('3'))
# str1 = 'this is string example....wow!!!'
# str2 = 'exam'
# print(str1.index(str2))
# print(str1.index(str2,10))
# print(str1.index(str2,40))
# str = '000030111137184819999040000'
# print(str.strip('0'))
# str2 = '        rumua         '
# print(str2.strip())
# s = 'ejiejie,meimei,gege,ddi,renmbee'
# print(s.strip('e'))
# print(s.strip('12'))
# a = '\rzha ng\n\t '
# print(len(a))
# b = a.strip()
# print(b)
# print(len(b))
# s = 'rrrbbbrrddeeee'
# print(s.strip('re'))
# print(s)
# a = 'aaabcdfkls222jjclljsbbbaaa'
# print(a.strip('abc'))
# print(a.strip('acb'))
# print(a.strip('bac'))
# print(a.strip('cba'))
# a = '  zhangkang   '
# print(a.lstrip(),len(a.lstrip()))
# print(a.rstrip(),len(a.rstrip()))
# a = 'babababa2222babaccccddd'
# print(a.lstrip('abc'))
# print(a.rstrip('d'))
# split
# str = 'line1-abcdef \nLine2-abc \nLIne4-abcd'
# print(str.split())
# print(str.split(' ',1))
# u = 'wwweiwu.wooowio.skjhd.sljodwdjw.s.s.ioe.slk'
# print(u.split())
# print(u.split('.'))
# print(u.split('.',2))
# c = '''say
# hello
# baby'''
# print(c.split('\n'))
# str = 'hello boy<[www.doiido.com]>byebye'
# print(str.split('[')[1].split(']'[0]))
# print(str.split('[')[1].split(']')[0].split('.'))
# str = '-'
# seq =('a','b','c')
# print(str.join(seq))
# seq1 = ['hello','good','boy','doiio']
# print(' '.join(seq1))
# print(':'.join(seq1))
# seq2 = 'hello good boy doiio'
# print(':'.join(seq2))
# seq = {'hello':1,'good':2,'boy':3,'doiido':4}
# print(':'.join(seq))
# content = input('请输入内容：').split('+') #第七题
# s1=int(content[0])
# s2=int(content[1])
# print(s1+s2)
# content = input('请输入内容：').split('+')    #第八题
# num = 0
# for i in content:
#     num +=int(i)
# print(num)
# # content = input('请输入内容：')                #第九题
# count = 0
# for i in content:
#     if i in list('0123456789'):
#         count +=1
# print('数字的个数：{}'.format(count))
# while True:
#     name = input('请选择路程A,B,C:')
#     if name == 'A':
#         print('走大路回家')
#         sux = input('选择公交车还是步行:')
#         if sux == '公交车':
#             print('十分钟到家')
#             break
#         else:
#             print('显示20分钟到家')
#             break
#     elif name == 'B':
#         print('走小路回家')
#         break
#     elif name == 'C':
#         print('绕道回家')
#         sun = input('选择游戏厅玩会，还是网吧:')
#         if sun == '游戏厅玩会':
#             print('一个半小时到家，爸爸在家，拿棍等你。')
#         else:
#             print('两个小时到家，妈妈已做好了战斗准备。')
#     print('请重新输入A，B,C选项')
# num = 0
# count = 1
# while num < 100:
#     temp = num % 2
#     if temp == 0:
#         count -= 1
#     elif temp == 1:
#         count += 1
#     elif num == 88:
#         continue
#     num += 1
#     print(count)
# name = input("请输入姓名：")
# sex = input('请输入地点：')
# mtn = input('请输入爱好：')
# print('敬爱可亲的{},最喜欢在{}地方干{}'.format(name,sex,mtn))
# while True:
#     num = input('请输入内容：')
#     if num =='小粉嫩' or "大铁锤":
#         print('存在敏感字符请重新输入：')
#     else:
#         print(num)







