import django_filters
from .models import EmployeesModel

class EmployeeFilter(django_filters.FilterSet):
    designa =django_filters.CharFilter(field_name='designation',lookup_expr='iexact',label='Dasignaton emp')
    emp_names=django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains',)
    #ids=django_filters.RangeFilter(field_name='id')
    ids_min=django_filters.CharFilter(method='filter_by_id',label='id from')
    ids_max=django_filters.CharFilter(method='filter_by_id',label='id to')

    class Meta:
        model=EmployeesModel
        fields=['designa','emp_names','ids_min','ids_max']

    
    def filter_by_id(self,queryset,name,value):
        if name=="ids_min":
            return queryset.filter(emp_id__gte=value)
        elif name=="ids_max":
            return queryset.filter(emp_id__lte=value)
        
        return queryset