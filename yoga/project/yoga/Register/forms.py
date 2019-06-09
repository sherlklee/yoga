from django import forms
from Database.models import Customer
from django.core.exceptions import ValidationError, ObjectDoesNotExist


class RegisterForm(forms.Form):  # 登录时输入的表单
    username = forms.CharField(label='用户名', widget=forms.TextInput, min_length=5, max_length=20)  # 用户名框
    password = forms.CharField(label='密 码', widget=forms.PasswordInput, min_length=6, max_length=20)  # 密码框
    confirmPassword = forms.CharField(label="确认密码", widget=forms.PasswordInput,min_length=6, max_length=20)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        user = Customer()  # 创建空用户对象
        flag = True
        try:
            user = Customer.objects.get(username=username)  # 尝试查询该用户
        except ObjectDoesNotExist:  # 用户名不存在，执行创建操作
            flag = False
        if flag:
            raise ValidationError("此用户名已存在")

