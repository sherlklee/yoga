from django.urls import path
from .views import *

urlpatterns = {
    path('addclassroom/', addclassroom),
    path('classroomlist/',classroomlist),
}