
from django.urls import path,include
from blogs import views

from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('',views.print)
]

