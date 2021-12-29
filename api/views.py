from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Companies


def index(request):
    page = request.GET.get('page', '1')
    companies = Companies.objects.order_by('-amount')
    paginator = Paginator(companies, 15)
    page_obj = paginator.get_page(page)
    context = {'companies': page_obj, 'page': page}
    return render(request, 'index.html', context=context)
