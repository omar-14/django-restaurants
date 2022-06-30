from django.db import models

class Restaurant(models.Model):
  name = models.TextField()
  type = models.TextField()
  address = models.TextField()
  telephone = models.TextField()

  def __str__(self) -> str:
    return '{}'.format(self.name)