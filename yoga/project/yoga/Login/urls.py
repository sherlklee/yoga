from django.urls import path
from .views import *

urlpatterns = {
    path('', customerlogin),
    path('logout/', logout),
}
