from django.contrib import admin

from Apps.employees.models import EmployeesModel

class EmployeeModelAdmin(admin.ModelAdmin):
    list_display=('id','emp_id','emp_name','designation','created_at','updated_to')
    search_fields=['emp_name']

admin.site.register(EmployeesModel,EmployeeModelAdmin)
