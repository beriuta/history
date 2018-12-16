from rest_framework import serializers
from applistions.models import Student

CHOICES = ((1, '男'), (2, '女'))


class TeacherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    t_name = serializers.CharField(max_length=32)  # 只序列化这里的字段,匹配的上留下,匹配不上的丢弃
    # sex = serializers.ChoiceField(choices=CHOICES)
    sex = serializers.CharField(source='get_sex_display',
                                read_only=True)  # source是资源后面可跟ORM的操作,read_only=True表示这个参数值正序用
    post_sex = serializers.IntegerField(write_only=True)  # write_only这个参数决定这个字段只反序用


class ClassSerializer(serializers.Serializer):
    c_name = serializers.CharField(max_length=32)
    teacher = TeacherSerializer(many=True, read_only=True)  # many=True是因为老师跟班级是多对多的关系,所以是多个
    # post_teacher = serializers.ListField(write_only=True)


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)  # required=False表示这个字段不需要做校验,因为如果是新增的,是没有id这个字段的
    name = serializers.CharField(max_length=32)
    age = serializers.IntegerField()
    student_id = serializers.IntegerField()
    c_num = ClassSerializer(read_only=True)
    c_post_num = serializers.ListField(write_only=True)

    def create(self, validated_data):
        # 通过ORM操作给Student表增加数据
        print(validated_data)  # 验证通过的数据就是前端传过来的数据
        print('8' * 120)
        student_obj = Student.objects.create(
            name=validated_data['name'],
            age=validated_data['age'],
            student_id=validated_data['student_id'],
            # c_num=validated_data['c_post_num'],
        )
        print(validated_data['c_post_num'], type(validated_data['c_post_num']))
        print(student_obj.c_num)
        print('-' * 120)
        student_obj.c_num.add(*validated_data['c_post_num'])  # 因为是多对多关系,所以需要add

        return student_obj
