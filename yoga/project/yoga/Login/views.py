from django.shortcuts import render, HttpResponseRedirect ,HttpResponse
from .forms import LoginForm
from Database.models import Customer
from Sessionmanager.sessionmanager import SessionManager
# Create your views here.

def customerlogin(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogined():
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data.get('username')
            sessionManager.Setlogin(username)
            user = Customer.objects.get(username=username)
            if user.Isadmin():
                return HttpResponseRedirect("/")
            elif user.Istrainer():
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/")
    else:
        loginForm = LoginForm()
    return render(request, 'loginUI.html', {'loginForm': loginForm})


def logout(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogined():
        sessionManager.Setlogout()
    return HttpResponseRedirect("/")