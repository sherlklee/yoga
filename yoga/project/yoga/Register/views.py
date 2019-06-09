from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .forms import RegisterForm
from Database.models import Customer
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
            # personalInformation = PersonalInformation.objects.create(username=username)
            return HttpResponseRedirect("/login")
    else:
        registerForm = RegisterForm()
    return render(request, "RegisterUI.html", {'registerForm': registerForm})
