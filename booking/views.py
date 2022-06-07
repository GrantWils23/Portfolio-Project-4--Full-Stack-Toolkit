from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views import generic, View
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, DetailView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import request
from .models import Booking
from .forms import BookingForm


class Home(TemplateView):
    template_name = 'index.html'


class Gallery(TemplateView):
    template_name = 'gallery.html'


class Services(TemplateView):
    template_name = 'services.html'


class Contact(TemplateView):
    template_name = 'contact.html'


class PriceList(TemplateView):
    template_name = 'price_list.html'

class ListBookings(ListView):
    model = Booking
    queryset = Booking.objects.all().order_by('-booking_id')
    template_name = 'bookings.html'
    paginate_by = 6
    context_object_name = 'bookings'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ViewBooking(DetailView):
    template_name = 'booking_details.html'
    model = Booking
    template_name_suffix = '<int:pk>'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class AddBookingView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'booking_form.html'
    form_class = BookingForm
    success_message = 'Thank you for your booking, We will send you a confirmation email shortly.'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        return super().form_valid(form)


class EditBookingView(SuccessMessageMixin, UpdateView):
    template_name = 'booking_form.html'
    form_class = BookingForm
    model = Booking
    success_message = 'Your booking details has been updated, you will receive a confirmation email shortly.'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class DeleteBookingView(SuccessMessageMixin, DeleteView):
    template_name = 'delete_booking.html'
    model = Booking
    success_url = reverse_lazy('bookings')
    success_message = 'Your booking has been cancelled. Sorry to hear that but we hope to see you again soon. You will receive an email shortly.'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def delete(self, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(DeleteBookingView, self).delete(request, *args, **kwargs)


# Error Handlers #
def handler400(request, exception):
    return render(request, 'handler400.html', status=400)


def handler403(request, exception):
    return render(request, 'handler403.html', status=403)


def handler404(request, exception):
    return render(request, 'handler404.html', status=404)


def handler500(request):
    return render(request, 'handler500.html', status=500)
