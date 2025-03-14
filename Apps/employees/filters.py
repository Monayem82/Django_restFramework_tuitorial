import django_filters
from .models import EmployeesModel

class EmployeeFilter(django_filters.FilterSet):
    designa =django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
    emp_names=django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains')

    class Meta:
        model=EmployeesModel
        fields=['designa','emp_names']