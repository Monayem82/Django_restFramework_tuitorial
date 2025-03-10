
from django.urls import path
from api import views

urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>',views.studentDetailsViews,name="Studnet-api-view"),

    #class based url patterns
    path('employees/',views.EmployeesClassView.as_view()),
    path('employees/<int:pk>',views.EmployeesDetailsClassView.as_view())
]

