"""bebeauty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from booking.views import Home, Gallery, Contact, ListBookings, AddBookingView, ViewBooking, EditBookingView, DeleteBookingView, CancelBookingView
from booking.views import AdminListView, AdminListTodayView, AdminListPastSevenDaysView, AdminListNextSevenDaysView, AdminListThisMonthView, AdminListThisYearView
from booking.views import AdminEditBookingView, AdminCancelBookingView, AdminDeleteBookingView
from treatment.views import TreatmentListView, ServicesListView


handler400 = 'booking.views.handler400'
handler403 = 'booking.views.handler403'
handler404 = 'booking.views.handler404'
handler500 = 'booking.views.handler500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('gallery', Gallery.as_view(), name='gallery'),
    path('services', ServicesListView.as_view(), name='services'),
    path('contact', Contact.as_view(), name='contact'),
    path('price-list', TreatmentListView.as_view(), name='price-list'),
    path('bookings', ListBookings.as_view(), name='bookings'),
    path('booking', AddBookingView.as_view(), name='booking'),
    path('booking/<int:pk>', ViewBooking.as_view(), name='view-booking'),
    path('booking/<int:pk>/edit', EditBookingView.as_view(), name='edit-booking'),
    path('booking/<int:pk>/cancel', CancelBookingView.as_view(), name='cancel-booking'),
    path('booking/<int:pk>/delete', DeleteBookingView.as_view(), name='delete-booking'),
    path('accounts/', include('allauth.urls')),
    path('admin-bookings', AdminListView.as_view(), name='admin-bookings'),
    path('admin-bookings/today', AdminListTodayView.as_view(), name='admin-bookings-today'),
    path('admin-bookings/past_7_days', AdminListPastSevenDaysView.as_view(), name='admin-bookings-past-7'),
    path('admin-bookings/next_7_days', AdminListNextSevenDaysView.as_view(), name='admin-bookings-next-7'),
    path('admin-bookings/this-month', AdminListThisMonthView.as_view(), name='admin-bookings-this-month'),
    path('admin-bookings/this-year', AdminListThisYearView.as_view(), name='admin-bookings-this-year'),
    path('booking-admin/<int:pk>/edit', AdminEditBookingView.as_view(), name='admin-booking-edit'),
    path('booking-admin/<int:pk>/cancel', AdminCancelBookingView.as_view(), name='admin-booking-cancel'),
    path('booking-admin/<int:pk>/delete', AdminDeleteBookingView.as_view(), name='admin-booking-delete'),
]
