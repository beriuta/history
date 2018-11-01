from functools import wraps
from datetime import datetime
def wrapper(func):
    @wraps(func)  # 写在实际执行函数的上面
    def inner(*args,**kwargs):
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S %w'))
        r = func(*args,**kwargs)
        print('新功能也可以写这里')
        return r
    return inner
