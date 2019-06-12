from django import forms
from Database import models
class ClassroomForm(forms.ModelForm):  #完善个人信息时提交的表单
    class Meta:
        model = models.Classroom
        exclude = ['classroomid' ]
        labels = {
            'classroomname': '教室名',
            'note': '备注',
            'maxpersonnumber': '容纳人数',
        }
        error_messages = {
            '_all_':{
                'required':'请输入内容',
                'invaild':'请检查输入的内容'
            }
        }
