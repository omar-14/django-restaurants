from django.db import models


class UserManager(models.Manager):
    def register_user(self, data):
        user = self.create(
            username = data['username'],
            email = data['email'],
            password = data['password']
        )

        return user