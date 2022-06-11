from .models import Booking
from django import forms
from django.forms import Form, ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Field, Layout, HTML

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import datetime

class DateInput(forms.DateInput):
    input_type = 'date'


class CancelForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ["cancelled",]
        # widgets = {'cancelled': forms.HiddenInput(),}
        


class BookingForm(ModelForm):
    def clean_appointment_date(self):
        data = self.cleaned_data['appointment_date']

        if data < datetime.date.today():
            raise ValidationError(_('invalid date - date is in the past'))
        return data


    # def clean_appointment_slot(self):
    #     data = self.cleaned_data['appointment_slot', 'appointment_date']

    #     if data == :
    #         raise ValidationError(_('invalid timeslot - This slot is already been booked on this day'))
    #     return data


    addition_info = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4},))
    appointment_date = forms.DateField(widget=DateInput)
    appointment_date = forms.DateField(widget=DateInput(attrs={"class": "form-control datepicker validate"}))
    
    class Meta:
        model = Booking
        fields = ['contact_no', 'treatment',
                  'appointment_date', 'appointment_slot', 'address_line_one',
                  'address_line_two', 'address_line_three', 'city',
                  'post_code', 'addition_info',
                  ]
        help_texts = {'due_back': _('invalid date - date is in the past')}


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
