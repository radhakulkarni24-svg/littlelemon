from django.test import TestCase, Client
from django.urls import reverse
from .models import Menu, Booking
from decimal import Decimal
from datetime import date, time


class MenuModelTest(TestCase):
    def setUp(self):
        self.item = Menu.objects.create(
            name="Lemon Pasta",
            price=Decimal("12.99"),
            description="Fresh pasta with lemon sauce",
        )

    def test_menu_str(self):
        self.assertEqual(str(self.item), "Lemon Pasta : $12.99")

    def test_menu_content(self):
        self.assertEqual(self.item.name, "Lemon Pasta")
        self.assertEqual(self.item.price, Decimal("12.99"))


class BookingModelTest(TestCase):
    def setUp(self):
        self.booking = Booking.objects.create(
            first_name="John",
            last_name="Doe",
            guest_count=4,
            reservation_date=date(2024, 12, 25),
            reservation_time=time(19, 0),
        )

    def test_booking_str(self):
        self.assertEqual(str(self.booking), "John Doe - 2024-12-25")

    def test_booking_content(self):
        self.assertEqual(self.booking.first_name, "John")
        self.assertEqual(self.booking.guest_count, 4)


class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu_item = Menu.objects.create(
            name="Greek Salad",
            price=Decimal("9.99"),
            description="Classic Greek salad",
        )

    def test_home_page(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Little Lemon")

    def test_about_page(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_menu_page(self):
        response = self.client.get(reverse("menu"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Greek Salad")

    def test_menu_item_page(self):
        response = self.client.get(reverse("menu_item", kwargs={"pk": self.menu_item.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Greek Salad")

    def test_book_page(self):
        response = self.client.get(reverse("book"))
        self.assertEqual(response.status_code, 200)
