import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysiste.settings")

    import django
    django.setup()

    from applistions.models import Student,MyClass,Teacher

    # 把赵老师的学生都删掉
    ret = Teacher.objects.filter(t_name='赵老师').values_list('my_class__student__id')  # 寻找老师表格里面的班级，从班级反向查找student的id
    print(ret)  # <QuerySet [(1,), (2,), (4,), (6,), (7,)]>
    # 列表推导式
    id_list = [i[0] for i in ret]
    print(id_list)  # [1, 2, 4, 6, 7]
    ret1 = Student.objects.filter(id__in=id_list)  # id__in意思是：id是否有在后面的那个列表里，如果有，则会打印出相应的名字
    print(ret1)  # <QuerySet [<Student: 远远>, <Student: 梦雨>, <Student: 兔子>, <Student: 鹿子>, <Student: 大象>]>
    # 最后删掉
    ret1.delete()