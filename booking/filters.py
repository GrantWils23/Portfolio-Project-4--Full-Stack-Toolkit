''' the filter file to filter the custom admin view bookings '''
import django_filters
from .models import Booking


class AdminFilter(django_filters.FilterSet):
    ''' filtering class for the admin list view '''
    class Meta:
        ''' the meta data to the admin filter '''
        model = Booking
        fields = {
            'user': ['exact'],
            'booking_id': ['exact'],
            }
