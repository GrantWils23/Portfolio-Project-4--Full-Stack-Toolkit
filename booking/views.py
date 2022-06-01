from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from .models import Booking
from .forms import BookingForm


class Home(TemplateView):
    template_name = 'index.html'


class Gallery(TemplateView):
    template_name = 'gallery.html'


class Services(TemplateView):
    template_name = 'services.html'


class ListBookings(ListView):
    model = Booking()
    queryset = Booking.objects.all().order_by('booking_id')
    template_name = 'bookings.html'
    paginate_by = 6

    def get_queryset(self):
        return Booking.objects.all()


class ViewBooking(DetailView):
    template_name = 'booking_details.html'
    model = Booking
    template_name_suffix = '<int:pk>'


class AddBookingView(SuccessMessageMixin, CreateView):
    template_name = 'booking_form.html'
    form_class = BookingForm
    success_message = 'Thank you for your booking, We will send you a confirmation email shortly'


class EditBookingView(SuccessMessageMixin, UpdateView):
    template_name = 'booking_form.html'
    form_class = BookingForm
    model = Booking
    success_message = 'Thank you for your booking, We will send you a confirmation email shortly'


class DeleteBookingView(DeleteView):
    template_name = 'delete_booking.html'
    model = Booking
    success_url = reverse_lazy('bookings')
