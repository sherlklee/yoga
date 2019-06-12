from django.shortcuts import render, HttpResponseRedirect
from .form import CompleteForm
from Database.models import Customer ,Customerinformation
from Sessionmanager.sessionmanager import SessionManager
# Create your views here.
def customerinformation(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    username = sessionManager.Getusername()
    user = Customer.objects.get(username=username)
    userinformation = Customerinformation.objects.get(username = username)
    if user.Isadmin():
        HttpResponseRedirect("/")
    elif user.Istrainer():
        HttpResponseRedirect("/trainerinformation/")
    elif user.Iscustomer():
        userid = "customer"
        if request.method == "POST":
            customerform = CompleteForm(request.POST)
            if customerform.is_valid():
                name = customerform.cleaned_data.get('name')
                age = customerform.cleaned_data.get('age')
                profession = customerform.cleaned_data.get('profession')
                phone = customerform.cleaned_data.get('phone')
                sex = customerform.cleaned_data.get('sex')
                birthday = customerform.cleaned_data.get('birthday')
                height = customerform.cleaned_data.get('height')
                weight = customerform.cleaned_data.get('weight')
                bust = customerform.cleaned_data.get('bust')
                waistline = customerform.cleaned_data.get('waistline')
                hipline = customerform.cleaned_data.get('hipline')
                shoulderwidth = customerform.cleaned_data.get('shoulderwidth')

                personalInformation = Customerinformation.objects.get(username=username)

                personalInformation.Setname(name)
                personalInformation.Setage(age)
                personalInformation.Setprofession(profession)
                personalInformation.Setphone(phone)
                personalInformation.Setsex(sex)
                personalInformation.Setbirthday(birthday)
                personalInformation.Setheight(height)
                personalInformation.Setweight(weight)
                personalInformation.Setbust(bust)
                personalInformation.Setwaistline(waistline)
                personalInformation.Sethipline(hipline)
                personalInformation.Setshoulderwidth(shoulderwidth)
                return HttpResponseRedirect("/")

        else:
            customerform = CompleteForm(instance=userinformation)
    return render(request, "customerinformationUI.html", locals())