from . import views
from django.urls import path

urlpatterns = [
    path('price-list', views.TreatmentListView.as_view(), name='price-list'),
]
