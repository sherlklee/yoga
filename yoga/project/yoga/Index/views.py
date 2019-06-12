from django.shortcuts import render,HttpResponseRedirect
from Sessionmanager.sessionmanager import SessionManager
from Database.models import Customer

def index(request):
    sessionManager = SessionManager(request)
    username = ""
    if sessionManager.Islogined():  # 如果是登陆状态，那么对应页面就应该显示登出
        username = sessionManager.Getusername()
        user = Customer.objects.get(username=username)
        if user.Isadmin():
            userid = "admin"
        elif user.Istrainer():
            userid = "trainer"
        else:
            userid = "customer"
    else:  # 如果是未登录状态，那么对应页面就应该显示登陆或者注册
        userid = "none"
    return render(request, 'base.html', {"userid": userid,"username":username} )  # 渲染页面

def indextemp(request):
    return render(request,"basemanager.html",locals())