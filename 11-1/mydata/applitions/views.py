from django.shortcuts import render


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
    return render(request, 'm.html', {'name': name})
