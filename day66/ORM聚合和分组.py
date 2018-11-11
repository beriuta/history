import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day66.settings")

    import django
    django.setup()

    from applistions.models import MyClass,Student,Teacher,Employee
    from django.db.models import Avg, Sum, Max, Min, Count

    # 1.求所有人里面工资最高的
    ret = Employee.objects.all().aggregate(Max('salary'))
    print(ret)  # {'salary__max': 80909}

    # # 指定返回字典中key的值
    ret = Employee.objects.all().aggregate(max_salary=Max('salary'))
    print(ret)  # {'max_salary': 80909}

    # # 求所有人的平均价格
    ret = Employee.objects.all().aggregate(Avg('salary'))
    print(ret)  # {'salary__avg': 20855.1667}

    # 使用ORM查询每个部门的平均工资
    ret = Employee.objects.values('dept').aggregate(Avg('salary'))
    print(ret)  # 查询的是每个人的平均工资，此条查询错误
    # annotate中要写上分住之后要做的事情
    # anntate前面查询的是什么就按什么分组
    ret = Employee.objects.values('dept').annotate(Avg('salary')).values_list('dept','salary__avg')
    print(ret)  # <QuerySet [('财务部', 2111.0), ('技术部', 17000.0), ('人事部', 6000.0), ('管理部', 80909.0)]>

    # # ORM中分组使用annotate
    # # 1. annotate中要写上分组之后要做的事情
    # # 2. annotate前面查询的是什么就按什么分组
    # ret = Employee.objects.values('dept').annotate(avg_price=Avg('salary')).values('dept', 'avg_price')
    # print(ret)
    #
    # # 每个部门的平均年龄
    ret = Employee.objects.values('dept').annotate(avg_age=Avg('age')).values_list('dept','avg_age')
    print(ret)  # <QuerySet [('财务部', 27.5), ('技术部', 300.0), ('人事部', 45.0), ('管理部', 45.0)]>

    # # 求每个班级的学生的数量
    ret = Student.objects.values('myclass').annotate(s_count=Count('id'))
    print(ret)  # <QuerySet [{'myclass': 1, 's_count': 1}, {'myclass': 2, 's_count': 3}, {'myclass': 3, 's_count': 2}, {'myclass': 4, 's_count': 1}, {'myclass': 5, 's_count': 1}, {'myclass': 6, 's_count': 1}, {'myclass': 7, 's_count': 1}]>
