from django import forms
from Database import models
class TrainerForm(forms.ModelForm):  #完善个人信息时提交的表单
    class Meta:
        model = models.Trainer
        exclude = [ 'username' ]
        labels = {
            'name ': '姓名',
            'phone': '电话',
            'age': '年龄',
            'professionaltitle': '职称',
            'sex': '性别',
            'introduction': '自我简介',
            'photo': '照片',
        }
        error_messages = {
            '_all_': {
                'required': '请输入内容',
                'invaild': '请检查输入的内容'
            }
        }