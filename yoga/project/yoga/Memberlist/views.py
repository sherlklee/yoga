from django.shortcuts import render, HttpResponseRedirect
from Database.models import Customer ,Customerinformation, Trainer
from Sessionmanager.sessionmanager import SessionManager
from django.db.models import Q


def membermessage(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    username = sessionManager.Getusername()
    if sessionManager.Isadministrator():  # 如果是管理员登陆
        userid = 'admin'
    else:  # 如果是客户登陆
        return HttpResponseRedirect("/")
    if request.method == "POST":
        search = request.POST.get("search")
        if search:
            user_list = Customerinformation.objects.filter(Q(username__contains=search) | Q(name__contains=search))
        else:
            user_list = Customerinformation.objects.all()
    else:
        user_list = Customerinformation.objects.all()
    return render(request, 'customerinformation.html', locals())

def membermessagetime(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    username = sessionManager.Getusername()
    if sessionManager.Isadministrator():  # 如果是管理员登陆
        userid = 'admin'
    else:  # 如果是客户登陆
        return HttpResponseRedirect("/")
    if request.method == "POST":
        search = request.POST.get("search")
        if search:
            user_list = Customerinformation.objects.filter(Q(username__contains=search) | Q(name__contains=search))
        else:
            user_list = Customerinformation.objects.order_by("username").reverse()
    else:
        user_list = Customerinformation.objects.order_by("username").reverse()
    return render(request, 'customerinformationtime.html', locals())


def membermessagedetail(request, username):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if sessionManager.Isadministrator():  # 如果是管理员登陆
        userid = 'admin'
    else:  # 如果是客户登陆
        return HttpResponseRedirect("/")
    return render(request, 'customerdetail.html', locals())


def trainermessage(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    username = sessionManager.Getusername()
    if sessionManager.Isadministrator():  # 如果是管理员登陆
        userid = 'admin'
    else:  # 如果是客户登陆
        return HttpResponseRedirect("/")
    if request.method == "POST":
        search = request.POST.get("search")
        if search:
            user_list = Trainer.objects.filter(Q(username__contains=search) | Q(name__contains=search))
        else:
            user_list = Trainer.objects.all()
    else:
        user_list = Trainer.objects.all()
    return render(request, 'trainerinformation.html', locals())