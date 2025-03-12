
from django.urls import path,include
from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'employees',views.StudentViewSetsView)


urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>',views.studentDetailsViews,name="Studnet-api-view"),

    #class based url patterns
    # path('employees/',views.EmployeesClassView.as_view()),
    # path('employees/<int:pk>',views.EmployeesDetailsClassView.as_view())

    path('',include(router.urls))
]

