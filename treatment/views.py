from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView
from django.http import request
from .models import Treatment


class TreatmentListView(ListView):
    model = Treatment
    template_name = "price_list.html"
    queryset = Treatment.objects.all().order_by('treatment_type')
    context_object_name = "treatments"


class ServicesListView(ListView):
    template_name = 'services.html'
    queryset = Treatment.objects.all()
    context_object_name = "treatments"
