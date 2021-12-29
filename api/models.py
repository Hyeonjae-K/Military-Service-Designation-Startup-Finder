from django.db import models


class Companies(models.Model):
    ko_name = models.CharField(max_length=64)
    en_name = models.CharField(max_length=64)
    amount = models.IntegerField(default=0)
    category = models.CharField(max_length=32)
    industry = models.CharField(max_length=16)
    scale = models.CharField(max_length=16)
    logo = models.CharField(max_length=256, null=True)
    update_date = models.DateTimeField()
