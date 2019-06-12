from django import forms
from Database import models
class CompleteForm(forms.ModelForm):  #完善个人信息时提交的表单
    class Meta:
        model = models.Customerinformation
        exclude = [ 'username' ]
        labels = {
            'name ': '姓名',
            'phone': '电话',
            'birthday': '生日',
            'profession': '职业',
            'sex': '性别',
            'height':'身高',
            'weight':'体重',
            'bust' : '胸围',
            'waistline':'腰围',
            'hipline':'臀围',
            'hipline':'臀围',
            'shoulderwidth':'肩宽'
        }
        help_texts ={
            'birthday': 'yyyy-mm-dd'
        }
        error_messages = {
            '_all_':{
                'required':'请输入内容',
                'invaild':'请检查输入的内容'
            }
        }