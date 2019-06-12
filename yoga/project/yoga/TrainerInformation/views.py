from django.shortcuts import render, HttpResponseRedirect
from .forms import TrainerForm
from Database.models import Customer ,Customerinformation,Trainerinformation
from Sessionmanager.sessionmanager import SessionManager
# Create your views here.
def trainerinformation(request):
    sessionManager = SessionManager(request)
    if sessionManager.Islogouted():
        return HttpResponseRedirect("/")
    username = sessionManager.Getusername()
    user = Customer.objects.get(username=username)
    if user.Isadmin():
        HttpResponseRedirect("/")
    elif user.Iscustomer():
        HttpResponseRedirect("/")
    else:
        userid = "trainer"
        if request.method == "POST":
            trainerform = TrainerForm(request.POST)
            if trainerform.is_valid():
                name = trainerform.cleaned_data.get('name')
                age = trainerform.cleaned_data.get('age')
                professionaltitle = trainerform.cleaned_data.get('professionaltitle')
                phone = trainerform.cleaned_data.get('phone')
                sex = trainerform.cleaned_data.get('sex')
                photo = trainerform.cleaned_data.get('photo')
                introduction = trainerform.cleaned_data.get('introduction')

                username = sessionManager.Getusername()
                personalInformation = Trainerinformation.objects.get(username=username)

                personalInformation.Setname(name)
                personalInformation.Setage(age)
                personalInformation.Setprofessionaltitle(professionaltitle)
                personalInformation.Setphone(phone)
                personalInformation.Setsex(sex)
                personalInformation.Setintroduction(introduction)
                personalInformation.Setphoto(photo)

                return HttpResponseRedirect("/")

        else:
            userinformation = Trainerinformation.objects.get(username=username)
            trainerform = TrainerForm(instance=userinformation)
    return render(request, "trainerinformationUI.html", locals())