from django.shortcuts import render
from django.http import JsonResponse,Http404

from . serializers import StudentSerializer ,EmployeesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins,generics,viewsets
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

from django_filters.rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter,BaseFilterBackend,OrderingFilter
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from Apps.employees.filters import EmployeeFilter

from Apps.students.models import StudentModel
from Apps.employees.models import EmployeesModel

from Apps.blogs.models import Blog,Comment
from Apps.blogs.serializers import CommentSerializer,BlogSerializer


# def studentsView(request):
#     students=StudentModel.objects.all() # As a Queryset (dictionary)
#     #print(students.values()) #Query set list dictionary
#     values_list=list(students.values()) # QuerySet is represent in list and inner its dictionary
#     #print(values_list)
#     return JsonResponse(values_list,safe=False) #JsonResponse always need to dictionary. safe=False means data should be comes any format


# Custom Paginations

class CustomPagination(LimitOffsetPagination):
    page_size=3


# Function based views in API

@api_view(['GET','POST'])
def studentsView(request):
    if request.method =='GET':
        students=StudentModel.objects.all()
        serializer=StudentSerializer(students,many=True)
        #print(serializer)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method =="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def studentDetailsViews(request,pk):
    try:
        student=StudentModel.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer=StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method =="PUT":
        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=="DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

#Class Based Views

# class EmployeesClassView(APIView):
#     def get(self,request): #member functon
#         employee=EmployeesModel.objects.all()
#         serializer=EmployeesSerializer(employee, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def post(self,request):
#         serializer=EmployeesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
        

# class EmployeesDetailsClassView(APIView):
#     def get_object(self,pk):
#         try:
#             employee=EmployeesModel.objects.get(pk=pk)
#             return employee
#         except EmployeesModel.DoesNotExist:
#             raise Http404
    
#     def get(self,request,pk):
#         employee=self.get_object(pk)
#         serializer=EmployeesSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     def put(self,request,pk):
#         emplooyee=self.get_object(pk)
#         serializer=EmployeesSerializer(emplooyee,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         employee=self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# Mixins based API

# class EmployeesClassView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset =EmployeesModel.objects.all()
#     serializer_class=EmployeesSerializer

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)
    


# class EmployeesDetailsClassView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=EmployeesModel.objects.all()
#     serializer_class=EmployeesSerializer

#     def get(self,request,pk):
#         return self.retrieve(request,pk)
    
#     def put(self,request,pk):
#         return self.update(request,pk)
    
#     def delete(self,request,pk):
#         return self.destroy(request,pk)
    


# Generics APIView 

# class EmployeesClassView(generics.ListCreateAPIView):
#     queryset=EmployeesModel.objects.all()
#     serializer_class=EmployeesSerializer


# class EmployeesDetailsClassView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=EmployeesModel.objects.all()
#     serializer_class=EmployeesSerializer
#     lookup_field='pk'

# ViewSets in API

class EmployeeViewSetsView(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset=EmployeesModel.objects.all()
    serializer_class=EmployeesSerializer
    pagination_class=CustomPagination
    filterset_class=EmployeeFilter


#---------Blog Apps Api ---------

class BlogAPIViewSets(generics.ListCreateAPIView):
    
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    pagination_class=CustomPagination
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['blog_title', 'blog_content']
    ordering_fields=['id']

class BlogDeteilsViewsets(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    lookup_field="pk"


class CommentAPIViewSets(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer

# also use RetrieveUpdateDestroyAPIView in GET, Update , Destroy

#--------- Blog api with modelViewsets------------------------

# class blogModelViewSets(viewsets.ModelViewSet):
#     queryset=Blog.objects.all()
#     serializer_class=BlogSerializer

# class CommentModelViewSets(viewsets.ModelViewSet):
#     queryset=Comment.objects.all()
#     serializer_class=CommentSerializer