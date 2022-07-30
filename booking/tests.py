from django.test import TestCase
from django.urls import reverse, resolve
import datetime
from django.contrib.auth.models import User
from .forms import CancelForm
from .views import Home, Gallery, Contact, AddBookingView, ListBookings, ViewBooking, CancelBookingView, DeleteBookingView, EditBookingView
from .views import AdminListView, AdminListTodayView, AdminListNextSevenDaysView, AdminListPastSevenDaysView, AdminListThisMonthView, AdminListThisYearView
from .views import AdminAddBookingView, AdminEditBookingView, AdminCancelBookingView, AdminDeleteBookingView
from .models import Booking, Treatment

class TestBooking(TestCase):
    ''' Test parameters of the booking '''

    @classmethod
    def setUpTestData(cls):
        print('setup test DB')
        user = User(
            username="User",
            is_active=True,
            email='test@email.com'
            )
        user.save()

        user2 = User(
            username="User2",
            is_active=True,
            email='servent@gmail.com'
            )
        user2.save()

        testtreatment = Treatment(
            treatment_type=0,
            treatment_name='FaceMassage',
            treatment_price=60,
            treatment_time='1hr',
            treatment_description="a facial massage service"
            )
        testtreatment.save()

        cls.booking = Booking.objects.create(
            booking_id=1,
            user=user,
            contact_no="+44 7838 443 444",
            treatment=testtreatment,
            email=user.email,
            booking_time=datetime.date.today(),
            appointment_date=(datetime.date.today() + datetime.timedelta(days=12)),
            appointment_slot=1,
            address_line_one="1 Test House",
            address_line_two="",
            address_line_three="",
            city="London",
            post_code="EC1V 2AC",
            additional_info="Test Text",
            cancelled=0)
        cls.booking.save()

        cls.booking2 = Booking.objects.create(
            booking_id=2,
            user=user,
            contact_no="+44 7838 303 191",
            treatment=testtreatment,
            email=user.email,
            booking_time=datetime.date.today(),
            appointment_date=(datetime.date.today() + datetime.timedelta(days=12)),
            appointment_slot=0,
            address_line_one="13 Lumpkin Lane",
            address_line_two="",
            address_line_three="",
            city="Manchester",
            post_code="MN1 23OP",
            additional_info="Test Text",
            cancelled=0
            )

        cls.booking3 = Booking.objects.create(
            booking_id=3,
            user=user2,
            contact_no="+44 7838 679 342",
            treatment=testtreatment,
            email=user2.email,
            booking_time=datetime.date.today(),
            appointment_date=(datetime.date.today() - datetime.timedelta(days=3)),
            appointment_slot=3,
            address_line_one="13 Zander Street",
            address_line_two="",
            address_line_three="",
            city="Walsall",
            post_code="WA3 3LY",
            additional_info="Test Text",
            cancelled=0
            )

    def test_unique_appointment(self):
        print("test_unique_appointment")
        print(self.booking.appointment_date, self.booking.appointment_slot)
        print(self.booking2.appointment_date, self.booking2.appointment_slot)
        form_data = {'booking': self.booking2}
        self.assertNotEqual(form_data, self.booking)

    def test_booking_date_not_old(self):
        print('test_booking_date_is_not_old')
        self.assertTrue(self.booking3.appointment_date <=
                        self.booking3.booking_time)

    def test_get_absolute_url(self):
        print('test_get_absolute_url')
        self.assertEqual(self.booking.get_absolute_url(), '/booking/1')

    def test_booking_id(self):
        self.assertTrue(self.booking.booking_id == 1)

    def test_cancelled(self):
        self.assertEqual(self.booking.cancelled, 0)
    
    def test_cancel_booking_form(self):
        print('test cancel booking form')
        form = CancelForm(data={'cancelled': 1})
        self.assertTrue(form.is_valid())


    def tearDown(self):
        print('tearDown')


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('setup test DB')
        user = User(username="User", is_active=True, email='test@email.com',)
        user.save()

        user2 = User(username="User2", is_active=True,
                     email='servent@gmail.com',)
        user2.save()

        testtreatment = Treatment(treatment_type=0, treatment_name='FaceMassage', treatment_price=60,
                                  treatment_time='1hr', treatment_description="a facial massage service")
        testtreatment.save()

        cls.booking = Booking.objects.create(booking_id=1, user=user, contact_no="+44 7838 443 444",
                                             treatment=testtreatment, email=user.email, booking_time=datetime.date.today(),
                                             appointment_date=(datetime.date.today() + datetime.timedelta(days=12)), appointment_slot=1,
                                             address_line_one="1 Test House", address_line_two="", address_line_three="", city="London",
                                             post_code="EC1V 2AC", additional_info="Test Text", cancelled=0)
        cls.booking.save()

        cls.booking2 = Booking.objects.create(booking_id=2, user=user, contact_no="+44 7838 303 191",
                                              treatment=testtreatment, email=user.email, booking_time=datetime.date.today(),
                                              appointment_date=(datetime.date.today() + datetime.timedelta(days=12)), appointment_slot=0,
                                              address_line_one="13 Lumpkin Lane", address_line_two="", address_line_three="", city="Manchester",
                                              post_code="MN1 23OP", additional_info="Test Text", cancelled=0)

        cls.booking3 = Booking.objects.create(booking_id=3, user=user2, contact_no="+44 7838 679 342",
                                              treatment=testtreatment, email=user2.email, booking_time=datetime.date.today(),
                                              appointment_date=(datetime.date.today() - datetime.timedelta(days=3)), appointment_slot=3,
                                              address_line_one="13 Zander Street", address_line_two="", address_line_three="", city="Walsall",
                                              post_code="WA3 3LY", additional_info="Test Text", cancelled=0)

