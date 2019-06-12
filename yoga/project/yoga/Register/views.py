from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import RegisterForm
from Database.models import Customer , Customerinformation,Trainerinformation
from Sessionmanager.sessionmanager import SessionManager

#会员注册
def register(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogined():
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            username = registerForm.cleaned_data.get('username')
            password = registerForm.cleaned_data.get('password')
            Customer.objects.create(username=username, password=password)
            customerInformation = Customerinformation.objects.create(username=username)
            return HttpResponseRedirect("/login")
    else:
        registerForm = RegisterForm()
    return render(request, "RegisterUI.html", {'registerForm': registerForm})

#教练注册
def trainerregister(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    userid = "admin"
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            username = registerForm.cleaned_data.get('username')
            password = registerForm.cleaned_data.get('password')
            Customer.objects.create(username=username, password=password, identity="trainer")
            customerInformation = Trainerinformation.objects.create(username=username)
            return HttpResponse("注册成功")
    else:
        registerForm = RegisterForm()
    return render(request, "RegisterUI.html", locals())