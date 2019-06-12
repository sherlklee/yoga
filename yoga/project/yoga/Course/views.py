from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from Sessionmanager.sessionmanager import SessionManager
from .forms import CourseForm
from Database.models import Customer, Course
from django.db.models import Q

def addcourse(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    else:
        if request.method == "POST":
            course = CourseForm(request.POST)
            if course.is_valid():
                coursename = course.cleaned_data.get('coursename')
                trainer = course.cleaned_data.get('trainer')
                courseprice = course.cleaned_data.get('courseprice')
                introduction = course.cleaned_data.get('introduction')
                coursenew = Course.objects.create(coursename=coursename, trainer=trainer, courseprice=courseprice, introduction=introduction)
                return HttpResponseRedirect("/course/courselist/")
        else:
            course = CourseForm()
    return render(request, "addcourse.html", {"course": course})

def courselist(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    if request.method == "POST":
        search = request.POST.get("search")
        if search:
            course = Course.objects.filter(Q(coursename=search) | Q(trainer=search) & Q(coursevalid=True))
        else:
            course = Course.objects.filter(coursevalid=True)
    else:
        course = Course.objects.filter(coursevalid=True)
    return render(request, "courselist.html", locals())


def discourse(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    if request.method == "POST":
        search = request.POST.get("search")
        if search:
            course = Course.objects.filter(Q(coursename=search) | Q(trainer=search) & Q(coursevalid=False))
        else:
            course = Course.objects.filter(coursevalid=False)
    else:
        course = Course.objects.filter(coursevalid=False)
    return render(request, "discourse.html", locals())

def canclecourse(request, id):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    course = Course.objects.get(courseid=id)
    course.Setcoursevalid(False)
    return HttpResponseRedirect("/course/courselist/")

def trainercourse(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    username = sessionManager.Getusername()
    user = Customer.objects.get(username=username)
    if not user.Istrainer():
        return HttpResponseRedirect("/")
    else:
        course_list = Course.objects.filter(trainer=username)
    return render(request,"trainercourse.html",locals())

def changecourse(request,courseid):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    course = Course.objects.get(courseid=courseid)
    courseform = CourseForm(course)
    return render(request, "mkscourse.html", locals())

def coursedetail(request,courseid):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    course = Course.objects.get(courseid=courseid)
    return render(request, "coursedetail.html", locals())