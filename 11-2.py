from datetime import datetime
from dateutil import relativedelta

var = input('请输入年月日(以xxxx-xx-x格式):')
now = datetime.now()
temp = datetime.strptime(var, '%Y-%m-%d')
ret = relativedelta.relativedelta(now, temp)
print('您已出生{obj.years}年{obj.months}月{obj.days}天'.format(obj=ret))
