from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


TREATMENTS = ((0, "Facial"), (1, "Make-Up"), (2, "Pedicure"), (3, "Manicure"), (4, "EyeBrow Plucking"))

TIMESLOTS = ((0, "9am-11am"), (1, "12pm-2pm"), (2, "3pm-5pm"), (3, "6pm-8pm"))


class Booking(models.Model):
    booking_id = models.BigAutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User")
    contact_no = PhoneNumberField(region="GB")
    email = models.EmailField()
    treatment = models.IntegerField(choices=TREATMENTS)
    booking_time = models.DateField(auto_now=True)
    appointment_date = models.DateField()
    appointment_slot = models.IntegerField(choices=TIMESLOTS)
    address_line_one = models.CharField(max_length=60)
    address_line_two = models.CharField(max_length=60)
    address_line_three = models.CharField(max_length=60)
    city = models.CharField(max_length=20)
    post_code = models.CharField(max_length=10)
    addition_info = models.TextField(max_length=300, null=True, )

    class meta:
        ordering = ['appointment_date', 'appointment time']

    def __str__(self):
        return f"Booking No. #{self.booking_id}"

