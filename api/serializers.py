from rest_framework import serializers
from .models import Startups

class StartupsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Startups
    fields = '__all__'
