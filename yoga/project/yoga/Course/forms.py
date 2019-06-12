from django import forms
from Database import models
class CourseForm(forms.Form):  # 登录时输入的表单
    coursename = forms.CharField(label='课程名', widget=forms.TextInput, max_length=20)
    introduction = forms.CharField(label='简介', widget=forms.TextInput, max_length=100)
    trainer = forms.CharField(label='教练', widget=forms.TextInput, max_length=20)
    courseprice = forms.FloatField(label='价格', min_value=0, max_value=9999, initial=0)

