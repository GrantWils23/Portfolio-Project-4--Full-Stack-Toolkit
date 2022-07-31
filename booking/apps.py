''' the admin.py file for the booking app '''
from django.apps import AppConfig


class BookingConfig(AppConfig):
    ''' the admin file how the default value of a booking behaves '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'
