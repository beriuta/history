# dic = {'name': '太白', 'age': 18, 'sex': '男', 'job': 'IT'}
# print(dic.pop('name1','没有此键'))
# print(dic.clear())
# print(dic.popitem())
# del dic['name']
# print(dic)
# dic['age'] = 25
# print(dic)
# dic2 = {'name':'alex','hoppy':'feill'}
# dic.update(dic2)
# print(dic)
# print(dic.get('name'))
# print(dic.keys())
# l1 = list(dic.keys())
# print(l1)
# l1 = list(dic.values())
# print(l1)
# print(dic.items())
# for i in dic:
#     for k,v in i.items
# dic = {'name_list': ['王双', 'alex', '孙飞', 'taibai'],
#        1: {'name': 'taibai', 'age': 18, 'sex': '男'},
#        (1, 2): [100, {'ip': '192.168.1.1', 'port': 3306}]
#        }
# dic ['name_list'].append( '司徒大人')
# print(dic)
# dic.get('name_list')[1]=dic.get('name_list')[1].upper()
# print(dic)
# dic[1].update(weight=75)
# print(dic)
# dic[1]['weight'] = 75
# print(dic)
# dic[1].setdefault('weight',75)
# print(dic)
# dic[1].update(name = 'alex')
# print(dic)
# dic[(1,2)][1].pop('port')
# print(dic)
# dic['name_list'].append('司徒大人')
# print(dic)
# dic[1].update(name = 'alex')
# print(dic)
# dic['name_list'][1] =dic['name_list'][1].upper()
# print(dic)
# dic[1].setdefault('weight',75)
# print(dic)
# dic[(1,2)][1].pop('port')
# print(dic)
# dic = {'name':'Beriuta','age':'18','hoppy':'chanson','sex':'fille'}
# dic.setdefault('class',3)
# print(dic)
# print(list(dic.values()))
# print(dic.items())
# dic.setdefault('k','v')   #随机加在里面
# print(dic)
# dic.setdefault('k','v1')   #如果原字典中含有本身的键跟值，那么新添加的不覆盖不更改
# print(dic)
# dic.pop('age')               #pop删除都是键值对的形式
# print(dic)
# del dic['name']
# print(dic)
# dic.popitem()
# print(dic.popitem())             #随机删除字典的某个键对值，以元祖的的形式返回
# dic_clear = dic.clear()
# print(dic.clear())                 #清空字典
# print(dic,dic_clear)                #{} None
# dic.update(hello='world')            #括号里面第一个是键，不应该加引号
# print(dic)
# dic2 = {'国家':'和平','繁荣':'昌盛'}         #这是把dic所有的键值对覆盖添加（相同的覆盖，没有的添加）到dic2
# dic2.update(dic)                       #要添加的哪个，哪个在前面
# print(dic2)
# valuel = dic['name']                    #查询dic[]里面的键对应的值
# print(valuel)
# value = dic.get('dkkjfhdkfh','默认返回值')      #如果字典没有找寻的键 就返回设定的返回值
# print(value)
# item = dic.items()                        #dict是字典  dict_items是字典中的一个类型，里面是以元祖的形式打印出来的
# print(item)
# keys = dic.keys()                            #也是dict的一种形式   dict_keys
# print(keys)
# values = dic.values()
# print(values)                                #是dic的一种形式     dic_values
# dic = {'name':'Beriuta','age':'18','hoppy':'chanson','sex':'fille'}
# for key in dic:
#        print(key)                            #把字典的所有的键打印出来
# li = [2, 4,[5,'sdkkf',{'name':'miao'},],6,'eckx']
# for i in li:
#        if type(i) == list:
#               for key in i:
#                      if type(key)== str:
#                             print(key.lower())
#                      else:
#                             print(key)
#        elif type(i) == str:
#               print(i.lower())
#        else:
#               print(i)
# for item in dic.items():
#        print(item)                         #把字典以元祖的形式循环打印出来
# for key,value in dic.items():                #把键跟值从字典的dic.items类型中打印出来
#        print(key,value)
# li = [1,'a','b',2, 3,'a','c']
# li.insert(0,55)                             #按照索引把元素添加进去
# print(li)
# li.insert(5,'d')
# print(li)
# li.insert(4,'ddd')
# print(li)
# li.insert(7,'r')
# print(li)
# li.insert(3,'ghftrt')
# print(li)
# li.extend(['a,e,r,c,x,zz,'])                     #迭代的增加
# print(li)
# li.extend(['a,e,','r,','c,x,zz,'])                  #按照引号的分割方式迭代添加
# print(li)
# li.extend('2,3,4,5,')
# print(li)
# li.extend('a')
# print(li)
# li.extend('axd')
# print(li)
# li.extend('a,b,c')                                  #里面每一个字符都会被迭代添加进去，标点符号也算
# print(li)
# li.pop(1)                                              #按照索引位置去删除，有返回值
# print(li)
# li.remove('c')                                          #按照remove括号里的元素删减
# print(li)
# li.remove('a')
# print(li)
# li.clear()
# print(li)
# 列表的增
# append()   追加
# extend()   按照元素添加
# isert()    按照索引去添加
# 删
# pop(1，x)   按照索引删除
# remove('c')   按照元素删除
# del
# del li[]
# del li[1:7]
# del li
# 改
# 切片  索引  切片+步长
# 查
# for循环查询
# count  指定元素所出现的个数
# len  整个列表的长度
# 其他
# sort, 从小到大重新排列
# sort(reverse=True)   从大到小
# reverse   翻转
# index  从列表中的值打印索引位置
# dic.setdefault('k')
# print(dic)
# setdefault 在字典中添加键值对，如果键没有对应的值，则显示none，但如果原字典中存在设置的键值对，则他不会更改或者覆盖
# dic.setdefault('中国','美国')
# print(dic)
# dic.setdefault('d','m')
# print(dic)
# dic.setdefault('v,m')
# print(dic)
# dic.pop('name')
# print(dic)
# dic.pop('age')
# print(dic)
# pop 根据key删除键对值，并返回对应的值，如果没有key则返回默认返回值
# print(dic.pop('name'))
# del dic['name']
# print(dic)
# dic_pop1 = dic.popitem()
# print(dic_pop1)
# popitem  随即删除字典中某个键值对，将删除的键值对以元祖的形式返回，括号里面不能添加元素
# dic_clear = dic.clear()
# print(dic_clear,dic)
# 字典的update,将dic所有的键值对覆盖添加（相同的覆盖，没有的添加）到dic2中
# update,也可以当做增加键值对使用
# dic.update(name='yun')     #使用方法是括号里面第一个是键不能加引号‘’中间只能用等号，后面所对应的值字符串或者数字
# print(dic)
# dic.update(weight=44)
# print(dic)
# dic['name']='vue'
# print(dic)
# dic.setdefault('v','v')            #只能添加不同的键，不然没有反应
# print(dic)
# dic.update(name='kl')
# print(dic)
# dic['name']  是检查这个键是否存在字典中
# print(dic['name'])
# print(dic.get('skdhfksd','默认返回值'))
# s1 = dic.get('sdjsjf')
# print(s1)
# get  查询字典中是否存在某个键值对
# 字典的循环
# for key in dic:
#        print(key)          #打印出的全部是键
# for item in dic.items():
#        print(item)         #键跟值以元祖的形式打印
# for key,value in dic.items():
#        print(key,value)         #键跟值是以字符的形式打印出来
# msg = 'odfoidugodigudofjdfig'
# for item in msg:
#        print(item)
#单独打印成一串
# li = ['alex','银角','女神','egon','taibia']
# for i in li :
#        print(i)
#把每个字符串成串打印出来
# dic = {'name':'太白','age':18,'sex':'man'}
# for k,v in dic.items():
#        print(k,v)
#打印出以键值对的竖排串
# dic = {'name_list': ['王双', 'alex', '孙飞', 'taibai'],
#        1: {'name': 'taibai', 'age': 18, 'sex': '男'},
#        (1, 2): [100, {'ip': '192.168.1.1', 'port': 3306}]
#        }
# 1,给 name_list对应的列表追加一个值: 司徒大人.
# 2,将name_lsit对应的alex 变成全部大写.
# 3, 将1对应的字典添加一个键值对: weight : 75
# 4,将1 对应的字典的name键对应的名字taibai 换成alex
# 5,将 {'ip': '192.168.1.1', 'port': 3306} 次字典的port键值对删除.
# dic['name_list'].append('司徒大人')
# print(dic)
# dic['name_list'][1] =dic['name_list'][1].upper()
# print(dic)
# dic[1].update(weight=75)
# print(dic)
# dic[1]['weight']=75
# print(dic)
# dic[1].setdefault('weight',75)
# print(dic)
# dic[1]['name'] = 'alex'
# print(dic)
# dic[1].update(name='alex')
# print(dic)
# dic[1].setdefault('name','alex')    #不显示所更改的项目,因为setdefault对于字典中存在的键值对是更改不了的
# print(dic)
# dic[(1,2)][1].pop('port')
# print(dic)
# dic[(1,2)][1].popitem('port', 3306)    #显示popitem不接受参数的指定
# print(dic)
# set1 = set({1,2,'barry'})
# set2 ={1,2,'barry'}
# print(set1,set2)
# {1, 2, 'barry'} {1, 2, 'barry'}          #集合的创建
# set1 = {'alex','wusir','ritian','egon','barry'}
# set1.add('景女神')
# print(set1)
# add     随机添加进这个集合
# update     迭代着增加
# set1.update('A')
# print(set1)
# set1.update('老司机')
# print(set1)
# set1.update([1,2,3])
# print(set1)
# set1 = {'alex','wusir','ritian','egon','barry'}
# set1.remove('alex')
# print(set1)
# set1.clear()
# print(set1)
# del set1
# print(set1)
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1|set2)           #并集取两个集合不通透的数据结合在一个集合里
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1 & set2)           #交集
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1 ^ set2)              #反交集
# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7,8}
# print(set1 < set2)               #返回bool值
# set1 = {1,2,3}
# set2 = {1,2,3,4,5,6}
# print(set2 > set1)
# dic = {'name':'Beriuta','age':18,'sex':'feille'}
# day5作业及默写
# 1，有如下变量（tu是个元祖），请实现要求的功能
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11, 22, 33)}, 44])
# a.讲述元祖的特性
# 元祖是Python的数据类型之一,可以储存大量的数据,并且具有不可改变性
# b.请问tu变量中的第一个元素"alex"是否可被修改？
# 不可以修改
# c.请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素"Seven"
# K2对应的值是列表,并且可以修改
# tu[1][2]['k2'].append('Seven')
# print(tu)
# d.请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素"Seven"
# k3属于元祖,不可以被修改
# 2， 字典dic,
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}                # a.请循环输出所有的key
# for key in dic:
#        print(key)
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}                # b.请循环输出所有的value
# for value in dic.values():
#        print(value)
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}                # c.请循环输出所有的key和value
# for k,v in dic.items():
#        print(k,v)
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}                # d.请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic.update(k4='v4')
# print(dic)
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}                # e.请在修改字典中"k1"对应的值为 "alex"，输出修改后的字典
# dic['k1']='alex'
# print(dic)
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}                 # f.请在k3对应的值中追加一个元素44，输出修改后的字典
# dic['k3'].append(44)
# print(dic)
# dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}                # g.请在k3对应的值的第 1个位置插入个元素18，输出修改后的字典
# dic['k3'].insert(0,18)
# print(dic)
# av_catalog = {
#        "欧美": {
#               "www.youporn.com": ["很多免费的,世界最大的", "质量一般"],
#               "www.pornhub.com": ["很多免费的,也很大", "质量比yourporn高点"],
#               "av_catalog": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
#               "x-art.com": ["质量很高,真的很高", "全部收费,屌丝请绕过"]
#        },
#        "日韩": {
#               "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]
#        },
#        "大陆": {
#               "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
#        }
# }
# av_catalog['欧美']['www.youporn.com'].insert(1,'量很大')                            # a, 给此["很多免费的,世界最大的", "质量一般"]列表第二个位置插入一个元素：'量很大'。
# print(av_catalog)
# av_catalog['欧美']['x-art.com'].pop(1)                                             # b, 将此["质量很高,真的很高", "全部收费,屌丝请绕过"]列表的"全部收费,屌丝请绕过"删除。
# print(av_catalog)
# av_catalog['日韩']['tokyo-hot'][1] = av_catalog['日韩']['tokyo-hot'][1].upper()          # d, 将此["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]列表的"verygood"全部变成大写。
# print(av_catalog)
# av_catalog['大陆'].setdefault('1048','一天就封了')                                        # e, 给 '大陆' 对应的字典添加一个键值对'1048': ['一天就封了']
# print(av_catalog)
# av_catalog['欧美'].pop('av_catalog')                                                 # f, 删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"]键值对。
# print(av_catalog)
# av_catalog['大陆']['1024'].insert(0,'可以爬下来')                                       # g, 给此["全部免费,真好,好人一生平安", "服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
# print(av_catalog)
# 4、有字符串
# "k:1|k1:2|k2:3|k3:4"处理成字典{'k': 1, 'k1': 2....}
# s = 'k:1|k1:2|k2:3|k3:4'
# new_dic ={}
# for item in s.split('|'):
#        s=item.split(':')
#        new_dic.setdefault(s[0],s[1])
# print(new_dic)
# 5、元素分类
# 有如下值li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]，将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值列表, 'k2': 小于66的所有值列表}
# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# l1 = []
# l2 = []
# dic ={}
# for i in li:
#        if i > 66:
#               l1.append(i)
#
#        elif i < 66:
#               l2.append(i)
# dic.update(k1=l1,k2=l2)    #({k1:l1,k2:l2})
# print(dic)

goods = [{"name": "电脑", "price": 1999},
         {"name": "鼠标", "price": 10},
         {"name": "游艇", "price": 20},
         {"name": "美女", "price": 998}, ]

while 1:
       num = int(input('请输入商品序号:').strip())
       if num.upper()=='q':
              break
       elif num > len(goods):
              # for i in goods:

              # print(goods(len))

              print(i['name'])
              print(i['price'])

















