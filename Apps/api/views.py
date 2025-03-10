from django.shortcuts import render
from django.http import JsonResponse,Http404

from . serializers import StudentSerializer ,EmployeesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from Apps.students.models import StudentModel
from Apps.employees.models import EmployeesModel


# def studentsView(request):
#     students=StudentModel.objects.all() # As a Queryset (dictionary)
#     #print(students.values()) #Query set list dictionary
#     values_list=list(students.values()) # QuerySet is represent in list and inner its dictionary
#     #print(values_list)
#     return JsonResponse(values_list,safe=False) #JsonResponse always need to dictionary. safe=False means data should be comes any format


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

class EmployeesClassView(APIView):
    def get(self,request): #member functon
        employee=EmployeesModel.objects.all()
        serializer=EmployeesSerializer(employee, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class EmployeesDetailsClassView(APIView):
    def get_object(self,pk):
        try:
            employee=EmployeesModel.objects.get(pk=pk)
            return employee
        except EmployeesModel.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        employee=self.get_object(pk)
        serializer=EmployeesSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        emplooyee=self.get_object(pk)
        serializer=EmployeesSerializer(emplooyee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employee=self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        