from django.db import models

from .managers import UserManager

class User(models.Model):
  user_name = models.TextField()
  email = models.EmailField()
  password = models.TextField()
  objects = UserManager()

  def __str__(self) -> str:
    return '{}'.format(self.email)

  

  