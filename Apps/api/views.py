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
        