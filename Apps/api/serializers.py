from rest_framework import serializers
from Apps.students.models import StudentModel
from Apps.employees.models import EmployeesModel

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields ="__all__"


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model =EmployeesModel
        fields="__all__"