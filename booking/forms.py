from .models import Booking
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout, HTML


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'contact_no', 'email', 'treatment',
                  'appointment_date', 'appointment_slot', 'address_line_one',
                  'address_line_two', 'address_line_three', 'city',
                  'post_code', 'addition_info', ]
        
    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
             HTML('<h2>Submit your Booking:</h2>')
        )
        return helper
