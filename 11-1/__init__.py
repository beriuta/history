# from functools import wraps
from datetime import datetime
# def wrapper(func):
#     @wraps(func)  # 写在实际执行函数的上面
#     def inner(*args,**kwargs):
#         print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %w'))
#         r = func(*args,**kwargs)
#         print('新功能也可以写这里')
#         return r
#     return inner

# from functools import wraps
# from datetime import datetime
# def wrapper(func):
#     @wraps(func)
#     def inner(*args,**kwargs):
#         print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %w'))
#         r = func(*args,**kwargs)
#         print('新功能在这里')
#         return r
#     return inner
from dateutil.parser import parse
# import datetime
from dateutil import rrule
# y = input('请输入年：')
# m = input('请输入月')
# d = input('请输入日')
# # ye = input('请输入年月日，以”-“分隔:')
# # ye_list  =ye.strip().split('-')
# # print(data,type(data))
# today = datetime.date.today()
# oneday = datetime.date(int(y),int(m),int(d))
# # days = rrule.rrule(rrule.DAILY, dtstart=oneday, until=today).count()
# # print(days)
# years = rrule.rrule(rrule.YEARLY, dtstart=oneday, until=today).count()
# print(years)
from dateutil.relativedelta import relativedelta
from datetime import date
import datetime
now = date.today()
print(now)
tim = input('>>>')
# ret1 = '{} 00:00:00'.format(tim)
# ret2 = time.strptime(ret1,"%Y-%m-%d %H:%M:%S")
# print(ret2)
# nn = now - ret2
# date_str = '2017-10-19'
tim1 = datetime.date(*map(int, tim.split('-')))
print(tim1,type(tim1))
new = now - tim1
print(new)
# ret = relativedelta(ret2,tim1)
# print(ret)
# tss1 = '2013-10-10 23:40:00'
# timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
# print(timeArray)








