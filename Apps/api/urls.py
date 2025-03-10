
from django.urls import path
from api import views

urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>',views.studentDetailsViews,name="Studnet-api-view"),
]

