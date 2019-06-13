from django.urls import path
from .views import *

urlpatterns = {
    path('customer/', membermessage),
    path('customertime/', membermessagetime),
    path('customer/<username>/', membermessagedetail),
    path('trainer/', trainermessage),
}