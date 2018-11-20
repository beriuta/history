from django import forms
from crm.models import UserProfile
from django.core.exceptions import ValidationError


class RegForm(forms.ModelForm):
    # class Meta:
    #     fields = '__all__'
    re_password = forms.CharField(
        label='确认密码',
        widget=forms.widgets.PasswordInput(),
    )

    class Meta:  # 类的配置信息
        model = UserProfile  # 告诉django绑定的类是哪个
        fields = ['email', 'password', 're_password', 'name', 'mobile']
        # 按顺序展示列表中列出来的字段
        # exclude = ['']  # 把不需要展示的字段排除,展示剩下的字段
        labels = {
            'email':'邮箱'
        }
        error_messages = {
            'password':{
                'min-length':'密码最短8位',
            }
        }
        widgets = {
            'password':forms.widgets.PasswordInput(),
            're_password':forms.widgets.PasswordInput()
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields.values())
        for field in self.fields.values():
            field.widget.attr.update({'class':'form-control'})

    def clean_email(self):  # 局部钩子
        email_value = self.cleaned_data.get('email')
        is_exist = UserProfile.objects.filter(email=email_value)
        if is_exist:
            raise ValidationError('邮箱已被注册')
        else:
            return email_value

    def clean(self):
        pwd_value = self.cleaned_data.get('password')
        re_pwd_value = self.cleaned_data.get('re_password')
        if pwd_value == re_pwd_value:
            return self.cleaned_data
        else:
            self.add_error('re_password','两次密码是不一样')
            raise ValidationError('两次密码不一致')