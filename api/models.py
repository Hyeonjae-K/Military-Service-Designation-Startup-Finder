from django.db import models


class Startups(models.Model):
    en_name = models.CharField(max_length=64, primary_key=True)
    ko_name = models.CharField(max_length=64)
    amount = models.IntegerField(default=0)
    category = models.CharField(max_length=32)
    industry = models.CharField(max_length=16)
    scale = models.CharField(max_length=16)
    logo = models.CharField(max_length=256, null=True)
    update_date = models.DateTimeField()


class Recruitments(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
    indystry = models.CharField(max_length=32)
    response_rate = models.FloatField()
    response_day = models.IntegerField()
    logo = models.CharField(max_length=256)
    update_date = models.DateField()
