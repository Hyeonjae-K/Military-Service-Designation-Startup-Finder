from rest_framework import routers
from api.viewsets import StartupsViewSet

router = routers.DefaultRouter()

router.register(r'startups', StartupsViewSet)
