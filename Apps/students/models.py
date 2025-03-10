from django.db import models


class StudentModel(models.Model):
    student_id=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_to=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
