from django.db import models

class Companies(models.Model):
  name = models.CharField(max_length=64)
  slug = models.CharField(max_length=64)
  amount = models.IntegerField()
  logo = models.CharField(max_length=256)
