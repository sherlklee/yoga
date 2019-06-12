from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from Sessionmanager.sessionmanager import SessionManager
from .forms import ClassroomForm
from Database.models import Customer, Course, Classroom

def addclassroom(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    else:
        if request.method == "POST":
            classroom = ClassroomForm(request.POST)
            if classroom.is_valid():
                classroomname = classroom.cleaned_data.get("classroomname")
                note = classroom.cleaned_data.get("note")
                maxpersonnumber = classroom.cleaned_data.get("maxpersonnumber")
                classroomnew = Classroom.objects.create(classroomname=classroomname, note=note, maxpersonnumber=maxpersonnumber)
                return HttpResponseRedirect("/")
        else:
            classroom = ClassroomForm()
    return render(request, 'addclassroom.html', locals())

def classroomlist(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    classroom = Classroom.objects.all()
    return render(request,"classroomlist.html",locals())