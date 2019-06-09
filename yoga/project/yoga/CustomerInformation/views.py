from django.shortcuts import render

# Create your views here.
def customerinformation(requset):

    return render(requset,locals())