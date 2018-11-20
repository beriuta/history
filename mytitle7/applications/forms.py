from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from applications.models import GENDER_CHOICES,DEFAULT_GENDER,UserInfo


class RegForm(forms.Form):
    username = forms.CharField(
        max_length=12,
        min_length=3,
        label='用户名',
        widget=forms.widgets.TextInput()
    )
    password = forms.CharField(
        max_length=20,
        min_length=6,
        label='密码',
        widget=forms.widgets.PasswordInput()
    )
    re_password = forms.CharField(
        max_length=20,
        min_length=6,
        label='确认密码',
        widget=forms.widgets.PasswordInput()
    )
    phone = forms.CharField(
        max_length=11,
        min_length=11,
        label='手机号码',
        widget=forms.widgets.TextInput(),
        validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号码格式不正确')]
    )
    email = forms.CharField(
        label='邮箱',
        widget=forms.widgets.EmailInput(),
        validators=[RegexValidator(r'[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$','邮箱格式不正确')]
    )
    gender = forms.ChoiceField(
        label='性别',
        widget=forms.widgets.RadioSelect(),
        choices=GENDER_CHOICES,
        initial=DEFAULT_GENDER,
    )

    # 验证用户名是否存在的局部钩子
    def clean_name(self):
        name_value = self.cleaned_data.get('phone')
        is_exist = UserInfo.objects.filter(username=name_value)
        if is_exist:
            raise ValidationError('用户名已存在')
        return name_value

    # 局部钩子,校验手机号码是否存在
    def clean_phone(self):
        phone_value = UserInfo.objects.get('phone')
        is_exist = UserInfo.objects.filter(phone=phone_value)
        if is_exist:
            raise ValidationError('手机号码已存在')
        return phone_value

    def clean(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd == re_pwd:
            return self.cleaned_data  # 明确返回
        else:
            self.add_error('re_password', '历史那个词密码是不一致')
            raise ValidationError('两次密码不一致')

    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):  # 迭代器
            print(field,type(self.fields))
            if field == 'gender':
                continue
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control'
                }
            )











