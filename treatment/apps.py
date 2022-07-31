''' the treatment app config settings '''
from django.apps import AppConfig


class TreatmentConfig(AppConfig):
    ''' Treatment Config for the app and how the default behaves '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'treatment'
