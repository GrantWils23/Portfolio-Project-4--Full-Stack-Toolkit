# Generated by Django 3.2 on 2022-06-29 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('treatment', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('contact_no', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='GB')),
                ('email', models.EmailField(max_length=254)),
                ('booking_time', models.DateField(auto_now=True)),
                ('appointment_date', models.DateField()),
                ('appointment_slot', models.IntegerField(choices=[(0, '9am-11am'), (1, '12pm-2pm'), (2, '3pm-5pm'), (3, '6pm-8pm')])),
                ('address_line_one', models.CharField(max_length=60)),
                ('address_line_two', models.CharField(blank=True, max_length=60)),
                ('address_line_three', models.CharField(blank=True, max_length=60)),
                ('city', models.CharField(max_length=20)),
                ('post_code', models.CharField(max_length=10)),
                ('addition_info', models.TextField(blank=True, max_length=300)),
                ('cancelled', models.IntegerField(choices=[(0, 'OK'), (1, 'CANCELLED')], default=0)),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Treatment_Name', to='treatment.treatment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
