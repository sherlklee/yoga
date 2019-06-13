from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import RegisterForm
from Database.models import Customer,Customerinformation,Trainer
from Sessionmanager.sessionmanager import SessionManager

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
            personalInformation = Customerinformation.objects.create(username=username)
            return HttpResponseRedirect("/login/")
    else:
        registerForm = RegisterForm()
    return render(request, "RegisterUI.html", locals())


def trainerregister(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    username=sessionManager.Getusername()
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            username = registerForm.cleaned_data.get('username')
            password = registerForm.cleaned_data.get('password')
            Customer.objects.create(username=username, password=password, identity='trainer')
            TrainerInformation = Trainer.objects.create(username=username)
            return HttpResponseRedirect("/login/")
    else:
        registerForm = RegisterForm()
    return render(request, "trainerregister.html", locals())