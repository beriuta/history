from rest_framework import serializers
from SerDemo.models import Book


#
# class PublisherSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=32)
#
#
# class AuthorSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=32)
#
#
# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=32)
#     CHOICES = ((1, "python"), (2, "linux"), (3, "go"))  # 种类
#     category = serializers.ChoiceField(choices=CHOICES, read_only=True)
#     post_category = serializers.IntegerField(write_only=True)  # post反序列化的时候只传序号
#     pub_time = serializers.DateField()
#     publisher = PublisherSerializer(read_only=True)  # 获取的是id
#     authors = AuthorSerializer(many=True, read_only=True)  # 获取的是列表
#
#     publisher_id = serializers.IntegerField(write_only=True)  # post反序列化的时候校验这个字段
#     authors_list = serializers.ListField(write_only=True)
#
#     # 构建单个字段的校验
#     def validate_title(self, value):
#         # title必须含有"鬼鬼"
#         if "鬼鬼" in value.lower():
#             return value
#         raise serializers.ValidationError('输入的书名不合法')
#
#     # 构建多个字段的校验
#     def validate(self, attrs):
#         # attrs是前端传来的所有的数据组成的字典
#         if '嘻嘻' in attrs['title'] and attrs['post_category'] == 1:
#             return attrs
#         raise serializers.ValidationError('输入的图书名字或者分类不合法')
#
#     def create(self, validated_data):
#         # 需要自己创建create和update方法,create是更新全部的,而update是更新局部,用在修改数据上面
#         # 通过ORM给数据库创建数据
#         book_obj = Book.objects.create(
#             title=validated_data['title'],
#             category=validated_data['post_category'],
#             pub_time=validated_data['pub_time'],
#             publisher=validated_data['publisher_id'],
#                                        )
#         book_obj.authors.add(*validated_data['authors_list'])  # 因为作者表跟书籍表是多对多关系,所以需要打散传进去
#         return book_obj
#
#     def update(self, instance, validated_data):
#         # 此时的instance就是传进来的book_obj
#         instance.title = validated_data.get('title',instance.title)
#         instance.category = validated_data.get('post_category',instance.category)
#         instance.pub_time = validated_data.get('pub_time',instance.pub_time)
#         instance.publisher = validated_data.get('publisher_id',instance.publisher)
#         if validated_data.get('authors_list',False):
#             instance.authors.set(validated_data['authors_list'])
#             instance.save()
#         return instance
#
#
#
# # 构建自定义的字段校验,
# def my_validate(value):
#     if "我是测试" in value.lower():
#         raise serializers.ValidationError('输入的内容含有敏感词汇')
# # 搭建的自定义字段校验要放在想要校验的字段中
# # 比如:title = serializers.CharField(max_length=32,validators=[my_validate])

# ----------------- 以上是继承了Serializer这个类,需要自己写每个字段--------------
# ----------------- 以下是继承ModelSerializer这个类,不需要自己写每个字段--------------

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['title','pub_time'...]  # 需要校验的字段写在里面
        # exclude = ['title','pub_time'...]  # 需要过滤掉的字段写在里面
        # depath = 1  # 内置的一个参数,可以深入的层数是给的数字,但是会把所有的字段都默认添加上read_only = True这个参数
        extra_kwargs = {
            "category": {'write_only': True},
            "publisher": {'write_only': True},
            "authors": {'write_only': True}
        }

    category_text = serializers.SerializerMethodField(read_only=True)
    # SerializerMethodField默认会调用此类的钩子方法,钩子方法的返回值返回给这个字段
    publisher_info = serializers.SerializerMethodField(read_only=True)
    authors_info = serializers.SerializerMethodField(read_only=True)

    # 所找的钩子方法是get_字段名称,传入的是obj,是序列化每个模型的对象

    def get_category_text(self, obj):
        return obj.get_category_display()

    def get_publisher_info(self, obj):
        return {'id': obj.publisher.id, 'title': obj.publisher.title}

    def get_authors_info(self, obj):
        return [{'id': author.id, 'name': author.name} for author in obj.authors.all()]
