import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysiste.settings")

    import django
    django.setup()
    from applistions.models import MyClass,Student,Teacher

    # 1. 查询id=2的班级的所有学生
    # ret = Student.objects.filter(my_class__id=2)
    # print(ret)  # <QuerySet [<Student: 白白>, <Student: 狗子>]>
    #
    # # 2. 查询id=2的班级的所有老师
    # ret = Teacher.objects.filter(my_class__id=2)
    # print(ret)  # <QuerySet [<Teacher: 袁老师>, <Teacher: 辛老师>]>
    # 给id=1的班级添加一个id=5的学生
    # ret = MyClass.objects.get(id=1).student_set.all()
    # print(ret)  # <QuerySet [<Student: 远远>, <Student: 梦雨>]>

    # 先找到id=5的那个学生
    # ret = Student.objects.get(id=5)
    # print(ret)  # 狗子
    # 把id=5的学生添加到id=1的班级的学生列表中
    # MyClass.objects.get(id=1).student_set.add(ret)
    # 把所有的学生都绑定到id=1的班级中


    # 给id=2的老师添加一个id=3的新班级
    # ret = MyClass.objects.get(id=2).teacher_set.add(Teacher.objects.get(id=2))  # 错误
    # Teacher.objects.get(id=2).my_class.add(2)
    # id=2的老师被开除了(把id=2的老师关联的班级都清空)
    # 把id=2的老师不带2班
    # Teacher.objects.get(id=2).my_class.get(id=2).delete()  # 错误,把id=2的班级都删除了
    # 让id=3的老师不带id=4的班级
    # Teacher.objects.get(id=3).my_class.remove(4)
    # id=2的老师现在要带一门新课：生理课
    # 1. 先创建了一个生理课 的班级
    # MyClass.objects.create(c_name='生理课')
    # 2. 把上一步创建的班级和id=2的老师绑定起来
    # Teacher.objects.get(id=2).my_class.create(c_name='生理课')
    ret = Teacher.objects.get(id=2).my_class.all()
    print(ret)  # <QuerySet [<MyClass: 三年五班>, <MyClass: 初三六班>, <MyClass: 初三七班>, <MyClass: 生理课>, <MyClass: 生理课>]>
