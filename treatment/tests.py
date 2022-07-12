from django.test import TestCase
from django.urls import reverse, resolve
import datetime
from django.contrib.auth.models import User
from .views import TreatmentListView, ServicesListView

# Create your tests here.

class TestUrls(TestCase):

    def test_price_list_view_resolves(self):
        url = reverse('price-list')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, TreatmentListView)

    def test_services_list_view_resolves(self):
        url = reverse('services')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, ServicesListView)