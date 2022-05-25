from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('gallery', views.Gallery.as_view(), name='gallery'),
    path('booking', views.BookingPage.as_view(), name='booking'),
    path('bookings', views.ListBookings.as_view(), name='bookings'),
]
