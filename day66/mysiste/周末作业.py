import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysiste.settings")

    import django

    django.setup()

    import datetime
    from apphomework.models import Author, AuthorInfo, Book, Publisher2

    # 查找所有书名里包含番茄的书
    # ret = Book.objects.filter(title__contains="番茄")
    # print(ret)
    # 查找出版日期是2017年的书
    # temp = datetime.date
    # ret = Book.objects.filter(pub_date__year=2017)
    # print(ret)  # <QuerySet [<Book: 猴子物语>]>
    # 查找出版日期是2017年的书名
    # ret = Book.objects.filter(pub_date__year=2017).values_list('title')
    # print(ret)
    # 查找价格大于50元的书
    # ret = Book.objects.filter(price__gt=50)
    # print(ret)  # <QuerySet [<Book: 番茄物语>, <Book: 黄瓜物语>, <Book: 西瓜物语>, <Book: 冬瓜物语>, <Book: 和马物语>, <Book: 鳄鱼物语>, <Book: 猩猩物语>, <Book: 猴子物语>, <Book: 香蕉物语>]>
    # # 查找价格大于500元的书名和价格
    # ret = Book.objects.filter(price__gt=500).values('title', 'price')
    # print(ret)  # <QuerySet [{'title': '猴子物语', 'price': Decimal('657.43')}]>
    # # 查找memo字段是空的书
    # ret = Book.objects.filter(memo=None)
    # print(ret)  # <QuerySet [<Book: 鳄鱼物语>, <Book: 番茄炒鸡蛋>]>
    # # 查找在北京的出版社
    # ret = Publisher2.objects.filter(city='北京')
    # print(ret)  # <QuerySet [<Publisher2: 沙河出版社>, <Publisher2: 金融出版社>]>
    # # 查找名字以沙河开头的出版社
    # ret = Publisher2.objects.filter(p_name__startswith='沙河')
    # print(ret)  # <QuerySet [<Publisher2: 沙河出版社>, <Publisher2: 沙河1出版社>, <Publisher2: 沙河2出版社>]>
    # # 查找作者名字里面带“小”字的作者
    # ret = Author.objects.filter(a_name__contains='小')
    # print(ret)  # <QuerySet [<Author: 小猫>, <Author: 小狗>]>
    # # 查找年龄大于30岁的作者
    # ret = Author.objects.filter(age__gt=30)
    # print(ret)  # <QuerySet [<Author: 小猫>, <Author: 小狗>, <Author: 阿狗>, <Author: 阿花>, <Author: 麋鹿>, <Author: 燕子>]>
    # # 查找手机号是155开头的作者
    # ret = Author.objects.filter(phone__startswith='155')
    # print(ret)  # <QuerySet [<Author: 麋鹿>]>
    # # 查找手机号是155开头的作者的姓名和年龄
    # ret = Author.objects.filter(phone__startswith='155').values('a_name','age')
    # print(ret)  # <QuerySet [{'a_name': '麋鹿', 'age': 1039}]>
    # # 查找书名是“番茄物语”的书的出版社
    # ret = Publisher2.objects.filter(book__title='番茄物语')
    # print(ret)  # <QuerySet [<Publisher2: 沙河出版社>]>
    # # 查找书名是“番茄物语”的书的出版社所在的城市
    # ret = Publisher2.objects.filter(book__title='番茄物语').values('city')
    # print(ret)  # <QuerySet [{'city': '北京'}]>
    #
    # # 查找书名是“番茄物语”的书的出版社的名称
    # ret = Publisher2.objects.filter(book__title='番茄物语').values('p_name')
    # print(ret)  # <QuerySet [{'p_name': '沙河出版社'}]>
    #
    # # 查找书名是“番茄物语”的书的所有作者
    # ret = Author.objects.filter(book__title='番茄物语')
    # print(ret)  # <QuerySet [<Author: 小猫>, <Author: 阿毛>, <Author: 阿狗>, <Author: 阿花>]>
    # ret2 = Book.objects.get(title="番茄物语").author.all()
    # print(ret2)  # <QuerySet [<Author: 小猫>, <Author: 阿毛>, <Author: 阿狗>, <Author: 阿花>]>
    # print(Book.objects.filter(title="番茄物语").values("author__a_name"))
    # #<QuerySet [{'author__a_name': '小猫'}, {'author__a_name': '阿毛'}, {'author__a_name': '阿狗'}, {'author__a_name': '阿花'}]>
    #
    # # 查找书名是“番茄物语”的书的作者的年龄
    # ret = Book.objects.filter(title='番茄物语').values('author__age')
    # print(ret)  # <QuerySet [{'author__age': 34}, {'author__age': 23}, {'author__age': 234}, {'author__age': 45}]>
    # # 查找书名是“番茄物语”的书的作者的手机号码
    # ret = Book.objects.filter(title='番茄物语').values('author__phone')
    # print(ret)  # <QuerySet [{'author__phone': '12948573024'}, {'author__phone': '12847384950'}, {'author__phone': '19104857693'}, {'author__phone': '18923048576'}]>
    # # 查找书名是“番茄物语”的书的作者的地址
    # ret = Book.objects.filter(title='番茄物语').values('author__detail__addr')
    # print(ret)  # <QuerySet [{'author__detail__addr': '神经病医院三楼349号房203床'}, {'author__detail__addr': '神经病医院三楼350号房203床'}, {'author__detail__addr': '神经病医院三楼449号房203床'}, {'author__detail__addr': '神经病医院四楼349号房203床'}]>
    # # 查找书名是“番茄物语”的书的作者的邮箱
    # ret = Book.objects.filter(title='番茄物语').values('author__detail__email')
    # print(ret)  # <QuerySet [{'author__detail__email': '2@3.m'}, {'author__detail__email': '6@9.m'}, {'author__detail__email': '3@t.m'}, {'author__detail__email': 'd@w.m'}]>
    # ret = Book.objects.get(title='番茄物语').author.all()
    # for i in ret:
    #     print(i.detail.email)  #2@3.m  6@9.m  3@t.m  d@w.m

    from django.db.models import F, Q

    # 找到作者另一半的年龄比作者大的作者名
    ret = Author.objects.filter(companion_age__gt=F('age')).values('a_name')
    print(ret)
    # Q查询，满足条件的里面有一个 就可以，或
    # 查询作者名是麋鹿或燕子的书
    ret = Book.objects.filter(Q(author__a_name='麋鹿') | Q(author__a_name='燕子'))
    print(ret)  # <QuerySet [<Book: 西瓜物语>, <Book: 鸡蛋物语>]>

    # 查询作者名字是燕子并且不是2018年出版的书的书名
    ret = Book.objects.filter(Q(author__a_name='燕子') & ~Q(pub_date__year=2018)).values('title')
    print(ret)  # <QuerySet [{'title': '西瓜物语'}]>
    # 查询出版年份是2017或2018，书名中带瓜的所有书
    # ret = Book.objects.filter(Q(pub_date__year=2018)|Q(pub_date__year=2017),Q(title__contains='瓜'))
    ret = Book.objects.filter(Q(pub_date__year=2018)|Q(pub_date__year=2017),title__contains='瓜')
    print(ret)  # <QuerySet [<Book: 西瓜物语>, <Book: 冬瓜物语>]>
