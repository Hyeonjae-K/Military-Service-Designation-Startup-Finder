from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q

from .models import Startups


def startups(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    fil = request.GET.get('fil', '')
    companies = Startups.objects.order_by('-amount')

    if kw:
        companies = companies.filter(
            Q(ko_name__icontains=kw) | Q(en_name__icontains=kw)).distinct()
    if fil:
        companies = companies.filter(Q(industry__icontains=fil)).distinct()

    paginator = Paginator(companies, 15)
    page_obj = paginator.get_page(page)
    context = {'companies': page_obj, 'page': page,
               'last_page_num': paginator.num_pages, 'kw': kw, 'fil': fil}
    return render(request, 'startups.html', context=context)
