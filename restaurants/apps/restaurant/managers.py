from django.db import models


class RestaurantManager(models.Manager):
    def register_restaurant(self, data):
        restaurant = self.create(
            name=data['name'],
            type=data['type'],
            address=data['address'],
            telephone=data['telephone']
        )

        return restaurant
