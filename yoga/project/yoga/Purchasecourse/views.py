from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from Sessionmanager.sessionmanager import SessionManager
from Database.models import Customer, Course, BuyRecord
def purchasecourse(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    else:
        course_list = Course.objects.filter(coursevalid=True)
    return render(request, "customerpuchasecourse.html", locals())

def purchasemks(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    if request.method == 'POST':
        username_now=sessionManager.Getusername()
        course = request.POST.get('course_name', '')
        amounttemp = request.POST.get('quantity', '')
        if course and amounttemp:
            course_temp = Course.objects.get(coursename=course)
            idtemp = BuyRecord.objects.order_by('-number')
            if idtemp:
                numbertemp = idtemp[0].Getnumber()+1
            else:
                numbertemp = 0
            temp = int(amounttemp)
            p = BuyRecord()
            p.coursename = course
            p.number = numbertemp
            p.username = username_now
            p.price = temp*course_temp.Getcourseprice()
            p.courseid = course_temp.Getcourseid()
            p.amount = temp
            p.Setpayflag(False)
            return HttpResponse("添加成功")
    return HttpResponse("添加失败")

def showmyrecordunpaid(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    username = sessionManager.Getusername()
    record = BuyRecord.objects.filter(valid=True, username=username, pay_flag=False)
    return render(request,"showunpaidrecord.html",locals())

def showmyrecordpaid(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    username = sessionManager.Getusername()
    record = BuyRecord.objects.filter(valid=True, username=username, pay_flag=True)
    return render(request,"showpaidrecord.html",locals())

def cancelrecord(request, recordid):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    record = BuyRecord.objects.get(number=recordid)
    record.Setvalid(False)
    if sessionManager.Isadministrator():
        return HttpResponseRedirect("/purchasecourse/showrecordadmin/unpaid/")
    return HttpResponseRedirect("/purchasecourse/myrecord/unpaid/")

def makesurerecord(request, recordid):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    record = BuyRecord.objects.get(number=recordid)
    record.Setpayflag(True)
    return HttpResponseRedirect("/purchasecourse/showrecordadmin/unpaid/")

def deleterecord(request, recordid):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    record = BuyRecord.objects.get(number=recordid)
    record.Setvalid(False)
    return HttpResponseRedirect("/purchasecourse/showrecordadmin/unpaid/")

def showrecordadminpaid(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    record = BuyRecord.objects.filter(valid=True, pay_flag=True)
    return render(request, "showrecordadminpaid.html", locals())

def showrecordadminunpaid(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    record = BuyRecord.objects.filter(valid=True, pay_flag=False)
    return render(request, "showrecordadminunpaid.html", locals())



def showrecordadmindisvalid(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    if not sessionManager.Isadministrator():
        return HttpResponseRedirect("/")
    record = BuyRecord.objects.filter(valid=False)
    return render(request, "showrecordadmindsivalid.html", locals())