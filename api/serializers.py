from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Startups, Recruitments


class StartupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startups
        fields = '__all__'


class RecruitmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruitments
        fields = '__all__'
