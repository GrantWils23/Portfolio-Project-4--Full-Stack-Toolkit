from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('gallery', views.Gallery.as_view(), name='gallery'),
    path('bookings', views.ListBookings.as_view(), name='bookings'),
    path('add_booking', views.AddBookingView.as_view(), name='add-booking'),
    path('<int:pk>', views.ViewBooking.as_view(), name='booking')
    # path('author/<int:pk>/', AuthorUpdateView.as_view(), name='author-update'),
    # path('author/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
]

