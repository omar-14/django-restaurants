from django.db import models

class UserManager(models.Manager):
  def register_user(self, data):
    user = self.create(
      user_name = data['user_name'],
      email = data['email'],
      password = data['password']
    )

    return user