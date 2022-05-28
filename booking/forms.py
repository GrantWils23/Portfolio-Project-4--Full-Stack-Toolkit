from .models import Booking
from django import forms
from django.forms import Form
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout, HTML

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(ModelForm):
    addition_info = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    # appointment_date = forms.DateField(widget=DateInput)
    appointment_date = forms.DateField(widget=DateInput(attrs={"class": "form-control datepicker validate"}))

    class Meta:
        model = Booking
        fields = ['user', 'contact_no', 'email', 'treatment',
                  'appointment_date', 'appointment_slot', 'address_line_one',
                  'address_line_two', 'address_line_three', 'city',
                  'post_code', 'addition_info',
                  ]

# Custom control required on the treatment, appointment_date and appointment_slot
    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            # Field('User'),
            # Field('contact_no'),
            # Field('email'),
            # Field('treatment'),
            # Field('appointment_date'),
            # Field('appointment_slot'),
            # Field('address_line_one'),
            # Field('address_line_two'),
            # Field('address_line_three'),
            # Field('city'),
            # Field('post_code'),
            # Field('addition_info'),
            # Submit('submit', 'Submit your Booking', css_class='pag-page-btn')
        )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        # helper.layout.append(Submit('submit', 'Submit your Booking', css_class='pag-page-btn'))
        helper.field_class = 'col-sm-9'
        helper.label_class = 'col-sm-3'
        return helper
