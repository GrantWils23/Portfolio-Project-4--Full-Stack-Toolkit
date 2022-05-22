from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from booking.models import Booking


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_no = PhoneNumberField(region='GB')
    birth_date = models.DateField(null=True, blank=True)
    address_line_one = models.CharField(max_length=60)
    address_line_two = models.CharField(max_length=60)
    address_line_three = models.CharField(max_length=60, null=True)
    city = models.CharField(max_length=20)
    post_code = models.CharField(max_length=10)

    class meta:
        ordering = ['user', ]

    def __str__(self):
        return f"Welcome {self.user}"
