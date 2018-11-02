from django.shortcuts import render
from datetime import datetime,timedelta

# Create your views here.
def t(request):
    name = '测试'
    d1 = {'name': '小鬼', 'age': 18, 'hobby': 'eat', 'items': 'hello'}

    class People:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        @staticmethod
        def dream():
            return 'Write the code,Change the world'

    p5 = People('小懒虫', 1)
    p1 = People('小明', 23)
    p2 = People('小红', 13)
    p3 = People('小白', 15)
    list1 = [p1, p2, p3]

    list2 = ['深圳', '上海', '北京', '广州', '东莞', '威海', '青岛', '潍坊']
    return render(request, 't.html', {'name': name, 'd1': d1, 'f5': p5, 'list': list1, 'list2': list2})


def s(request):
    l = [11, 32, 73]
    name = '小懒虫'

    class Food:
        def __init__(self, name, kg):
            self.name = name
            self.kg = kg

        # @staticmethod  #当一个函数用不到self的时候，可以在上面添加一个装饰器
        def dream(self):
            return '{}的梦想：世界唯有美食不可辜负！'.format(self.name)  # 这里不能用print，不然会直接在后台打印，页面不显示

    duck = Food('烤鸭', 2)
    pig = Food('烤猪', 50)
    sheep = Food('烤全羊', 30)
    chicken = Food('炸鸡', 23)
    lst = [pig, sheep, chicken]
    return render(request, 's.html',
                  {
                      'l': l,
                      'name': name,
                      'food': duck,
                      'lst': lst
                  }
                  )


# filter语法相关
def m(request):
    name = 'Beriuta'
    file_size = 10000
    a = '<a href="https://www.baidu.com">百度</a>'
    p = '在苍茫的大海上，狂风卷积着乌云，在乌云和大海之间，海燕像黑色的闪电，在高傲地飞翔！'
    p_1 = '在 苍 茫 的 大 海 上，狂风卷积着乌云，在乌云和大海之间，海燕像黑色的闪电，在高傲地飞翔！'
    p_2 = 'aaabsbshsasjahahaayaha'
    now = datetime.now()  # 获取一个datetime类型的时间
    list1 = ['huhu','hehe','didi','shil','sb']
    # 获取五个小时之前的时间
    hours = now - timedelta(hours=4)
    return render(request, 'm.html',
                  {'name': name,
                   'file_size':file_size,
                   'now':now,
                   'a':a,
                   'p':p,
                   'p_1':p_1,
                   'p_2':p_2,
                   'list1':list1,
                   'hours':hours

                   }
                  )
