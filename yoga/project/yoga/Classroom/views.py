from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from Sessionmanager.sessionmanager import SessionManager
from .forms import ClassroomForm
from Database.models import Customer, Course, Classroom
from django.db.models import Q

def addclassroom(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    username = sessionManager.Getusername()
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
    username = sessionManager.Getusername()
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    if request.method == "POST":
        search = request.POST.get("search")
        if search:
            classroom = Classroom.objects.filter(Q(classroomname__startswith=search))
        else:
            classroom = Classroom.objects.all()
    else:
        classroom = Classroom.objects.all()
    return render(request, "classroomlist.html", locals())