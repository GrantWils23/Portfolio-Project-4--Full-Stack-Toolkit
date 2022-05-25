from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import TemplateView, FormView, CreateView, DetailView, ListView
from django.http import HttpResponseRedirect
from .models import Booking
from .forms import BookingForm


class Home(TemplateView):
    template_name = 'index.html'


class Gallery(TemplateView):
    template_name = 'gallery.html'

class ListBookings(ListView):
    model = Booking()
    queryset = Booking.objects.all().order_by('-booking_id')
    template_name = 'bookings.html'
    paginate_by = 6

class BookingPage(FormView):
    template_name = 'booking.html'
    form_class = BookingForm.helper

    # form_class = BookingModel()

# class EditBooking(DetailView):
#     template_name = 'booking.html'
    

