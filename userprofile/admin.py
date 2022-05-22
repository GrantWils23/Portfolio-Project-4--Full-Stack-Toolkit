from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'contact_no',)
    search_fields = ['user', 'post_code', 'bookings']
    list_filter = ('user', )
