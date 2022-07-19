
from datetime import date, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, DetailView, ListView, edit
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import request
from .models import Booking
from .forms import BookingForm, CancelForm, AdminBookingForm
from .filters import AdminFilter


class Home(TemplateView):
    template_name = 'index.html'


class Gallery(TemplateView):
    template_name = 'gallery.html'


class Contact(TemplateView):
    template_name = 'contact.html'

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
###########################################################
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class AddBookingView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    context_object_name = 'bookings'
    template_name = 'booking_form.html'
    form_class = BookingForm
    success_message = 'Thank you for your booking.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        return super().form_valid(form)

class EditBookingView(SuccessMessageMixin, UpdateView):
    template_name = 'booking_form.html'
    form_class = BookingForm
    model = Booking
    success_message = 'Your booking details has been updated.'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class CancelBookingView(SuccessMessageMixin, UpdateView):
    template_name = 'cancel_booking_form.html'
    form_class = CancelForm
    model = Booking
    success_message = 'Your booking has been cancelled'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class DeleteBookingView(SuccessMessageMixin, DeleteView):
    template_name = 'delete_booking.html'
    model = Booking
    success_url = reverse_lazy('bookings')
    success_message = 'Your booking has been deleted.'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def delete(self, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(DeleteBookingView, self).delete(request, *args, **kwargs)


class AdminListView(ListView):
    model = Booking
    template_name = 'admin-planner.html'
    queryset = Booking.objects.order_by('-appointment_date')
    paginate_by = 10
    context_object_name = 'bookings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        context['filter'] = AdminFilter(self.request.GET, self.get_queryset(),)
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return AdminFilter(self.request.GET, queryset=queryset).qs


class AdminListTodayView(ListView):
    model = Booking
    template_name = 'admin-planner.html'
    today = date.today()
    queryset = Booking.objects.filter(appointment_date=today).order_by('-appointment_date', 'appointment_slot')
    paginate_by = 10
    context_object_name = 'bookings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = today = date.today()
        context['filter'] = AdminFilter(self.request.GET, self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return AdminFilter(self.request.GET, queryset=queryset).qs


class AdminListPastSevenDaysView(ListView):
    model = Booking
    template_name = 'admin-planner.html'
    startdate = date.today()
    enddate = startdate - timedelta(days=7)
    queryset = Booking.objects.filter(appointment_date__range=[enddate, startdate]).order_by('appointment_date', 'appointment_slot')
    paginate_by = 10
    context_object_name = 'bookings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = today = date.today()
        context['filter'] = AdminFilter(self.request.GET, self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return AdminFilter(self.request.GET, queryset=queryset).qs


class AdminListNextSevenDaysView(ListView):
    model = Booking
    template_name = 'admin-planner.html'
    today = date.today()
    startdate = today + timedelta(days=1)
    enddate = startdate + timedelta(days=7)
    queryset = Booking.objects.filter(appointment_date__range=[startdate, enddate]).order_by('-appointment_date', 'appointment_slot')
    paginate_by = 10
    context_object_name = 'bookings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = today = date.today()
        context['filter'] = AdminFilter(self.request.GET, self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return AdminFilter(self.request.GET, queryset=queryset).qs


class AdminListThisMonthView(ListView):
    model = Booking
    template_name = 'admin-planner.html'
    today = date.today()
    queryset = Booking.objects.filter(appointment_date__year=today.year).filter(appointment_date__month=today.month).order_by('-appointment_date', 'appointment_slot')
    paginate_by = 10
    context_object_name = 'bookings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        context['filter'] = AdminFilter(self.request.GET, self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return AdminFilter(self.request.GET, queryset=queryset).qs


class AdminListThisYearView(ListView):
    model = Booking
    template_name = 'admin-planner.html'
    today = date.today()
    queryset = Booking.objects.filter(appointment_date__year=today.year).order_by('-appointment_date', 'appointment_slot')
    paginate_by = 10
    context_object_name = 'bookings'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        context['filter'] = AdminFilter(self.request.GET, self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return AdminFilter(self.request.GET, queryset=queryset).qs


class AdminAddBookingView(LoginRequiredMixin, SuccessMessageMixin, CreateView, edit.ModelFormMixin):
    context_object_name = 'bookings'
    template_name = 'admin_booking_form.html'
    form_class = AdminBookingForm
    success_message = 'Thank you for your booking.'
    success_url = reverse_lazy("admin-bookings")
    

class AdminEditBookingView(SuccessMessageMixin, UpdateView, edit.ModelFormMixin):
    template_name = 'admin_booking_form.html'
    form_class = AdminBookingForm
    model = Booking
    success_message = 'Your booking details has been updated.'
    success_url = reverse_lazy("admin-bookings")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        return super().form_valid(form)



   

class AdminCancelBookingView(SuccessMessageMixin, UpdateView):
    template_name = 'cancel_booking_form.html'
    form_class = CancelForm
    model = Booking
    success_message = 'Your booking has been cancelled'
    success_url = reverse_lazy("admin-bookings")


class AdminDeleteBookingView(SuccessMessageMixin, DeleteView):
    template_name = 'delete_booking.html'
    model = Booking
    success_url = reverse_lazy('admin-bookings')
    success_message = 'Your booking has been deleted.'


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
