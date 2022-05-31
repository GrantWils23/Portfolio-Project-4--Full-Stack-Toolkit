from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('gallery', views.Gallery.as_view(), name='gallery'),
    path('services', views.Services.as_view(), name='services'),
    path('bookings', views.ListBookings.as_view(), name='bookings'),
    path('booking', views.AddBookingView.as_view(), name='booking'),
    path('booking/<int:pk>', views.ViewBooking.as_view(), name='view-booking'),
    path('booking/<int:pk>/edit', views.EditBookingView.as_view(), name='edit-booking'),
    # path('booking/<int:pk>/edit', views.EditBookingView.as_view(), name='edit-booking')
]