# s1 = 'alexsb'
# s2 = s1[100:]
# print(s2)
# count = 1
# sux = 0
# while count < 100:
#     if count == 88:
#         count += 1
#
#     if count % 2 ==0:
#         sux -= count
#     else:
#         sux += count
#     count += 1
# print(sux)
# num = 1
# count = 0
# while num < 100:
#     if num == 88:
#         num += 1
#     temp = num % 2
#     if temp == 0:
#         count -= num
#     elif temp == 1:
#         count += num
#     num += 1
# print(count)
# content = input('请输入内容：').strip()
# num_list = content.split('+')
# result = int(num_list[0])+int(num_list[1])
# print(result)
# content = input('请输入内容：').strip()
# for i in content.split('+'):
#     pass
# l1 = ['alex', 'wusir', 'taibai', 'egon', '景女神', '文周老师', '日天']
# l1.append('bebe')
# # print(l1)
# l1.insert(5,'bebe')
# print(l1)
# l1.extend('[wjjsjd]')
# print(l1)
# l1.pop(0)
# print(l1)
# l1.remove('egon')
# print(l1)
# l1.clear()
# print(l1)
# del l1[5]
# print(l1)
# del l1[:3:2]
# print(l1)
# l1[2] = '女神'
# print(l1)
# l1[:4] =['shebdjkf','dh','222']
# print(l1)
# l1[:4:2]=('dd')
# print(l1)
# for i in l1:
#     print(i)
# s2 = len(l1)
# # print(s2)
# print(l1.count('alex'))
# print(l1.index('alex'))
# l2 =[4, 5, 7, 3, 2, 1, 8, 9, 0]
# l2.sort()
# print(l2)
# l2.sort(reverse=True)
# print(l2)
# l2.reverse()
# print(l2)
# l3 = ['alex', 'wusir', ['taibai',99,'ritian'], 20]
# s1 = l3[0]
# print(s1[2])
# s2 = l3[0][2]
# print(s2)
# s2 = l3[1]
# w=s2.upper()
# l3[1] = w
# print(l3)
# l3[1] = l3[1].upper()
# print(l3)
# l3[2].append('文周')
# print(l3)
# l3[2][0] = l3[2][0].capitalize()
# print(l3)
# l3[2][1] = l3[2][1] + 1
# l3[2][1] +=1
# print(l3)
# l1 = ['alex', 'wusir', 'taibai', 'egon', '景女神', '文周老师', '日天']
# for i in range(0,len(l1)):
#     print(i)
# for i in l1:
#     print(l1.index(i))      #列表不能用重复的元素
# s2 = l1.count('alex')
# print(s2)
# l3 = ['alex', 'wusir', ['taibai',99,'ritian'], 20]
# print(l3[0][2])
# l3[1] = l3[1].upper()
# print(l3)
# l3[-2].append('文州')
# print(l3)
# l3[-2][0] = l3[-2][0].capitalize()
# print(l3)
# l3[-2][1] += 1
# print(l3)
# l1 = ['alex', 'wusir', 'taibai', 'egon', '景女神', '文周老师', '日天']
# for i in range(len(l1)):
#     print(i)
# l1=['bebe' , '美国' , '中国' , '日本' , '韩国' , '纽约']
# l1.insert(3 ,'法国')
# print(l1)
# l1.insert(4,'印尼')
# print(l1)
# l1.extend('非洲')
# print(l1)
# l1.pop(-1)
# print(l1)
# l1.remove('非')
# print(l1)
# l1[0] = '朝鲜'
# print(l1)
# l1[:3] = '南法','北法','埃菲尔铁塔','左罗门'
# print(l1)
# content = input('请输入内容：').strip()
# count = 0
# for i in content:
#     if i.isdigit():
#         count += 1
# print(count)
# sam = 0
# count = 0
# while sam < 100:
#     if sam == 88:
#         sam += 1
#
#     if sam % 2 == 0:
#         count -= sam
#     else:
#         count += sam
#     sam += 1
# print(count)
# cut = input('请输入内容：').strip()
# num_list = cut.split('+')
# result = int(num_list[0])+int(num_list[1])
# print(result)
# name_list = ['赵三','李四']
# while 1:
#     username = input('请输入新员工姓名：').strip()
#     if username.upper() == 'Q':
#         break
#     name_list.append(username)
#     print(name_list)
# s = ['南法', '北法', '埃菲尔铁塔', '左罗门', '日本', '韩国', '纽约']
# for i in s:
#     print(i)
# count = 0
# for i in range(len(s)):
#         count += 1
# print(count)
# print(s.index('北法'))
# for i in s:                      #i是元素，s是整个列表，要通过i到s这个列表去找，i随着循环一直都在变
#     print(s.index(i))
# nam = ['小红','小明']
# while 1:
#     name_list = input('请输入姓名：').strip()
#     if name_list.upper() == 'Q':
#         break
#     nam.append(name_list)
#     print(nam)
# str = 'title={WiMAX Power Amplifier Design based on Si-LDMOS},author={Nader, Charles and De Carvalho, Nuno Borges},journal={University of Galve, Sweden},year={2006}'
# # for item in str.split(' '):
# #     print(item)
# for item in str.split('},'):
#     try:
#         if 'author'in item:
#             print(item.split('{',1))
#     except Exception as e :
#         print(e)
# content = input('请输入内容：').split('+')
# num = 0
# for i in content:
#     num += int(i)
# print(num)
# s = ['南法', '北法', '埃菲尔铁塔', '左罗门', '日本', '韩国', '纽约']
# print(s[5])
# print(s.index('日本'))
# print(s[:5:2])
# s[:3:-2] = '北京','上海'
# print(s)
# s1 = [2, 4, 1, 6, 9, 0]
# s1.sort()
# print(s1)
# s1.sort(reverse=True)
# print(s1)
# s1.reverse()
# print(s1)
# s[:4] = 'sjdifffo'
# print(s)
# s[2:5:1] = 'sjh'
# print(s)
# for i in s:
#     print(i)
# for i in s:
#     print(len(i))
# for i in range(len(s)):
#     print(i)
# range(5)
# for i in range(5):
#     print(i)
# print(list(range(5)))
# print(list(range(0,30,5)))
# print(list(range(0,10,2)))
# languages = ['c','c++','perl','python']
# for x in languages:
#     print(x)
# sites = ['baidu','google','runoob','taobao']
# for site in sites:
#     if site == 'runoob':
#         print('来跳舞')
#         break
#     print('循环数据'+ site)
# else:
#     print('没有数据循环！')
# print('完成循环')
# day4作业及默写
# 1，写代码，有如下列表，按照要求实现每一个功能
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# print(len(li))           # 1)计算列表的长度并输出
# li.append('seven')       # 2)列表中追加元素"seven", 并输出添加后的列表
# print(li)
# li.insert(0,'Tony')      # 3)请在列表的第1个位置插入元素 "Tony", 并输出添加后的列表
# print(li)
# li[1] = 'Kelly'           # 4)请修改列表第2个位置的元素为 "Kelly", 并输出修改后的列表
# print(li)
# l2 = [1, "a", 3, 4, "heart"]    # 5)请将列表l2 = [1, "a", 3, 4, "heart"]的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# li.extend(l2)
# print(li)
# li.extend('qwert')            # 6)请将字符串s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
# print(li)
# li.remove('alex')                # 7)请删除列表中的元素"alex", 并输出添加后的列表
# print(li)
# print('删除的元素：'+li[1])              # 8)请删除列表中的第2个元素，并输出删除的元素和删除元素后的列表
# del li[1]
# print(li)
# del li[1:4]                              # 9)请删除列表中的第2至4个元素，并输出删除元素后的列表
# print(li)
# li.reverse()                                 # 10)请将列表所有得元素反转，并输出反转后的列表
# print(li)
# sum = 0                                        # 11)请计算出#"alex"#元素在列表li中出现的次数，并输出该次数。
# for i in li:
#     if i.count('alex'):
#         sum += 1
#         print(sum)
# 2，写代码，有如下列表，利用切片实现每一个功能
# li = [1, 3, 2, "a", 4, "b", 5, "c"]
# print(li[:3])                                     # 1)通过对li列表的切片形成新的列表l1, l1 = [1, 3, 2]
# print(li[3:6])                                      # 2)通过对li列表的切片形成新的列表l2, l2 = ["a", 4, "b"]
# print(li[::2])                                         # 3)通过对li列表的切片形成新的列表l3, l3 = ["1,2,4,5]
# print(li[1:-2:2])                                         #4)通过对li列表的切片形成新的列表l4, l4 = [3, "a", "b"]
# print(li[-1])                                             # 5)通过对li列表的切片形成新的列表l5, l5 = ["c"]
# print(li[-3:0:-2])                                          # 6)通过对li列表的切片形成新的列表l6, l6 = ["b", "a", 3]
# 3, 写代码，有如下列表，按照要求实现每一个功能。
# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
# lis[3][2][1][0] = lis[3][2][1][0].upper()                   #  1)将列表lis中的"tt"变成大写（用两种方式）。
# print(lis)
# lis[3][2][1][0] ='TT'
# print(lis)
# lis[1] = '100'
# print(lis)                                                            # 2)将列表中的数字3变成字符串"100"（用两种方式）。
# lis[1] = str(100)
# print(lis)
# lis[3][2][1][2] = 101                                          # 3)将列表中的字符串"1"变成数字101（用两种方式）。
# print(lis)
# lis[3][2][1][2] = int(101)
# print(lis)
# 4, 请用代码实现：
# li = ["alex", "eric", "rain"]
# print('_'.join(li))                              # 利用下划线将列表的每一个元素拼接成字符串"alex_eric_rain"
# 5，利用for循环和range打印出下面列表的索引。
# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# for i in range(len(li)):
#     print(i)
# 6，利用for循环和range找出100以内所有的偶数并将这些偶数插入到一个新列表中。
# s1 = [ ]
# for i in range(2,101,2):
#     s1.append(i)
# print(s1)
# 7，利用for循环和range找出50以内能被3整除的数，并将这些数插入到一个新列表中。
# s1 = []
# for i in range(1,50):
#     if i % 3 == 0:
#         s1.append(i)
# print(s1)
# 8，利用for循环和range从100 ~1，倒序打印。
# for i in range(100,-1,-1):
#     print(i)
# 9，利用for循环和range从100 ~10，倒序将所有的偶数添加到一个新列表中，然后对列表的元素进行筛选，将能被4整除的数留下来。
# s1 = []
# for i in range(100,9,-1):
#     if i % 4 == 0:
#         s1.append(i)
# print(s1)
# 10，利用for循环和range，将1 - 30的数字一次添加到一个列表中，并循环这个列表，将能被3整除的数改成 *。
# s1 = []
# for i in range(1,31):
#         s1.append(i)
# print(s1)
# for i in range(30):
#     if s1[i] % 3 ==0:
#         s1[i]="*"
# print(s1)
# 11，查找列表li中的元素，移除每个元素的空格，并找出以"A"或者"a"开头，并以 "c"结尾的所有元素，并添加到一个新列表中, 最后循环打印这个新列表。
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
# seult = []
# for i in li:
#     j = i.strip()
#     if (j.startswith('a') or j.startswith('A')) and j.endswith('c'):
#         seult.append(j)
# print(seult)
# 12，开发敏感词语过滤程序，提示用户输入评论内容，如果用户输入的内容中包含特殊的字符：敏感词列表
# 则将用户输入的内容中的敏感词汇替换成等长度的 *（苍老师就替换 ** *），并添加到一个列表中；如果用户输入的内容没有敏感词汇，则直接添加到上述的列表中。
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# name = input('请输入评论内容：').strip()
# result = []
# for i in li:
#     if i in name:
#         name = name.replace(i,'*'*len(i))
#         result.append(name)
# print(name)


#
# 13，有如下列表
# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
# 循环打印列表中的每个元素，遇到列表则再循环打印出它里面的元素。
# 我想要的结果是：
# 1
# 3
# 4
# "alex"
# 3
# 7,
# 8
# "taibai"
# 5
# ritian
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# result = []
#
#
# while True:
#     content = input('请输入内容：\n')
#     for i in li:
#         if i in content:
#             a = content.replace(i, '*'*len(i))
#             result.append(a)
#     print(result)
