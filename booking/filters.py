import django_filters
from .models import Booking
from django_filters import DateFilter


class AdminFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name='appointment_date', lookup_expr="gte", )
    # end_date = DateFilter(field_name='appointment_date', lookup_expr="lte")

    class Meta:
        model = Booking
        fields = {'user': ['exact'],
                  'booking_id': ['exact'],
        }

