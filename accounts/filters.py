import django_filters
from django_filters import DateFilter
from .models import *

class Orderfilter(django_filters.FilterSet):
    class Meta:
        start_date = DateFilter(field_name = 'date_created',lookup_expr = 'gte')
        end_date = DateFilter(field_name = 'date_created',lookup_expr = 'lte')
        model = Order
        fields = '__all__'
        exclude = ['customer','date_created']