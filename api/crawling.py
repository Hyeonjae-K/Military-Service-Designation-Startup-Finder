from .models import Companies
import requests
import pandas as pd
from datetime import date
from urllib import request
from django.utils import timezone
import django
django.setup()


today = str(date.today())
xls_path = 'data_files/%s.xls' % today
startups = {}
company_names = company_industries = company_scales = None


def _get_data():
    global startups, company_names, company_industries, company_scales

    request.urlretrieve(
        'https://work.mma.go.kr/caisBYIS/search/downloadBYJJEopCheExcel.do', xls_path)

    df = pd.read_excel(xls_path)[['업체명', '업종', '기업규모']]
    del_strs = ['(주)', '(유)', '(합)', '㈜', '주식회사']
    company_names = df['업체명'].values.tolist()[:-1]
    for x in del_strs:
        company_names = [name.replace(x, '').strip() for name in company_names]
    company_industries = df['업종'].values.tolist()[:-1]
    company_scales = df['기업규모'].values.tolist()[:-1]

    items = requests.get(
        'https://startupspace.kr/api/companies').json()['items']
    amounts = requests.get(
        'https://startupspace.kr/api/amounts').json()['item']
    for item in items:
        key = item['id']
        startups[key] = {
            'ko_name': item['name'],
            'category': item['category']
        }
        if key in amounts:
            startups[key]['amount'] = amounts[key]
        try:
            startups[key]['logo'] = item['logo']['url']
        except:
            startups[key]['logo'] = None


def update_data():
    _get_data()
    companies, new_companies, update_companies = [], [], []
    datetime = timezone.now()

    for key, startup in startups.items():
        try:
            idx = company_names.index(startup['ko_name'])
            companies.append({
                'en_name': key,
                'ko_name': startup['ko_name'],
                'amount': startup['amount'],
                'category': startup['category'],
                'industry': company_industries[idx],
                'scale': company_scales[idx],
                'logo': startup['logo']
            })
        except:
            continue

    for data in companies:
        try:
            company = Companies.objects.get(en_name=data['en_name'])
            company.amount = data['amount']
            company.scale = data['scale']
            company.logo = data['logo']
            company.update_date = datetime
            update_companies.append(company)
        except:
            company = Companies(ko_name=data['ko_name'], en_name=data['en_name'], amount=data['amount'], category=data['category'],
                                industry=data['industry'], scale=data['scale'], logo=data['logo'], update_date=datetime)
            new_companies.append(company)

    if update_companies:
        Companies.objects.bulk_update(
            update_companies, ['amount', 'scale', 'logo', 'update_date'])
    if new_companies:
        Companies.objects.bulk_create(new_companies)
