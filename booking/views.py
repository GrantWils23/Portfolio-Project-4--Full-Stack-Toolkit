from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import Booking
# from .forms import CommentForm

class Home(TemplateView):
    template_name = "index.html"

class Gallery(TemplateView):
    template_name = "gallery.html"
    
# class BookingList(generic.ListView):
#     model = Booking()
#     template_name = 'index.html'
