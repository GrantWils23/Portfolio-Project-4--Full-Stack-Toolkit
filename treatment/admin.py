from django.contrib import admin
from .models import Treatment
# Register your models here.


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'treatment_name', 'treatment_type', 'treatment_price')
    search_fields = ['treatment_type', 'treatment_name', ]
    list_filter = ('treatment_type',)
