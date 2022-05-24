from .models import Booking
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('user', 'contact_no', 'email', 'treatment', 'appointment_date',
        'appointment_slot', 'address_line_1', 'address_line_2', 'address_line_3', 
        'city', 'postcode', 'additional_info', )
