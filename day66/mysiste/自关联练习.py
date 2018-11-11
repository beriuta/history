"""
这是一个评论的层级例子
"""

import os


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysiste.settings")

    import django
    django.setup()

    from applition1.models import Comment
    from applistions.models import MyClass,Student,Teacher

    # 查找id=2的评论的所有子评论
    ret = Comment.objects.filter(p_comment=2)
    print(ret)  # <QuerySet [<Comment: 我是评论二层的子评论>, <Comment: 我是评论二层的评论2>]>

    # 查找id=2班级的所有学生
    ret = Student.objects.filter(my_class__id=2)
    print(ret)  # <QuerySet [<Student: 白白>, <Student: 狗子>]>

    # 默认不支持反向查找，需要在ManyToMany字段中设置symmetrical=False
