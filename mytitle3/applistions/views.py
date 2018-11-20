from django.shortcuts import render, HttpResponse, redirect
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from applistions.models import UserInfo, Hobby
from django import views
from django import forms


# Create your views here.
class IndexView(views.View):
    def get(self, request):
        return render(request, 'index.html')


def check_egg(value):
    if '鸡蛋' in value:
        raise ValidationError('鸡蛋不能多吃!')


# class FagForm(forms.Form):
#     name = forms.CharField(
#         max_length=12,
#         min_length=3,
#         label='用户名',
#         widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
#         validators=[check_egg, ]  # 设置敏感词汇
#     )
#     password = forms.CharField(
#         min_length=6,
#         label='密码',
#         widget=forms.widgets.PasswordInput(attrs={'type': 'password', 'class': 'form-control '}, render_value=True),
#         # 将html代码中的相应的input类型变成password
#         error_messages={'min_length': '密码长度最小6位'},
#     )
#     re_password = forms.CharField(
#         min_length=6,
#         label='确认密码',
#         widget=forms.widgets.PasswordInput(attrs={'type': 'password', 'class': 'form-control '}, render_value=True),
#         # 将html代码中的相应的input类型变成password
#         error_messages={'min_length': '密码长度最小6位'},
#     )
#     gender = forms.ChoiceField(
#         choices=((1, '男'), (2, '女'), (3, '保密'),),
#         label='性别',
#         initial=3,
#         widget=forms.widgets.RadioSelect()  # 生成一个redio标签
#     )
#     hobby = forms.fields.ChoiceField(
#         choices=((1, '篮球'), (2, '足球'), (3, '双色球'),),
#         label='爱好',
#         initial=3,
#         widget=forms.widgets.Select()
#     )
#     hobby2 = forms.fields.ChoiceField(
#         choices=((1, '篮球'), (2, '足球'), (3, '双色球'),),
#         label='爱好2',
#         initial=3,
#         widget=forms.widgets.SelectMultiple()
#     )
#     keep = forms.fields.ChoiceField(
#         label='是否记住密码',
#         initial='checked',
#         widget=forms.widgets.CheckboxInput()
#     )
#     hobby3 = forms.fields.MultipleChoiceField(
#         choices=((1, '篮球'), (2, '足球'), (3, '双色球'),),
#         label='爱好',
#         initial=[1, 3],
#         widget=forms.widgets.CheckboxSelectMultiple()
#     )
#     phone = forms.CharField(
#         label='手机号',
#         widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
#         validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号码不正确'), ]
#     )
#     # 自定义验证规则
#     title = forms.fields.CharField(
#         max_length=20,
#         error_messages={
#             'required': '标题不能为空',
#             'min_length': '标题最少为5个字符',
#             'max_length': '标题最多为20个字符',
#         },
#         widget=forms.widgets.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': '标题5-20个字符'
#         })
#     )
#
#     # 局部的钩子
#     def clean_name(self):
#         value = self.cleaned_data.get('name', '')
#         if '捣蛋鬼' in value:
#             raise ValidationError('不符合社会主义核心价值观')
#         else:
#             return value
#
#     # 全局的钩子
#     def clean(self):
#         # self.cleaned_data  --> 所有经过校验的数据
#         pwd = self.cleaned_data.get('password')
#         re_pwd = self.cleaned_data.get('re_password')
#         if pwd == re_pwd:
#             return self.cleaned_data
#         else:
#             self.add_error('re_password', '两次密码不一致')
#             raise ValidationError('两次密码不一致')
#
#     # 重写了__init__方法,每次手动更新hobby字段choice选项,因为QuerySet惰性查询的特性
#     def __init__(self, *args, **kwargs):
#         super(FagForm, self).__init__(*args, **kwargs)
#         self.fields['hobby'].choices = Hobby.objects.all().values_list('id', 'name')


def login(request):
    if request.method == 'POST':
        user = request.POST.get('name')
        pwd = request.POST.get('password')
        ret = UserInfo.objects.filter(username=user, password=pwd)
        print(ret)
        user_obj = ret.first()
        if user_obj:
            # 设置session
            request.session['user'] = user_obj.id
            return redirect('/index/')
    return render(request, 'login.html')


# # 使用form表单方式提交
def rag(request):
    if request.method == 'POST':
        # 把提交的数据直接放到form类中实例化
        form_obj = FagForm(request.POST)
        # 调用form模块的is_valid()方法
        # 如果校验通过,吧信息都保存在form_obj.cleaned_data属性
        # 如果校验不通过,就把错误信息保存在form_obj.errors属性
        if form_obj.is_valid():
            # 局部钩子
            # 全局钩子
            print(form_obj.cleaned_data)
            print('#' * 120)
            # 如果数据没有问题
            username = form_obj.cleaned_data.get('name')
            pwd = form_obj.cleaned_data.get('password')
            UserInfo.objects.create(username=username, password=pwd)
            return redirect('/login/')
        else:
            print(form_obj.errors, type(form_obj.errors))
            print('-' * 120)
            # 如果数据有问题
            return render(request, 'rag.html', {'form': form_obj})
    form_obj = FagForm()
    return render(request, 'rag.html', {'form': form_obj})

# 自己练习,form表单提交实现注册页面,用户名,用户密码,确认密码,邮箱,手机号
class FagForm(forms.Form):
    name = forms.CharField(
        max_length=12,
        min_length=3,
        label='用户名',
        error_messages={
            'max_length': '用户名长度不能超过12位',
            'min_length': '用户名长度不能短于3位',
        },
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        min_length=6,
        label='用户密码',
        error_messages={
            'max_length': '用户密码不能小于6位',
        },
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
    )
    re_password = forms.CharField(
        min_length=6,
        label='确认密码',
        error_messages={
            'max_length': '用户密码不能小于6位',
        },
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
    )
    email = forms.EmailField(
        label='邮箱',
        required=False,
        error_messages={
            'required': '邮箱不能为空',
            'invalid': '邮箱格式错误',
        },
        widget=forms.widgets.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': '邮箱'
        })
    )
    phone = forms.CharField(
        label='手机号码',
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
        validators=[RegexValidator(r'1[3-9]\d{9}$', '手机号码不正确'), ]
    )

    # 全局的钩子,校验两次密码的一致性

    def clean(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd == re_pwd:
            return self.cleaned_data
        else:
            self.add_error('re_password', '密码输入不一致')
            return ValidationError('两次密码不一致')


def test(request):
    form_obj = FagForm(request.POST)
    if form_obj.is_valid():
        user = form_obj.cleaned_data.get('name')
        pwd = form_obj.cleaned_data.get('password')
        UserInfo.objects.create(username=user, password=pwd)
        return redirect('/login/')
    else:
        return render(request, 'test.html', {'form': form_obj})
    return render(request, 'test.html')
