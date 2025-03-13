
from django.urls import path,include
from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'employees',views.EmployeeViewSetsView)
router.register(r'blogs',views.blogModelViewSets)
router.register(r'comments',views.CommentModelViewSets)


urlpatterns = [
    # Studnet APPS
    path('students/',views.studentsView),
    path('students/<int:pk>',views.studentDetailsViews,name="Studnet-api-view"),

    # Employee APPS
    #class based url patterns  ---- class based APIView ----
    # path('employees/',views.EmployeesClassView.as_view()),
    # path('employees/<int:pk>',views.EmployeesDetailsClassView.as_view())

    path('',include(router.urls)),


    # Blog APSS

    # path('blogs/',views.BlogAPIViewSets.as_view()),
    # path('blogs/<int:pk>',views.BlogDeteilsViewsets.as_view()),
    # path('comments/',views.CommentAPIViewSets.as_view()),


    # ModelViewSet

    #Blog serializer
    path('',include(router.urls)),

    #comment serializer
    path('',include(router.urls))

]

