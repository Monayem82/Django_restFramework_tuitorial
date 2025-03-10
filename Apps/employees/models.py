from django.db import models

class EmployeesModel(models.Model):
    emp_id=models.CharField(max_length=10)
    emp_name=models.CharField(max_length=25)
    designation=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_to=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.emp_name} - {self.designation}'
