from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from phonenumber_field.modelfields import PhoneNumberField


TREATMENTS = ((0, "Facial"), (1, "Make-Up"), (2, "Pedicure"), (3, "Manicure"), (4, "Hair Styling"))

TIMESLOTS = ((0, "9am-11am"), (1, "12pm-2pm"), (2, "3pm-5pm"), (3, "6pm-8pm"))

class Booking(models.Model):
    booking_id = models.BigAutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User")
    contact_no = PhoneNumberField(region="GB", null=False, blank=False)
    email = models.EmailField()
    treatment = models.IntegerField(choices=TREATMENTS)
    booking_time = models.DateField(auto_now=True)
    appointment_date = models.DateField()
    appointment_slot = models.IntegerField(choices=TIMESLOTS)
    address_line_one = models.CharField(max_length=60)
    address_line_two = models.CharField(max_length=60)
    address_line_three = models.CharField(max_length=60, blank=True)
    city = models.CharField(max_length=20)
    post_code = models.CharField(max_length=10)
    addition_info = models.TextField(max_length=300, blank=True)


    class _Meta:
        ordering = ['appointment_date', 'appointment_slot']

    def __str__(self):
        return f"Booking No. #{self.booking_id}"

    def __name__(self):
        return f"Booking No. {self.booking_id}"

    def get_absolute_url(self):
        return reverse("view-booking", kwargs={'pk': self.pk})

