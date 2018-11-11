import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mymodel.settings')

    import django

    django.setup()

    from applistions.models import UserInfo, Site

    ret = UserInfo.objects.all()
    print(
        ret)  # <QuerySet [<UserInfo: UserInfo object>, <UserInfo: UserInfo object>, <UserInfo: UserInfo object>, <UserInfo: UserInfo object>, <UserInfo: UserInfo object>, <UserInfo: UserInfo object>]>
    # 找到名字是韩蕾的那个人
    ret = UserInfo.objects.filter(name='韩蕾')
    print(ret)  #<QuerySet [<UserInfo: UserInfo object>]>
    # 排除名字是阿里的那个人
    ret = UserInfo.objects.exclude(name='阿里')
    print(ret)  # <QuerySet [<UserInfo: UserInfo object>, <UserInfo: UserInfo object>, <UserInfo: UserInfo object>, <UserInfo: UserInfo object>, <UserInfo: UserInfo object>]>

    # values:返回的是列表，列表中不是对象而是字典
    ret1 = UserInfo.objects.all().values('name','gender','birthday')
    print(ret1)  # <QuerySet [{'name': '韩蕾', 'gender': 2, 'birthday': datetime.datetime(2012, 11, 6, 13, 57, 32, 632000, tzinfo=<UTC>)}, {'name': '阿里', 'gender': 1, 'birthday': datetime.datetime(2017, 11, 6, 13, 57, 57, 219000, tzinfo=<UTC>)}, {'name': '宣贯', 'gender': 3, 'birthday': datetime.datetime(1997, 11, 6, 13, 58, 17, 613000, tzinfo=<UTC>)}, {'name': '为止', 'gender': 1, 'birthday': datetime.datetime(2006, 11, 6, 23, 32, 42, 262000, tzinfo=<UTC>)}, {'name': '为袁', 'gender': 2, 'birthday': datetime.datetime(2014, 11, 6, 4, 59, 13, 239000, tzinfo=<UTC>)}, {'name': '原为', 'gender': 2, 'birthday': datetime.datetime(2018, 7, 6, 13, 59, 37, 578000, tzinfo=<UTC>)}]>

    # values_list:
    ret = UserInfo.objects.all().values_list('name','gender','birthday')
    print(ret)  # <QuerySet [('韩蕾', 2, datetime.datetime(2012, 11, 6, 13, 57, 32, 632000, tzinfo=<UTC>)), ('阿里', 1, datetime.datetime(2017, 11, 6, 13, 57, 57, 219000, tzinfo=<UTC>)), ('宣贯', 3, datetime.datetime(1997, 11, 6, 13, 58, 17, 613000, tzinfo=<UTC>)), ('为止', 1, datetime.datetime(2006, 11, 6, 23, 32, 42, 262000, tzinfo=<UTC>)), ('为袁', 2, datetime.datetime(2014, 11, 6, 4, 59, 13, 239000, tzinfo=<UTC>)), ('原为', 2, datetime.datetime(2018, 7, 6, 13, 59, 37, 578000, tzinfo=<UTC>))]>

    # order_by('XX')  根据xx排序
    ret1 = UserInfo.objects.order_by('id')
    ret2 = UserInfo.objects.order_by('-birthday')
    print(ret1)  # <QuerySet [<UserInfo: <userInfo韩蕾>>, <UserInfo: <userInfo阿里>>, <UserInfo: <userInfo宣贯>>, <UserInfo: <userInfo为止>>, <UserInfo: <userInfo为袁>>, <UserInfo: <userInfo原为>>]>
    print(ret2)  # <QuerySet [<UserInfo: <userInfo原为>>, <UserInfo: <userInfo阿里>>, <UserInfo: <userInfo为袁>>, <UserInfo: <userInfo韩蕾>>, <UserInfo: <userInfo为止>>, <UserInfo: <userInfo宣贯>>]>
    ret3 = UserInfo.objects.order_by('-birthday').reverse()
    print(ret3)  # <QuerySet [<UserInfo: <userInfo宣贯>>, <UserInfo: <userInfo为止>>, <UserInfo: <userInfo韩蕾>>, <UserInfo: <userInfo为袁>>, <UserInfo: <userInfo阿里>>, <UserInfo: <userInfo原为>>]>

    # count:返回数据数量
    ret1 = UserInfo.objects.all().count()
    print(ret1)  # 6

    # frist()和last()  -->返回的是具体的对象
    ret1 = UserInfo.objects.first()
    ret2 = UserInfo.objects.last()
    print(ret1)  # <userInfo韩蕾>  第一个
    print(ret2)  # <userInfo原为>  最后一个

    # exists  -->判断表中是否有数据，返回的是布尔值
    ret1 = UserInfo.objects.exists()
    ret2 = Site.objects.exists()
    print(ret1)  # True
    print(ret2)  # False

    # 单表查询之神奇的双下划线
    # 1.查询id值小于3的userinfo
    ret = UserInfo.objects.filter(id__lt=3)
    print(ret)  # <QuerySet [<UserInfo: <userInfo韩蕾>>, <UserInfo: <userInfo阿里>>]>
    # 2.查询id值大于等于3的userinfo
    ret = UserInfo.objects.filter(id__gte=3)
    print(ret)  # <QuerySet [<UserInfo: <userInfo宣贯>>, <UserInfo: <userInfo为止>>, <UserInfo: <userInfo为袁>>, <UserInfo: <userInfo原为>>]>
    # 3. 查询id值给定列表的那些user
    ret = UserInfo.objects.filter(id__in=[1,3,5])
    print(ret)  # <QuerySet [<UserInfo: <userInfo韩蕾>>, <UserInfo: <userInfo宣贯>>, <UserInfo: <userInfo为袁>>]>
    # 4.查询name中为的人
    ret = UserInfo.objects.filter(name__contains='为')
    print(ret)  # <QuerySet [<UserInfo: <userInfo为止>>, <UserInfo: <userInfo为袁>>, <UserInfo: <userInfo原为>>]>
    # 5. 查询name中以为结尾的人
    ret = UserInfo.objects.filter(name__endswith='为')
    print(ret)  # <QuerySet [<UserInfo: <userInfo原为>>]>
    # 6.找到7月出生的
    ret = UserInfo.objects.filter(birthday__month=7)
    print(ret)  # <<QuerySet [<UserInfo: <userInfo原为>>]>  注意：要在settings.py中设置USE_TZ = False
    # 7.找到1997年出生的
    ret = UserInfo.objects.filter(birthday__year=1997)
    print(ret)  # <QuerySet [<UserInfo: <userInfo宣贯>>]>