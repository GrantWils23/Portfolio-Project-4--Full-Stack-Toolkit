import django_filters
from .models import Booking


class AdminFilter(django_filters.FilterSet):
    ''' filtering class for the admin list view '''
    class Meta:
        model = Booking
        fields = {
            'user': ['exact'],
            'booking_id': ['exact'],
            }
