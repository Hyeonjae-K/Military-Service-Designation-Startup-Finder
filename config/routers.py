from rest_framework import routers
from api.viewsets import StartupsViewSet, RecruitmentsViewSet

router = routers.DefaultRouter()

router.register(r'startups', StartupsViewSet)
router.register(r'recruitments', RecruitmentsViewSet)
