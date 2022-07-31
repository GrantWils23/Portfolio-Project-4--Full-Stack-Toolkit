''' The treatment app view file '''
from django.views.generic import ListView
from .models import Treatment


class TreatmentListView(ListView):
    ''' the treatment list view  '''
    model = Treatment
    template_name = "price_list.html"
    queryset = Treatment.objects.all().order_by('treatment_type')
    context_object_name = "treatments"


class ServicesListView(ListView):
    ''' the services list view '''
    template_name = 'services.html'
    queryset = Treatment.objects.all()
    context_object_name = "treatments"
