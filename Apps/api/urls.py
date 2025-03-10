
from django.urls import path
from api import views

urlpatterns = [
    path('students/',views.studentsView),
]

