from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import TemplateView, FormView, CreateView, DeleteView, UpdateView, DetailView, ListView
from django.http import HttpResponseRedirect, HttpResponse
from .models import Booking
from .forms import BookingForm
from django.urls import reverse_lazy


class Home(TemplateView):
    template_name = 'index.html'


class Gallery(TemplateView):
    template_name = 'gallery.html'


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
    context_object_name = 'booking'


class AddBookingView(CreateView):
    template_name = 'booking_form.html'
    model = Booking
    fields = ['user', 'contact_no', 'email', 'treatment',
              'appointment_date', 'appointment_slot', 'address_line_one',
              'address_line_two', 'address_line_three', 'city',
              'post_code', 'addition_info', ]


class EditBookingView(UpdateView):
    model = Booking()
    fields = ['user', 'contact_no', 'email', 'treatment',
              'appointment_date', 'appointment_slot', 'address_line_one',
              'address_line_two', 'address_line_three', 'city',
              'post_code', 'addition_info', ]


class DeleteBookingView(DeleteView):
    model = Booking

# def add_booking(request):
#     return render(request, "create_booking.html", {'form': BookingForm()})



# # GET:
    # Form
# POST:
    # csrf
    # validate
    # save
    # redirect to success page (to Booking details page)
        # read the get_absolute_url from the object

