from django.urls import path
from .views import *

urlpatterns = {
    path('addcourse/', addcourse),
    path('courselist/', courselist),
    path('discourse/', discourse),
    path('cancle/<int:id>', canclecourse),
    path('trainercourse/',trainercourse),
    path('changecourse/<int:courseid>', changecourse),
    path('<int:courseid>/',coursedetail),
    path('customercourse/',customercourse),
}
