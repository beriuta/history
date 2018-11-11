import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day66.settings")

    import django
    django.setup()

    from applistions.models import MyClass,Teacher,Student,Comment,Employee
    from django.db.models import Avg, Sum, Max, Min, Count

    # 查找姓名是小猪并且在三年七班的同学
    ret = Student.objects.filter(s_name='小猪',myclass__c_name='三年七班')
    print(ret)  # <QuerySet [<Student: 小猪>]>

    # 查找姓名是小猪的同学
    ret = Student.objects.filter(s_name='小猪')
    print(ret)  # <QuerySet [<Student: 小猪>, <Student: 小猪>]>


    # 1. 查找书的价格大于100块或者作者里有小明的书并且这些书id都要大于3
    # Q查询
    from django.db.models import Q
    # Book.objects.filter(Q=('price__gt'=100) | Q=(author__name='小明'),id__gt=3)
    # 如果Q查询和关键字查询都存在，关键字查询必须放在Q查询的后面


    # 给所有书的价格加上20块
    # F用来在字段原来值的基础上做操作
    # from django.db.models import F
    # Book.objects.all().update(price=F('price')+20)
