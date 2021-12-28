from rest_framework import viewsets

from .models import Companies
from .serializers import CompaniesSerializer


class CompaniesViewSet(viewsets.ModelViewSet):
  queryset = Companies.objects.all()
  serializer_class = CompaniesSerializer
