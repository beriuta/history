import os
if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mystest.settings")

    import django
    django.setup()
    from applistions.models import Book,Author,AuthorInfo,Publisher
    # 外键
    # 1. 基于QuerySet的正向查找
    # 查询第一本书关联的出版社名称, 两个连续的双下划线表示跨表
    ret = Book.objects.filter(id=11).values('publisher__p_name')
    print(ret)  # <QuerySet [{'publisher__p_name': '西里出版社'}]>
    # 2.
    # 基于QuerySet的反向查找
    # 查询id=1的出版社出版的所有书的名称和价格
    ret = Publisher.objects.filter(id=1).values_list('books__b_name','books__price')
    print(ret)  # <QuerySet [('神经学科', Decimal('23.00')), ('艺术素养', Decimal('232.35'))]>

    # 一对一基于QuerySet跨表查询
    # 1. 查询id=1的作者婚否
    ret = Author.objects.filter(id=1).values_list('info__is_mary')
    print(ret)  # <QuerySet [(True,)]>
    # 2. 查找住在深圳的那个作者的姓名
    ret = AuthorInfo.objects.filter(city='深圳').values_list('author__a_name')
    print(ret)  # <QuerySet [('小明',)]>

    # 多对多基于QuerySet查询
    # 1. 查询id=1的作者关联的所有书籍的名称和价格
    ret = Author.objects.filter(id=1).values_list('books__b_name','books__price')
    print(ret)  # <QuerySet [('科技技术', Decimal('45.78'))]>
    # 2. 查找id=11的书的作者的名字
    ret = Book.objects.filter(id=11).values_list('authors__a_name')
    print(ret)  # <QuerySet [('小红',)]>
    # 3. 找id=11的书的作者的生日和城市
    ret =  Book.objects.filter(id=11).values_list('authors__info__birthday','authors__info__city')
    print(ret)  # <QuerySet [(datetime.date(2012, 9, 18), '上海')]>