from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Booking
# from .forms import CommentForm


def home(request):
    return render(request, "../templates/index.html")

# class Home(View):
#     template_name = 'index.html'

# class BookingList(generic.ListView):
#     model = Booking()
#     template_name = 'index.html'

# def say_hello(request):
#     return (HttpResponse('Hello!'))