class TestUrls(TestCase):

    def test_home_view_resolves(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, Home)

    def test_gallery_view_resolves(self):
        url = reverse('gallery')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, Gallery)

    def test_contact_view_resolves(self):
        url = reverse('contact')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, Contact)

    def test_bookings_view_resolves(self):
        url = reverse('bookings')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, ListBookings)

    def test_add_booking_view_url_resloves(self):
        url = reverse('booking')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, AddBookingView)

    def test_view_booking_view_url_resloves(self):
        url = reverse('view-booking', args=['2'])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, ViewBooking)

    def test_edit_booking_view_url_resloves(self):
        url = reverse('edit-booking', args=['2'])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, EditBookingView)

    def test_cancel_booking_view_url_resloves(self):
        url = reverse('cancel-booking', args=['2'])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, CancelBookingView)

    def test_delete_booking_view_url_resloves(self):
        url = reverse('delete-booking', args=['2'])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, DeleteBookingView)

    def test_admin_list_view_url_resolves(self):
        url = reverse('admin-bookings')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, AdminListView)

    def test_admin_today_view_url_resolves(self):
        url = reverse('admin-bookings-today')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, AdminListTodayView)
    
    def test_admin_next_seven_day_url_resolves(self):
        url = reverse('admin-bookings-next-7')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, AdminListNextSevenDaysView)
    
    def test_admin_past_seven_day_url_resolves(self):
        url = reverse('admin-bookings-past-7')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, AdminListPastSevenDaysView)

    def test_admin_next_month_url_resolves(self):
        url = reverse('admin-bookings-this-month')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, AdminListThisMonthView)
    
    def test_admin_this_year_url_resolves(self):
        url = reverse('admin-bookings-this-year')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, AdminListThisYearView)
        
    def test_admin_add_booking_url_resolves(self):
        url = reverse('admin-booking')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, AdminAddBookingView)
        
    def test_admin_edit_booking_url_resolves(self):
        url = reverse('admin-booking-edit', args=['2'])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, AdminEditBookingView)
        
    def test_admin_cancel_booking_url_resolves(self):
        url = reverse('admin-booking-cancel', args=['2'])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, AdminCancelBookingView)

    def test_admin_delete_booking_url_resolves(self):
        url = reverse('admin-booking-delete', args=['2'])
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, AdminDeleteBookingView)

