''' the admins view to the treatment model in the admin terminal '''
from django.contrib import admin
from .models import Treatment


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    ''' the Treatment settings in the Admin terminal '''
    list_display = ('pk', 'treatment_name',
                    'treatment_type', 'treatment_price')
    search_fields = ['treatment_type', 'treatment_name', ]
    list_filter = ('treatment_type',)
