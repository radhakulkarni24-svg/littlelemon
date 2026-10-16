from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.name} : ${self.price}"


class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_count = models.IntegerField(default=1)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reservation_date}"
