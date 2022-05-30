from .models import Booking
from django import forms
from django.forms import Form
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout, HTML

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(ModelForm):
    addition_info = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4}))
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
        helper.layout = Layout()
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.field_class = 'col-sm-9'
        helper.label_class = 'col-sm-3'
        helper.layout.append(HTML('<br>'))
        helper.layout.append(HTML('<div class="col-sm-12 form-group">'))
        helper.layout.append(HTML('<div class="text-center">'))
        helper.layout.append(Submit('submit', 'Submit Booking', css_class='pag-page-btn center-button'))
        helper.layout.append(HTML('</div>'))
        helper.layout.append(HTML('</div>'))

        return helper
