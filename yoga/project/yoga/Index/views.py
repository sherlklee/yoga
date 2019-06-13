from django.shortcuts import render,HttpResponseRedirect
from Sessionmanager.sessionmanager import SessionManager
from Database.models import Customer,Course,Trainer

def index(request):
    sessionManager = SessionManager(request)
    username = ""
    course = Course.objects.filter(coursevalid=True).all()[:4]
    item = course[0]
    item1 = course[1]
    item2 = course[2]
    trainer = Trainer.objects.all()[:4]
    trainer0 = trainer[0]
    trainer1 = trainer[1]
    trainer2 = trainer[2]
    trainer3 = trainer[3]

    if sessionManager.Islogined():  # 如果是登陆状态，那么对应页面就应该显示登出
        username = sessionManager.Getusername()
        user = Customer.objects.get(username=username)
        if user.Isadmin():
            userid = "admin"
            return render(request, 'adminbase.html', locals())
        elif user.Istrainer():
            userid = "trainer"
            return render(request, 'trainerbase.html', locals())
        else:
            userid = "customer"
            print("ok")
            return render(request, 'customerbase.html',locals())
    else:  # 如果是未登录状态，那么对应页面就应该显示登陆或者注册
        userid = "none"
    return render(request, 'base.html', locals())  # 渲染页面