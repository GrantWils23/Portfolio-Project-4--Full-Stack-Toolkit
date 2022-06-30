from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from treatment.models import Treatment

# Choices related to the booking form
TIMESLOTS = ((0, "9am-11am"), (1, "12pm-2pm"), (2, "3pm-5pm"), (3, "6pm-8pm"))
APPOINTMENT_STATUS = ((0, 'OK'), (1, 'CANCELLED'))


class Booking(models.Model):
    ''' The booking Model for clients '''
    booking_id = models.BigAutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User")
    contact_no = PhoneNumberField(region="GB", null=False, blank=False)
    email = models.EmailField()
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE, related_name="Treatment_Name")
    booking_time = models.DateField(auto_now=True)
    appointment_date = models.DateField()
    appointment_slot = models.IntegerField(choices=TIMESLOTS)
    address_line_one = models.CharField(max_length=60)
    address_line_two = models.CharField(max_length=60, blank=True)
    address_line_three = models.CharField(max_length=60, blank=True)
    city = models.CharField(max_length=20)
    post_code = models.CharField(max_length=10)
    addition_info = models.TextField(max_length=300, blank=True)
    cancelled = models.IntegerField(choices=APPOINTMENT_STATUS, default=0)

    class Meta:
        ordering = ['appointment_date', 'appointment_slot']
        constraints = [
            models.UniqueConstraint(fields=['appointment_date', 'appointment_slot'], name='unique_booking')
        ]

    def __str__(self):
        return f"Booking No. #{self.booking_id}"

    def __name__(self):
        return f"Booking No. {self.booking_id}"

    def get_absolute_url(self):
        ''' return back to the reverse url of the booking '''
        return reverse("view-booking", kwargs={'pk': self.pk})
