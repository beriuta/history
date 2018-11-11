import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day66.settings")

    import django
    django.setup()

    from applistions.models import MyClass, Student,Teacher,Comment

    # 1. 查询id=1学生的班级名称
    # 1.1 基于对象查询
    student_obj = Student.objects.get(id=1)
    ret = student_obj.myclass.c_name
    print(ret)  # 三年七班

    # 1.2 基于QuerySet查询
    student = Student.objects.filter(id=1).values_list('myclass__c_name')
    print(student)  # <QuerySet [('三年七班',)]>


    # 2. 查询名字是 何老师 所带的所有班级名称
    # 2.1 基于对象的查询
    teacher_obj = Teacher.objects.get(t_name='何老师')
    ret = teacher_obj.myclass.all()
    print(ret)  # <QuerySet [<MyClass: 三年七班>, <MyClass: 高一三班>, <MyClass: 初三六班>]>
    # 2.2 基于QuerySet查询
    ret = Teacher.objects.filter(t_name='何老师').values_list('myclass__c_name')
    print(ret)  # <QuerySet [('三年七班',), ('高一三班',), ('初三六班',)]>