from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import TemplateView, DetailView, ListView
from django.http import request
from .models import Treatment


class TreatmentListView(ListView):
    template_name = "price_list.html"
    queryset = Treatment.objects.all().order_by('treatment_type')
    context_object_name = "treatments"


class ServicesListView(ListView):
    template_name = 'services.html'
    queryset = Treatment.objects.all()
    coontext_object_name = 'treatments'
