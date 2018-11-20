from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class RegForm(forms.Form):
    email = forms.EmailField(
        label='邮箱',
        widget=forms.widgets.EmailInput(attrs={'class': 'form-control'}),
    )
    name = forms.CharField(
        max_length=12,
        min_length=3,
        label='用户名',
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        min_length=6,
        label='密码',
        widget=forms.widgets.PasswordInput(attrs={'type': 'password', 'class': 'form-control'})
    )
    re_password = forms.CharField(
        min_length=6,
        label='确认密码',
        widget=forms.widgets.PasswordInput(attrs={'type': 'password', 'class': 'form-control'})
    )

    # 全局的钩子
    def clean(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd == re_pwd:
            return self.cleaned_data
        else:
            self.add_error('re_password', '两次密码不一致')
            raise ValidationError('两次密码不一致')