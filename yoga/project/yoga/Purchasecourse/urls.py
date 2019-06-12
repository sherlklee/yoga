from django.urls import path
from .views import *

urlpatterns = {
    path('', purchasecourse),
    path('mks/',purchasemks),
    path('myrecord/unpaid/', showmyrecordunpaid),
    path('myrecord/paid/', showmyrecordpaid),
    path('cancel/<int:recordid>', cancelrecord),
    path('makesure/<int:recordid>', makesurerecord),
    path('delete/<int:recordid>', deleterecord),
    path('showrecordadmin/paid/',showrecordadminpaid),
    path('showrecordadmin/disvalid/',showrecordadmindisvalid),
    path('showrecordadmin/unpaid/',showrecordadminunpaid),
}

