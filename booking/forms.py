
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import ModelForm
from crispy_forms.layout import Submit, Field, Layout, HTML
from crispy_forms.helper import FormHelper
from phonenumber_field.formfields import PhoneNumberField
from .models import Booking, TIMESLOTS


class DateInput(forms.DateInput):
    ''' The DateInput selector for the model form '''
    input_type = 'date'


class CancelForm(forms.ModelForm):
    '''
    The CancelForm model that allows the user to change
    the status of the booking to cancelled
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['cancelled'] = 1

    class Meta:
        model = Booking
        fields = ["cancelled", ]
        widgets = {'cancelled': forms.HiddenInput(), }


class BookingForm(ModelForm):
    '''
    The BookingForm model that operates for the websites bookings
    '''
    def clean_appointment_date(self):
        data = self.cleaned_data['appointment_date']

        if data <= datetime.date.today():
            raise ValidationError(_('invalid date - date selected has to be in the future from today'))
        return data

    def validate_unique(self):
        '''
        Call the instance's validate_unique() method and update the form's
        validation errors if any were raised.
        '''
        exclude = self._get_validation_exclusions()
        try:
            self.instance.validate_unique(exclude=exclude)
        except ValidationError as error:  # e
            error = {'__all__': "The date and time slot have selected by someone else, please try a new time or date"}
            self._update_errors(error)

    contact_no = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': '+44'}), label=_("Phone number"))
    additional_info = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4},))
    appointment_date = forms.DateField(widget=DateInput(attrs={"class": "form-control datepicker validate"}))
    appointment_slot = forms.ChoiceField(choices=TIMESLOTS, widget=forms.RadioSelect)
    
    # def send_email(self):
    #     pass

    class Meta:
        model = Booking
        fields = ['contact_no', 'treatment',
                  'appointment_date', 'appointment_slot', 'address_line_one',
                  'address_line_two', 'address_line_three', 'city',
                  'post_code', 'additional_info',
                  ]

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout()
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row'),
            )
        helper.field_class = 'col-sm-9'
        helper.label_class = 'col-sm-3'
        helper.layout.append(HTML('<br>'))
        helper.layout.append(HTML('<div class="col-sm-12 form-group">'))
        helper.layout.append(HTML('<div class="text-center">'))
        helper.layout.append(Submit('submit', 'Submit Booking', css_class='pag-page-btn center-button', css_id="submit-booking"))
        helper.layout.append(HTML('</div>'))
        helper.layout.append(HTML('</div>'))
        return helper


class AdminBookingForm(forms.ModelForm):
    '''
    The BookingForm model that operates for the websites bookings
    '''
    def clean_appointment_date(self):
        data = self.cleaned_data['appointment_date']

        if data <= datetime.date.today():
            raise ValidationError(_('invalid date - date selected has to be in the future from today'))
        return data

    def validate_unique(self):
        '''
        Call the instance's validate_unique() method and update the form's
        validation errors if any were raised.
        '''
        exclude = self._get_validation_exclusions()
        try:
            self.instance.validate_unique(exclude=exclude)
        except ValidationError as error:  # e
            error = {'__all__': "The date and time slot have selected by someone else, please try a new time or date"}
            self._update_errors(error)

    contact_no = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': '+44'}), label=_("Phone number"))
    additional_info = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4},))
    appointment_date = forms.DateField(widget=DateInput(attrs={"class": "form-control datepicker validate"}))
    appointment_slot = forms.ChoiceField(choices=TIMESLOTS, widget=forms.RadioSelect)
    
    class Meta:
        model = Booking
        fields = ['user', 'email', 'contact_no', 'treatment',
                  'appointment_date', 'appointment_slot', 'address_line_one',
                  'address_line_two', 'address_line_three', 'city',
                  'post_code', 'additional_info', 'cancelled',
                  ]

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout()
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row'),
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

