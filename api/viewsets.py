from rest_framework import viewsets
from apscheduler.schedulers.background import BackgroundScheduler

from .models import Startups, Recruitments
from .serializers import StartupsSerializer, RecruitmentsSerializer
from .crawling import update_data

sched = BackgroundScheduler()
sched.add_job(update_data, 'cron', hour=12)
sched.start()


class StartupsViewSet(viewsets.ModelViewSet):
    queryset = Startups.objects.all()
    serializer_class = StartupsSerializer


class RecruitmentsViewSet(viewsets.ModelViewSet):
    queryset = Recruitments.objects.all()
    serializer_class = RecruitmentsSerializer
