from django.contrib import admin
from Apps.students.models import StudentModel

class StudentModelAdmin(admin.ModelAdmin):
    list_display=('id','student_id','name','department','create_at','updated_to')
    search_fields=['name']

admin.site.register(StudentModel,StudentModelAdmin)