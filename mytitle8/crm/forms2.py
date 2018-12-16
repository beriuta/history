from django import forms
from crm.models import UserProfile, Campuses, Customer, ConsultRecord,Enrollment,ClassList,CourseRecord,StudyRecord
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
            'email': '邮箱'
        }
        error_messages = {
            'password': {
                'min-length': '密码最短8位',
            }
        }
        widgets = {
            'password': forms.widgets.PasswordInput(),
            're_password': forms.widgets.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields.values())
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_email(self):  # 局部钩子
        email_value = self.cleaned_data.get('email')
        is_exist = UserProfile.objects.filter(email=email_value)
        print(is_exist)
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
            self.add_error('re_password', '两次密码是不一样')
            raise ValidationError('两次密码不一致')


class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'course': forms.widgets.SelectMultiple,
            'birthday': forms.widgets.DateInput(attrs={'type': 'date'})
        }


# 沟通记录的form
class ConsultRecordForm(forms.ModelForm):
    class Meta:
        model = ConsultRecord
        exclude = ['delete_status']  # 除去中括号里的字段,别的字段都显示

    def __init__(self, *args, **kwargs):
        super(ConsultRecordForm, self).__init__(*args, **kwargs)
        self.fields['customer'] = forms.models.ModelChoiceField(
            queryset=Customer.objects.filter(consultant=self.instance.consultant))
        self.fields['customer'].widget.attrs.update({'class': 'form-control'})


# 报名表
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        exclude = ['contract_approved', 'delete_status']

    def __init__(self, *args, **kwargs):
        super(EnrollmentForm, self).__init__(*args, **kwargs)
        # 限制添加报名表的时候只能选自己的私户
        print(self.instance)
        self.fields['customer'].choices = [(self.instance.customer.id, self.instance.customer.name)]


# 班级表
class ClassListForm(forms.ModelForm):
    class Meta:
        model = ClassList
        fields = '__all__'


# 课程记录表
class CourseRecordForm(forms.ModelForm):
    class Meta:
        model = CourseRecord
        fields = '__all__'


# 学习记录表
class StudyRecordForm(forms.Form):
    class Meta:
        model = StudyRecord
        fields = ['student', 'attendance', 'score', 'homework_note']
