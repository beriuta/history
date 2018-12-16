# import re
# ret = re.findall('a', 'berita is a abaoy')
# print(ret)
# ret = re.search('a','berita is a abaoy')
# print(ret)
# ret = re.search('a','berita is a abaoy').group()
# print(ret)
# ret = re.match('a','abc')
# print(ret)
# ret = re.split('[ab]','sfobeaiuabcdaebfg')
# print(ret)
# ret = re.sub('\d','H','beri1uta3beos4sodf4',2)
# print(ret)
# ret = re.subn('\d','H','beri1uta3beos4sodf4')
# print(ret)
# obj = re.compile('\d{3}')
# ret = obj.search('absdd1234ewwwdj')
# print(ret.group())  # 123
# ret = re.finditer('\d','ausdi3798ds7fs')
# print(ret)  # <callable_iterator object at 0x7f6c48b21908>
# print(next(ret).group())  # 3
# print(next(ret).group())  # 7
# print([i.group() for i in ret])  # ['9', '8', '7']
#
# ret = re.findall('www.(baidu|sougou).com','www.baidu.com')
# print(ret)  # ['baidu']
# ret = re.findall('www.(?:baidu|sougou).com','www.baidu.com')
# print(ret)  # ['www.baidu.com']
#
# ret = re.split('\d+','eslh34830vc90b')
# print(ret)  # ['eslh', 'vc', 'b']
# ret = re.split('(\d+)','eslh34830vc90b')
# print(ret)  # ['eslh', '34830', 'vc', '90', 'b']

# 这里有个列表里面有很多小字典
list1 = [
    {'name': '广州', 'p_id': 1, 'p_name': '广东', 'p_weight': 50},
    {'name': '深圳', 'p_id': 1, 'p_name': '广东', 'p_weight': 50},
    {'name': '惠州', 'p_id': 1, 'p_name': '广东', 'p_weight': 50},
    {'name': '无锡', 'p_id': 3, 'p_name': '江苏', 'p_weight': 30},
    {'name': '济南', 'p_id': 2, 'p_name': '山东', 'p_weight': 10},
    {'name': '威海', 'p_id': 2, 'p_name': '山东', 'p_weight': 10},
    {'name': '苏州', 'p_id': 3, 'p_name': '江苏', 'p_weight': 30},
]

# 写代码把上面的列表转换成如下字典
dict1 = {
    1: {
        'id': 1,
        'name': '广东',
        'weight': 50,
        'children': [{'name': '广州'}, {'name': '深圳'}, {'name': '惠州'}]
    },
    3: {
        'id': 3,
        'name': '江苏',
        'weight': 30,
        'children': [{'name': '无锡'}, {'name': '苏州'}]},
    2: {
        'id': 2,
        'name': '山东',
        'weight': 10,
        'children': [{'name': '济南'}, {'name': '威海'}]
    }
}


# 对得到的字典按照weight从大到小排序， 得到如下列表
# [{'id': 1, 'name': '广东', 'weight': 50, 'children': [{'name': '广州'}, {'name': '深圳'}, {'name': '惠州'}]}, {'id': 3, 'name': '江苏', 'weight': 30, 'children': [{'name': '无锡'}, {'name': '苏州'}]}, {'id': 2, 'name': '山东', 'weight': 10, 'children': [{'name': '济南'}, {'name': '威海'}]}]

list1 = [
    {'name': '广州', 'p_id': 1, 'p_name': '广东', 'p_weight': 50},
    {'name': '深圳', 'p_id': 1, 'p_name': '广东', 'p_weight': 50},
    {'name': '惠州', 'p_id': 1, 'p_name': '广东', 'p_weight': 50},
    {'name': '无锡', 'p_id': 3, 'p_name': '江苏', 'p_weight': 30},
    {'name': '济南', 'p_id': 2, 'p_name': '山东', 'p_weight': 10},
    {'name': '威海', 'p_id': 2, 'p_name': '山东', 'p_weight': 10},
    {'name': '苏州', 'p_id': 3, 'p_name': '江苏', 'p_weight': 30},
]
dict2 = {
    'id': '',
    'name': '',
    'weight':'',
    'children': ''
}
for i in list1:
    if i['p_id'] == 1:










