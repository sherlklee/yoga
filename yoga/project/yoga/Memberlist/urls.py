from django.urls import path
from .views import *

urlpatterns = {
    path('customer/', membermessage),
    path('trainer/', trainermessage),
}