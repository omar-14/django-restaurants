from django.db import models
from .managers import RestaurantManager


class Restaurant(models.Model):
    name = models.TextField('Name', max_length=50)
    type = models.TextField('Type', max_length=20)
    address = models.TextField('Address', max_length=100)
    telephone = models.TextField('Telephone', max_length=15)
    objects = RestaurantManager()

    def __str__(self) -> str:
        return '{}'.format(self.name)
