from django.db import models
import datetime


# Create your models here.

class Booking(models.Model):
   
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField(default=datetime.date.today)

    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'