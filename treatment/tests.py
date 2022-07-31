''' tests.py for the treatment app '''
from django.test import TestCase
from django.urls import reverse, resolve
from .views import TreatmentListView, ServicesListView


class TestUrls(TestCase):
    ''' The Test Urls class to run during a test suite '''
    def test_price_list_view_resolves(self):
        ''' tests the price list view url resolves '''
        url = reverse('price-list')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, TreatmentListView)

    def test_services_list_view_resolves(self):
        ''' tests the services list view url resolves '''
        url = reverse('services')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, ServicesListView)
