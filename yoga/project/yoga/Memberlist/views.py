from django.shortcuts import render, HttpResponseRedirect
from Database.models import Customer ,Customerinformation, Trainerinformation
from Sessionmanager.sessionmanager import SessionManager

def membermessage(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if sessionManager.Isadministrator():  # 如果是管理员登陆
        userid = 'admin'
    else:  # 如果是客户登陆
        return HttpResponseRedirect("/")
    user_list = Customerinformation.objects.all()
    return render(request, 'customerinformation.html', locals())

def trainermessage(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if sessionManager.Isadministrator():  # 如果是管理员登陆
        userid = 'admin'
    else:  # 如果是客户登陆
        return HttpResponseRedirect("/")
    user_list = Trainerinformation.objects.all()
    return render(request, 'trainerinformation.html', locals())