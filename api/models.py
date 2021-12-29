from django.db import models


class Companies(models.Model):
    ko_name = models.CharField(max_length=64)
    en_name = models.CharField(max_length=64)
    amount = models.IntegerField(null=True)
    category = models.CharField(max_length=32, null=True)
    industry = models.CharField(max_length=16, null=True)
    scale = models.CharField(max_length=16, null=True)
    logo = models.CharField(max_length=256, null=True)
