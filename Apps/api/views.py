from django.shortcuts import render
from django.http import JsonResponse

from . serializers import StudentSerializer 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from Apps.students.models import StudentModel


# def studentsView(request):
#     students=StudentModel.objects.all() # As a Queryset (dictionary)
#     #print(students.values()) #Query set list dictionary
#     values_list=list(students.values()) # QuerySet is represent in list and inner its dictionary
#     #print(values_list)
#     return JsonResponse(values_list,safe=False) #JsonResponse always need to dictionary. safe=False means data should be comes any format

@api_view(['GET'])
def studentsView(request):
    if request.method =='GET':
        students=StudentModel.objects.all()
        serializer=StudentSerializer(students,many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)