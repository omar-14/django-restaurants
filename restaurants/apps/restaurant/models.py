from django.db import models
from .managers import RestaurantManager


class Restaurant(models.Model):
    name = models.TextField()
    type = models.TextField()
    address = models.TextField()
    telephone = models.TextField()
    objects = RestaurantManager()

    def __str__(self) -> str:
        return '{}'.format(self.name)
