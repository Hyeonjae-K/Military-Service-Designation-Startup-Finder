from rest_framework import viewsets
from apscheduler.schedulers.background import BackgroundScheduler

from .models import Companies
from .serializers import CompaniesSerializer
from .crawling import update_data

sched = BackgroundScheduler()
sched.add_job(update_data, 'cron', hour=12)
sched.start()


class CompaniesViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
