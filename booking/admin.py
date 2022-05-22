from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'user', 'email', 'contact_no', 'appointment_date', 'appointment_slot', 'treatment')
    search_fields = ['booking_id', 'email', ]
    list_filter = ('appointment_date', 'appointment_slot')
