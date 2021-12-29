from django.db import models


class Companies(models.Model):
    ko_name = models.CharField(max_length=64)
    en_name = models.CharField(max_length=64)
    amount = models.IntegerField()
    category = models.CharField(max_length=32, null=True)
    industry = models.CharField(max_length=16, null=True)
    logo = models.CharField(max_length=256)
