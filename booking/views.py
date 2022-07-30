
from datetime import date, timedelta
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, DetailView, ListView, edit
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import request
from .models import Booking
from .forms import BookingForm, CancelForm, AdminBookingForm
from .filters import AdminFilter


class Home(TemplateView):
    ''' The index home view '''
    template_name = 'index.html'


class Gallery(TemplateView):
    ''' the gallery view '''
    template_name = 'gallery.html'


class Contact(TemplateView):
    ''' the contact page view '''
    template_name = 'contact.html'


class ListBookings(ListView):
    ''' the users list of bookings view '''
    model = Booking
    queryset = Booking.objects.all().order_by('-booking_id')
    template_name = 'bookings.html'
    paginate_by = 6
    context_object_name = 'bookings'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class ViewBooking(DetailView):
    ''' the detail view of a users booking '''
    template_name = 'booking_details.html'
    model = Booking
    template_name_suffix = '<int:pk>'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class AddBookingView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    ''' The create booking view  '''
    context_object_name = 'bookings'
    template_name = 'booking_form.html'
    form_class = BookingForm
    success_message = 'Thank you for your booking.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        body0 = (f"Hello {form.instance.user} ({form.instance.contact_no.as_national}),\n\nYour '{form.instance.treatment}' booking is on {form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 9am to 11am. The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body1 = (f"Hello {form.instance.user} ({form.instance.contact_no.as_national}),\n\nYour '{form.instance.treatment}' booking is on {form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 12am to 2pm. The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body2 = (f"Hello {form.instance.user} ({form.instance.contact_no.as_national}),\n\nYour '{form.instance.treatment}' booking is on {form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 3pm to 5pm. The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body3 = (f"Hello {form.instance.user} ({form.instance.contact_no.as_national}),\n\nYour '{form.instance.treatment}' booking is on {form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 6pm to 8pm. The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        form.save()
        if form.instance.appointment_slot == 0:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body0,
                "info@BeBeauty.co.uk",
                [self.request.user.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        elif form.instance.appointment_slot == 1:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body1,
                "info@BeBeauty.co.uk",
                [self.request.user.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        elif form.instance.appointment_slot == 2:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body2,
                "info@BeBeauty.co.uk",
                [self.request.user.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        else:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body3,
                "info@BeBeauty.co.uk",
                [self.request.user.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        return super().form_valid(form)
        

class EditBookingView(SuccessMessageMixin, UpdateView):
    ''' the edit booking view for a user '''
    template_name = 'booking_form.html'
    form_class = BookingForm
    model = Booking
    success_message = 'Your booking details has been updated.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        body0 = (f"Hello {form.instance.user} ({form.instance.contact_no.as_national}),\n\nYour booking (ref: #{form.instance.booking_id}) has been updated. \n\n{form.instance.treatment},\n{form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 9am to 11am.\n\nThe address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body1 = (f"Hello {form.instance.user} ({form.instance.contact_no.as_national}),\n\nYour booking (ref: #{form.instance.booking_id}) has been updated. \n\n{form.instance.treatment},\n{form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 12am to 2pm.\n\nThe address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body2 = (f"Hello {form.instance.user} ({form.instance.contact_no.as_national}),\n\nYour booking (ref: #{form.instance.booking_id}) has been updated. \n\n{form.instance.treatment},\n{form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 3pm to 5pm.\n\n The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body3 = (f"Hello {form.instance.user} ({form.instance.contact_no.as_national}),\n\nYour booking (ref: #{form.instance.booking_id}) has been updated. \n\n{form.instance.treatment},\n{form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 6pm to 8pm.\n\n The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        form.save()
        if form.instance.appointment_slot == 0:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body0,
                "info@BeBeauty.co.uk",
                [self.request.user.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        elif form.instance.appointment_slot == 1:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body1,
                "info@BeBeauty.co.uk",
                [self.request.user.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        elif form.instance.appointment_slot == 2:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body2,
                "info@BeBeauty.co.uk",
                [self.request.user.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        else:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body3,
                "info@BeBeauty.co.uk",
                [self.request.user.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        return super().form_valid(form)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class CancelBookingView(SuccessMessageMixin, UpdateView):
    ''' the user cancel booking view '''
    template_name = 'cancel_booking_form.html'
    form_class = CancelForm
    model = Booking
    success_message = 'Your booking has been cancelled'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        body0 = (f"Hello {form.instance.user} ({form.instance.contact_no.as_national}),\n\nYour booking (ref: #{form.instance.booking_id}) has been cancelled.\n\n We are sorry you can't make the appointment, We look forward to doing business with you in the future.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body1 = (f"Hello {form.instance.user} ({form.instance.contact_no.as_national}),\n\nYour booking (ref: #{form.instance.booking_id}) has been cancelled.\n\n We are sorry you can't make the appointment, We look forward to doing business with you in the future.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body2 = (f"Hello {form.instance.user} ({form.instance.contact_no.as_national}),\n\nYour booking (ref: #{form.instance.booking_id}) has been cancelled.\n\n We are sorry you can't make the appointment, We look forward to doing business with you in the future.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body3 = (f"Hello {form.instance.user} ({form.instance.contact_no.as_national}),\n\nYour booking (ref: #{form.instance.booking_id}) has been cancelled.\n\n We are sorry you can't make the appointment, We look forward to doing business with you in the future.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        form.save()
        if form.instance.appointment_slot == 0:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body0,
                "info@BeBeauty.co.uk",
                [self.request.user.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        elif form.instance.appointment_slot == 1:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body1,
                "info@BeBeauty.co.uk",
                [self.request.user.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        elif form.instance.appointment_slot == 2:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body2,
                "info@BeBeauty.co.uk",
                [self.request.user.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        else:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body3,
                "info@BeBeauty.co.uk",
                [self.request.user.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        return super().form_valid(form)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class DeleteBookingView(SuccessMessageMixin, DeleteView):
    ''' the user delete booking view '''
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
    ''' the admins list of bookings view '''
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
    ''' the admins list filtered today of bookings view '''
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
    ''' the amdins list filter past seven days of bookings views '''
    model = Booking
    template_name = 'admin-planner.html'
    startdate = date.today()
    enddate = startdate - timedelta(days=7)
    queryset = Booking.objects.filter(appointment_date__range=[enddate, startdate]).order_by('appointment_date', 'appointment_slot')
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


class AdminListNextSevenDaysView(ListView):
    ''' the admins list filter next seven days of bookings view '''
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
        context['today'] = date.today()
        context['filter'] = AdminFilter(self.request.GET, self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return AdminFilter(self.request.GET, queryset=queryset).qs


class AdminListThisMonthView(ListView):
    ''' the admins list filter next month of bookings view '''
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
    ''' the amdins list year of bookings view '''
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
    ''' admins view to create a booking '''
    template_name = 'admin_booking_form.html'
    form_class = AdminBookingForm
    success_message = 'Thank you for your booking.'
    success_url = reverse_lazy("admin-bookings")

    def form_valid(self, form):
        body0 = (f"Hello,\n\n This is your booking conformation for your '{form.instance.treatment}' session. Your booking is on {form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 9am to 11am. The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body1 = (f"Hello,\n\n This is your booking conformation for your '{form.instance.treatment}' session. Your booking is on {form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 12am to 2pm. The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body2 = (f"Hello,\n\n This is your booking conformation for your '{form.instance.treatment}' session. Your booking is on {form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 3pm to 5pm. The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body3 = (f"Hello,\n\n This is your booking conformation for your '{form.instance.treatment}' session. Your booking is on {form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 6pm to 8pm. The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        form.save()
        if form.instance.appointment_slot == 0:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body0,
                "info@BeBeauty.co.uk",
                [form.instance.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        elif form.instance.appointment_slot == 1:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body1,
                "info@BeBeauty.co.uk",
                [form.instance.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        elif form.instance.appointment_slot == 2:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body2,
                "info@BeBeauty.co.uk",
                [form.instance.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        else:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body3,
                "info@BeBeauty.co.uk",
                [form.instance.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        return super().form_valid(form)


class AdminEditBookingView(SuccessMessageMixin, UpdateView, edit.ModelFormMixin):
    ''' admins view to edit a booking '''
    template_name = 'admin_booking_form.html'
    form_class = AdminBookingForm
    model = Booking
    success_message = 'Your booking details has been updated.'
    success_url = reverse_lazy("admin-bookings")

    def form_valid(self, form):
        body0 = (f"Hello,\n\n  Your booking has been updated.\n\nYour new session details are:\n\n'{form.instance.treatment}' session is on {form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 9am to 11am. The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body1 = (f"Hello,\n\n  Your booking has been updated.\n\nYour new session details are:\n\n'{form.instance.treatment}' session is on {form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 12am to 2pm. The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body2 = (f"Hello,\n\n  Your booking has been updated.\n\nYour new session details are:\n\n'{form.instance.treatment}' session is on {form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 3pm to 5pm. The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body3 = (f"Hello,\n\n  Your booking has been updated.\n\nYour new session details are:\n\n'{form.instance.treatment}' session is on {form.instance.appointment_date.strftime('%A')} - {form.instance.appointment_date.strftime('%d/%m/%Y')}, for 6pm to 8pm. The address of the booking will take place at is:\n{form.instance.address_line_one},\n{form.instance.city},\n{form.instance.post_code}.\n\nIf you have any questions regarding your booking, please do not hesitate to get into contact with us.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        form.save()
        if form.instance.appointment_slot == 0:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body0,
                "info@BeBeauty.co.uk",
                [form.instance.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        elif form.instance.appointment_slot == 1:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body1,
                "info@BeBeauty.co.uk",
                [form.instance.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        elif form.instance.appointment_slot == 2:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body2,
                "info@BeBeauty.co.uk",
                [form.instance.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        else:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body3,
                "info@BeBeauty.co.uk",
                [form.instance.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        return super().form_valid(form)


class AdminCancelBookingView(SuccessMessageMixin, UpdateView, edit.ModelFormMixin):
    ''' amdins view to cancel booking '''
    template_name = 'cancel_booking_form.html'
    form_class = CancelForm
    model = Booking
    success_url = reverse_lazy("admin-bookings")
    success_message = 'Your booking has been cancelled'

    def form_valid(self, form):
        body0 = (f"Hello,\n\nYour booking (ref: #{form.instance.booking_id}) has been cancelled.\n\n We are sorry you can't make the appointment, We look forward to doing business with you in the future.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body1 = (f"Hello,\n\nYour booking (ref: #{form.instance.booking_id}) has been cancelled.\n\n We are sorry you can't make the appointment, We look forward to doing business with you in the future.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body2 = (f"Hello,\n\nYour booking (ref: #{form.instance.booking_id}) has been cancelled.\n\n We are sorry you can't make the appointment, We look forward to doing business with you in the future.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        body3 = (f"Hello,\n\nYour booking (ref: #{form.instance.booking_id}) has been cancelled.\n\n We are sorry you can't make the appointment, We look forward to doing business with you in the future.\n\nBest Wishes\n\nThe BeBeauty Team\n\nTel: +44 7838 555 323\nEmail: info@BeBeauty.co.uk")
        form.save()
        if form.instance.appointment_slot == 0:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body0,
                "info@BeBeauty.co.uk",
                [form.instance.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        elif form.instance.appointment_slot == 1:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body1,
                "info@BeBeauty.co.uk",
                [form.instance.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        elif form.instance.appointment_slot == 2:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body2,
                "info@BeBeauty.co.uk",
                [form.instance.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        else:
            email = EmailMessage(
                f"BeBeauty Booking Confirmation {form.instance.booking_id}",
                body3,
                "info@BeBeauty.co.uk",
                [form.instance.email, "grantwils.23@googlemail.com"],
            )
            email.send(fail_silently=False)
        return super().form_valid(form)


class AdminDeleteBookingView(SuccessMessageMixin, DeleteView):
    ''' admins view to delete bookings '''
    template_name = 'delete_booking.html'
    model = Booking
    success_url = reverse_lazy('admin-bookings')
    success_message = 'Your booking has been deleted.'

    def delete(self, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(AdminDeleteBookingView, self).delete(request, *args, **kwargs)


# Error Handlers #
def handler400(request, exception):
    ''' error400 handler '''
    return render(request, 'handler400.html', status=400)


def handler403(request, exception):
    ''' error403 handler '''
    return render(request, 'handler403.html', status=403)


def handler404(request, exception):
    ''' error404 handler '''
    return render(request, 'handler404.html', status=404)


def handler500(request):
    ''' error 500 handler '''
    return render(request, 'handler500.html', status=500)
