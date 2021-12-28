from rest_framework import routers
from api.viewsets import CompaniesViewSet

router = routers.DefaultRouter()

router.register(r'companies', CompaniesViewSet)
