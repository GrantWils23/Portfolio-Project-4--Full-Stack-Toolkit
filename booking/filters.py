import django_filters
from .models import Booking

class AdminFilter(django_filters.FilterSet):
    class Meta:
        model = Booking
        fields = {
            'user': ['exact'],
            'booking_id': ['exact'],
            }
